X1VulnScanner 🔎

A lightweight web security scanner designed for educational and authorized security testing.

X1VulnScanner analyzes a target URL and reports detected security findings with severity and confidence information.

---

✨ Features

- HTTP status detection
- Final URL detection
- Basic server information
- Security finding detection
- Severity classification
- Confidence level
- Structured security reports
- Simple command-line interface
- Report output storage

---

📥 Installation

1. Clone the repository

git clone https://github.com/X1-starr/X1VulnScanner.git

2. Enter the project directory

cd X1VulnScanner

3. Install dependencies

pip install -r requirements.txt

If your system uses "pip3":

pip3 install -r requirements.txt

---

🚀 Usage

Run the scanner with a target URL:

python3 main.py https://example.com

Example:

python3 main.py https://example.com

The scanner will analyze the target and display the detected security findings in the terminal.

---

📊 Reports

Scan results can be stored in the project's report directory:

reports/

This allows scan results to be preserved for later review.

---

🖥️ Example

[*] X1 Scanner started
[*] Target: https://example.com

[+] HTTP Status: 200
[+] Final URL: https://example.com/
[+] Server: Unknown

━━━━━━━━━━━━ X1 SECURITY FINDINGS ━━━━━━━━━━━━

┌─ FINDING #1 ─────────────────────────────
│ Severity   : LOW
│ Confidence : HIGH
└───────────────────────────────────────────

---

⚠️ Legal & Ethical Use

X1VulnScanner is provided for educational and authorized security-testing purposes.

Only scan websites, applications, and systems that you own or have explicit permission to test.

Do not use this tool to scan unauthorized targets.

The author is not responsible for misuse of this software.

---

👤 Author

X1-starr

GitHub:

https://github.com/X1-starr

---

📄 License

See the repository for licensing information.
