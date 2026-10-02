X1VulnScanner

Web Security Auditor V2

X1VulnScanner is a lightweight Python-based web security auditing tool designed to identify common security configuration issues in web applications.

«Created by X1»

---

Features

- Security HTTP header analysis
- Cookie security attribute checks
- Severity classification
- Finding confidence levels
- Evidence collection
- Impact explanations
- Security recommendations
- Modular checker architecture
- Clean terminal-based output

Security Headers Checked

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

Cookie Attributes Checked

- Secure
- HttpOnly
- SameSite

---

Project Structure

X1VulnScanner/
├── main.py
├── scanner.py
├── models.py
├── checks/
│   ├── __init__.py
│   ├── headers.py
│   └── cookies.py
├── reports/
│   └── __init__.py
├── tests/
├── requirements.txt
├── .gitignore
└── README.md

---

Installation

Clone the repository:

git clone https://github.com/X1-starr/X1VulnScanner.git
cd X1VulnScanner

Install the required Python package:

pip install -r requirements.txt

---

Usage

Run the scanner against a web target:

python3 main.py https://example.com

The scanner reports detected findings together with:

- Severity
- Confidence
- Category
- Location
- Evidence
- Explanation
- Impact
- Recommendation

---

Example

X1VulnScanner
Web Security Auditor V2

Created by X1

[*] X1 Scanner started
[*] Target: https://example.com

[+] HTTP Status: 200
[+] Final URL: https://example.com/
[+] Server: cloudflare

━━━━━━━━━━━━ X1 SECURITY FINDINGS ━━━━━━━━━━━━

---

Severity Levels

Severity| Meaning
CRITICAL| Extremely serious security issue
HIGH| Significant security issue
MEDIUM| Security weakness requiring attention
LOW| Lower-impact security issue
INFO| Informational observation

Severity indicates the potential importance of a finding and does not by itself prove exploitability.

---

Important Note

X1VulnScanner is intended for authorized security testing, defensive research, and educational use.

Only scan websites and systems that you own or have explicit permission to test.

The absence of a finding does not guarantee that a target is secure, and detecting a configuration weakness does not necessarily mean the target is directly exploitable.

---

Roadmap

Future versions may include additional non-destructive security checks, improved reporting, testing support, and expanded detection capabilities.

---

Author

X1

Cybersecurity learning project.

---

License

This project is provided for educational and authorized security-testing purposes.
