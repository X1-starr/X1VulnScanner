import requests

from models import ScanResult
from checks.headers import check_headers
from checks.cookies import check_cookies

class X1Scanner:
    def __init__(self, target):
        self.target = target.rstrip("/")
        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": "X1VulnScanner/2.0"
        })

        self.result = ScanResult(target=self.target)

    def fetch(self):
        try:
            response = self.session.get(
                self.target,
                timeout=10,
                allow_redirects=True
            )

            return response

        except requests.RequestException as error:
            print(f"[!] Connection error: {error}")
            return None

    def run(self):
        print("[*] X1 Scanner started")
        print(f"[*] Target: {self.target}\n")

        response = self.fetch()

        if response is None:
            return self.result

        check_headers(response, self.result)
        check_cookies(response, self.result)

        print(f"[+] HTTP Status: {response.status_code}")
        print(f"[+] Final URL: {response.url}")
        print(f"[+] Server: {response.headers.get('Server', 'Unknown')}")

        return self.result
