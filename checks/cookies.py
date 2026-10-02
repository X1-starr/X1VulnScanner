from models import Finding


def split_set_cookie_header(header):
    """
    Split Set-Cookie safely.
    Commas inside Expires=... are not cookie separators.
    """
    cookies = []
    current = []
    in_expires = False

    i = 0

    while i < len(header):
        char = header[i]

        if header[i:i + 8].lower() == "expires=":
            in_expires = True

        if char == "," and not in_expires:
            cookie = "".join(current).strip()

            if cookie:
                cookies.append(cookie)

            current = []
            i += 1
            continue

        current.append(char)

        if in_expires and char == ";":
            in_expires = False

        i += 1

    cookie = "".join(current).strip()

    if cookie:
        cookies.append(cookie)

    return cookies


def parse_cookie(cookie):
    """
    Parse cookie name/value and attributes.
    """
    parts = [part.strip() for part in cookie.split(";")]

    if not parts or "=" not in parts[0]:
        return None

    name, value = parts[0].split("=", 1)

    parsed = {
        "name": name.strip(),
        "value": value.strip(),
        "secure": False,
        "httponly": False,
        "samesite": None,
        "domain": None,
        "path": None,
    }

    for part in parts[1:]:
        if not part:
            continue

        lower = part.lower()

        if lower == "secure":
            parsed["secure"] = True

        elif lower == "httponly":
            parsed["httponly"] = True

        elif lower.startswith("samesite="):
            parsed["samesite"] = part.split("=", 1)[1].strip().lower()

        elif lower.startswith("domain="):
            parsed["domain"] = part.split("=", 1)[1].strip()

        elif lower.startswith("path="):
            parsed["path"] = part.split("=", 1)[1].strip()

    return parsed


def add_finding(result, response, title, severity, cookie, impact,
                recommendation, explanation):

    result.add(Finding(
        title=title,
        severity=severity,
        confidence="MEDIUM",
        category="Cookie Security",
        location=response.url,
        evidence=cookie,
        impact=impact,
        recommendation=recommendation,
        explanation=explanation
    ))


def check_cookies(response, result):
    cookies = response.headers.get("Set-Cookie")

    if not cookies:
        return result

    cookie_lines = split_set_cookie_header(cookies)

    seen = set()

    for cookie in cookie_lines:
        cookie = cookie.strip()

        if not cookie:
            continue

        parsed = parse_cookie(cookie)

        if not parsed:
            continue

        name = parsed["name"]
        name_lower = name.lower()

        # Prevent duplicate reports.
        if name_lower in seen:
            continue

        seen.add(name_lower)

        secure = parsed["secure"]
        httponly = parsed["httponly"]
        samesite = parsed["samesite"]

        # ---------------------------------------------------------
        # __Secure- prefix
        # ---------------------------------------------------------

        if name.startswith("__Secure-") and not secure:
            add_finding(
                result,
                response,
                "Invalid __Secure- Cookie Prefix",
                "MEDIUM",
                cookie,
                "The cookie uses the __Secure- prefix without the Secure attribute.",
                "Add the Secure attribute or remove the __Secure- prefix.",
                "Cookies using the __Secure- prefix are expected to use Secure."
            )

        # ---------------------------------------------------------
        # __Host- prefix
        # ---------------------------------------------------------

        if name.startswith("__Host-"):

            if not secure:
                add_finding(
                    result,
                    response,
                    "Invalid __Host- Cookie Prefix",
                    "MEDIUM",
                    cookie,
                    "The cookie uses the __Host- prefix without Secure.",
                    "Add the Secure attribute.",
                    "A __Host- cookie must use the Secure attribute."
                )

            if parsed["domain"] is not None:
                add_finding(
                    result,
                    response,
                    "Invalid __Host- Cookie Domain",
                    "MEDIUM",
                    cookie,
                    "A __Host- cookie contains a Domain attribute.",
                    "Remove the Domain attribute.",
                    "A __Host- cookie must not specify Domain."
                )

            if parsed["path"] != "/":
                add_finding(
                    result,
                    response,
                    "Invalid __Host- Cookie Path",
                    "MEDIUM",
                    cookie,
                    "A __Host- cookie does not use Path=/.",
                    "Set Path=/.",
                    "A __Host- cookie must use Path=/."
                )

        # ---------------------------------------------------------
        # SameSite=None
        # ---------------------------------------------------------

        if samesite == "none" and not secure:
            add_finding(
                result,
                response,
                "SameSite=None Without Secure",
                "MEDIUM",
                cookie,
                "A SameSite=None cookie without Secure may be rejected by modern browsers and does not provide the expected transport restriction.",
                "Use Secure with SameSite=None.",
                "Modern browser cookie behavior requires Secure when SameSite=None is used."
            )

        # ---------------------------------------------------------
        # Sensitive-looking cookies
        # ---------------------------------------------------------

        sensitive_keywords = (
            "session",
            "sess",
            "auth",
            "token",
            "jwt",
            "login",
        )

        is_sensitive = any(
            keyword in name_lower
            for keyword in sensitive_keywords
        )

        # Missing Secure on a potentially sensitive cookie.
        if is_sensitive and not secure:
            add_finding(
                result,
                response,
                "Potentially Sensitive Cookie Missing Secure",
                "MEDIUM",
                cookie,
                "A potentially sensitive cookie does not have the Secure attribute.",
                "Consider adding Secure so the cookie is only sent over HTTPS.",
                "Cookies carrying authentication or session-related information generally benefit from the Secure attribute."
            )

        # Missing HttpOnly on a potentially sensitive cookie.
        if is_sensitive and not httponly:
            add_finding(
                result,
                response,
                "Potentially Sensitive Cookie Missing HttpOnly",
                "MEDIUM",
                cookie,
                "A potentially sensitive cookie can potentially be accessed by client-side JavaScript.",
                "Use HttpOnly when client-side JavaScript does not need to access the cookie.",
                "HttpOnly prevents normal client-side JavaScript from reading the cookie."
            )

        # ---------------------------------------------------------
        # Informational SameSite observation
        # ---------------------------------------------------------

        if samesite is None:
            add_finding(
                result,
                response,
                "Cookie Missing SameSite Attribute",
                "LOW",
                cookie,
                "The cookie does not explicitly define SameSite behavior.",
                "Consider configuring an appropriate SameSite value based on application requirements.",
                "SameSite controls when cookies are sent with cross-site requests. Its absence alone does not prove a vulnerability."
            )

    return result
