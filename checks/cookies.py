from models import Finding


def check_cookies(response, result):
    cookies = response.headers.get("Set-Cookie")

    if not cookies:
        return result

    cookie_lines = cookies.split(",")

    for cookie in cookie_lines:
        cookie = cookie.strip()

        if "Secure" not in cookie:
            result.add(Finding(
                title="Cookie Missing Secure Attribute",
                severity="MEDIUM",
                confidence="HIGH",
                category="Cookie Security",
                location=response.url,
                evidence=cookie,
                impact="The cookie may be sent over a non-HTTPS connection.",
                recommendation="Add the Secure attribute to cookies when appropriate.",
                explanation="The Secure attribute tells the browser to send the cookie only over HTTPS connections."
            ))

        if "HttpOnly" not in cookie:
            result.add(Finding(
                title="Cookie Missing HttpOnly Attribute",
                severity="MEDIUM",
                confidence="HIGH",
                category="Cookie Security",
                location=response.url,
                evidence=cookie,
                impact="Client-side scripts may be able to access the cookie.",
                recommendation="Add the HttpOnly attribute to cookies that do not need JavaScript access.",
                explanation="The HttpOnly attribute prevents normal client-side JavaScript from reading the cookie."
            ))

        if "SameSite" not in cookie:
            result.add(Finding(
                title="Cookie Missing SameSite Attribute",
                severity="LOW",
                confidence="HIGH",
                category="Cookie Security",
                location=response.url,
                evidence=cookie,
                impact="Cross-site cookie behavior may be less restricted.",
                recommendation="Configure an appropriate SameSite attribute.",
                explanation="SameSite controls when a browser sends a cookie with cross-site requests."
            ))

    return result
