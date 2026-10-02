[1mdiff --git a/README.md b/README.md[m
[1mindex e69de29..d8e6dc2 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -0,0 +1,147 @@[m
[32m+[m[32mX1VulnScanner[m
[32m+[m
[32m+[m[32mWeb Security Auditor V2[m
[32m+[m
[32m+[m[32mX1VulnScanner is a lightweight Python-based web security auditing tool designed to identify common security configuration issues in web applications.[m
[32m+[m
[32m+[m[32m«Created by X1»[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32mFeatures[m
[32m+[m
[32m+[m[32m- Security HTTP header analysis[m
[32m+[m[32m- Cookie security attribute checks[m
[32m+[m[32m- Severity classification[m
[32m+[m[32m- Finding confidence levels[m
[32m+[m[32m- Evidence collection[m
[32m+[m[32m- Impact explanations[m
[32m+[m[32m- Security recommendations[m
[32m+[m[32m- Modular checker architecture[m
[32m+[m[32m- Clean terminal-based output[m
[32m+[m
[32m+[m[32mSecurity Headers Checked[m
[32m+[m
[32m+[m[32m- Content-Security-Policy[m
[32m+[m[32m- Strict-Transport-Security[m
[32m+[m[32m- X-Content-Type-Options[m
[32m+[m[32m- Referrer-Policy[m
[32m+[m[32m- Permissions-Policy[m
[32m+[m
[32m+[m[32mCookie Attributes Checked[m
[32m+[m
[32m+[m[32m- Secure[m
[32m+[m[32m- HttpOnly[m
[32m+[m[32m- SameSite[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32mProject Structure[m
[32m+[m
[32m+[m[32mX1VulnScanner/[m
[32m+[m[32m├── main.py[m
[32m+[m[32m├── scanner.py[m
[32m+[m[32m├── models.py[m
[32m+[m[32m├── checks/[m
[32m+[m[32m│   ├── __init__.py[m
[32m+[m[32m│   ├── headers.py[m
[32m+[m[32m│   └── cookies.py[m
[32m+[m[32m├── reports/[m
[32m+[m[32m│   └── __init__.py[m
[32m+[m[32m├── tests/[m
[32m+[m[32m├── requirements.txt[m
[32m+[m[32m├── .gitignore[m
[32m+[m[32m└── README.md[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32mInstallation[m
[32m+[m
[32m+[m[32mClone the repository:[m
[32m+[m
[32m+[m[32mgit clone https://github.com/X1-starr/X1VulnScanner.git[m
[32m+[m[32mcd X1VulnScanner[m
[32m+[m
[32m+[m[32mInstall the required Python package:[m
[32m+[m
[32m+[m[32mpip install -r requirements.txt[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32mUsage[m
[32m+[m
[32m+[m[32mRun the scanner against a web target:[m
[32m+[m
[32m+[m[32mpython3 main.py https://example.com[m
[32m+[m
[32m+[m[32mThe scanner reports detected findings together with:[m
[32m+[m
[32m+[m[32m- Severity[m
[32m+[m[32m- Confidence[m
[32m+[m[32m- Category[m
[32m+[m[32m- Location[m
[32m+[m[32m- Evidence[m
[32m+[m[32m- Explanation[m
[32m+[m[32m- Impact[m
[32m+[m[32m- Recommendation[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32mExample[m
[32m+[m
[32m+[m[32mX1VulnScanner[m
[32m+[m[32mWeb Security Auditor V2[m
[32m+[m
[32m+[m[32mCreated by X1[m
[32m+[m
[32m+[m[32m[*] X1 Scanner started[m
[32m+[m[32m[*] Target: https://example.com[m
[32m+[m
[32m+[m[32m[+] HTTP Status: 200[m
[32m+[m[32m[+] Final URL: https://example.com/[m
[32m+[m[32m[+] Server: cloudflare[m
[32m+[m
[32m+[m[32m━━━━━━━━━━━━ X1 SECURITY FINDINGS ━━━━━━━━━━━━[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32mSeverity Levels[m
[32m+[m
[32m+[m[32mSeverity| Meaning[m
[32m+[m[32mCRITICAL| Extremely serious security issue[m
[32m+[m[32mHIGH| Significant security issue[m
[32m+[m[32mMEDIUM| Security weakness requiring attention[m
[32m+[m[32mLOW| Lower-impact security issue[m
[32m+[m[32mINFO| Informational observation[m
[32m+[m
[32m+[m[32mSeverity indicates the potential importance of a finding and does not by itself prove exploitability.[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32mImportant Note[m
[32m+[m
[32m+[m[32mX1VulnScanner is intended for authorized security testing, defensive research, and educational use.[m
[32m+[m
[32m+[m[32mOnly scan websites and systems that you own or have explicit permission to test.[m
[32m+[m
[32m+[m[32mThe absence of a finding does not guarantee that a target is secure, and detecting a configuration weakness does not necessarily mean the target is directly exploitable.[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32mRoadmap[m
[32m+[m
[32m+[m[32mFuture versions may include additional non-destructive security checks, improved reporting, testing support, and expanded detection capabilities.[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32mAuthor[m
[32m+[m
[32m+[m[32mX1[m
[32m+[m
[32m+[m[32mCybersecurity learning project.[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32mLicense[m
[32m+[m
[32m+[m[32mThis project is provided for educational and authorized security-testing purposes.[m
