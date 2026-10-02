
# X1VulnScanner

## Web Security Auditor V2

X1VulnScanner is a lightweight Python-based web security auditing tool designed to identify common security configuration issues in web applications.

> Created by X1

---

## Features

- HTTP status and final URL detection
- Security HTTP header analysis
- Cookie security attribute analysis
- Severity classification
- Finding confidence levels
- Evidence collection
- Impact explanations
- Security recommendations
- Modular checker architecture
- Interactive X1 terminal interface
- Startup animation
- Interactive main menu
- Clean security findings output

---

## Security Headers Checked

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

---

## Cookie Attributes Checked

- Secure
- HttpOnly
- SameSite
- Cookie attribute parsing
- Sensitive cookie detection
- __Secure- and __Host- prefix checks
- SameSite=None + Secure validation

---

## Finding Information

Each finding can contain:

- Severity
- Confidence
- Category
- Location
- Evidence
- Explanation
- Impact
- Recommendation

---

## Project Structure

`text
X1VulnScanner/
├── main.py
├── scanner.py
├── models.py
├── x1.sh
├── checks/
│   initit__.py
│   ├── headers.py
│   └── cookies.py
├── reports/
│   initit__.py
├── tests/
├── requirements.txt
├── .gitignore
└── README.md


---

Installation

Clone the repository:

git clone https://github.com/X1-starr/X1VulnScanner.git
cd X1VulnScanner

Install the required Python packages:

pip install -r requirements.txt


---

Usage

Direct Scanner

Run the scanner against an authorized web target:

python3 main.py https://example.com

X1 Terminal Interface

Launch the interactive X1 interface:

chmod +x x1.sh
./x1.sh

The interface provides:

[1] Scan Target
[2] View Reports
[3] Scanner Information
[4] Settings
[5] Exit


---

Example

╔══════════════════════════════════════════════╗
║                                              ║
║              X1 VULN SCANNER                 ║
║              Security Auditor                ║
║                                              ║
╚══════════════════════════════════════════════╝

[*] X1 Scanner started
[*] Target: https://example.com

[+] HTTP Status: 200
[+] Final URL: https://example.com/

━━━━━━━━━━━━ X1 SECURITY FINDINGS ━━━━━━━━━━━━

[01] LOW | Security Headers
     Missing Security Header: Referrer-Policy

[02] MEDIUM | Cookie Security
     Potentially Sensitive Cookie Missing HttpOnly


---

Severity Levels

Severity	Meaning

CRITICAL	Extremely serious security issue
HIGH	Significant security issue
MEDIUM	Security weakness requiring attention
LOW	Lower-impact security issue
INFO	Informational observation


Severity indicates the potential importance of a finding and does not by itself prove exploitability.


---

Architecture

X1VulnScanner uses a modular checker architecture.

Target
  │
  ▼
HTTP Scanner
  │
  ├── Security Headers
  │
  └── Cookie Analyzer
          │
          ▼
     Finding Engine
          │
          ▼
     Terminal Output

The Bash interface provides the user-facing terminal experience while the Python scanner handles the security analysis.


---

Important Note

X1VulnScanner is intended for authorized security testing, defensive research, and educational use.

Only scan websites and systems that you own or have explicit permission to test.

The absence of a finding does not guarantee that a target is secure, and detecting a configuration weakness does not necessarily mean the target is directly exploitable.


---

Roadmap

Planned improvements may include:

Improved report generation

JSON and text report export

Advanced cookie analysis

Information disclosure checks

Technology detection

Improved false-positive reduction

Expanded non-destructive security checks

Enhanced terminal interface



---

Author

X1

Cybersecurity learning project.


---

License

This project is provided for educational and authorized security-testing purposes.
