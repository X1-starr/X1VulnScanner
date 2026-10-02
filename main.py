import sys

from scanner import X1Scanner


BANNER = r"""
╔════════════════════════════════════════════╗
║              X1VulnScanner                 ║
║        Web Security Auditor V2             ║
║                                            ║
║              Created by X1                 ║
╚════════════════════════════════════════════╝
"""


def main():
    print(BANNER)

    if len(sys.argv) != 2:
        print("Usage:")
        print("  python3 main.py https://example.com")
        return

    target = sys.argv[1]

    scanner = X1Scanner(target)
    result = scanner.run()

    print("\n━━━━━━━━━━━━ X1 SECURITY FINDINGS ━━━━━━━━━━━━")

    if not result.findings:
        print("[+] No findings detected.")
    else:
        for i, finding in enumerate(result.findings, 1):
            print(f"""
┌─ FINDING #{i} ─────────────────────────────
│ Severity   : {finding.severity}
│ Confidence : {finding.confidence}
│ Category   : {finding.category}
│
│ Problem:
│ {finding.title}
│
│ Location:
│ {finding.location}
│
│ Evidence:
│ {finding.evidence}
│ Explanation:
│ {finding.explanation}
     
│ Impact:
│ {finding.impact}
│
│ Recommendation:
│ {finding.recommendation}
└────────────────────────────────────────────
""")

    print(f"[*] Total Findings: {len(result.findings)}")


if __name__ == "__main__":
    main()
