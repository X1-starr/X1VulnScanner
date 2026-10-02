from models import Finding


SECURITY_HEADERS = {
    "Content-Security-Policy": {
        "severity": "MEDIUM",
        "impact": "Browser-side protections may be reduced.",
        "recommendation": "Configure an appropriate Content-Security-Policy.",
        "explanation": (
            "CSP controls which resources a browser is allowed to load. "
            "Its absence does not by itself prove an XSS vulnerability."
        )
    },

    "Strict-Transport-Security": {
        "severity": "MEDIUM",
        "impact": "HTTPS enforcement may be weaker.",
        "recommendation": (
            "Configure HSTS after confirming HTTPS is working correctly."
        ),
        "explanation": (
            "HSTS helps browsers use HTTPS for the site and reduces "
            "certain downgrade-related risks."
        )
    },

    "X-Content-Type-Options": {
        "severity": "LOW",
        "impact": "MIME-type sniffing protections may be reduced.",
        "recommendation": "Set X-Content-Type-Options to nosniff.",
        "explanation": (
            "This header helps prevent MIME-type sniffing. "
            "The commonly recommended value is nosniff."
        )
    },

    "Referrer-Policy": {
        "severity": "LOW",
        "impact": "Referrer information may be disclosed more broadly than necessary.",
        "recommendation": "Configure an appropriate Referrer-Policy.",
        "explanation": (
            "Referrer-Policy controls how much referrer information "
            "is sent with outgoing requests."
        )
    },

    "Permissions-Policy": {
        "severity": "LOW",
        "impact": "Browser features may not be explicitly restricted.",
        "recommendation": (
            "Configure Permissions-Policy according to the application's requirements."
        ),
        "explanation": (
            "Permissions-Policy allows a site to control access to "
            "selected browser features."
        )
    },
}


def check_headers(response, result):
    headers = response.headers

    # Header names are case-insensitive.
    present_headers = {
        header.lower(): value
        for header, value in headers.items()
    }

    for header, info in SECURITY_HEADERS.items():

        if header.lower() not in present_headers:
            finding = Finding(
                title=f"Missing Security Header: {header}",
                severity=info["severity"],
                confidence="MEDIUM",
                category="Security Headers",
                location=response.url,
                evidence=f"{header} header was not present.",
                impact=info["impact"],
                recommendation=info["recommendation"],
                explanation=info["explanation"]
            )

            result.add(finding)

    return result
