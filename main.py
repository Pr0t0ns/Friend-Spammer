import tls_client, random, threading, json


class FQ:
    def __init__(self) -> None:
        self.proxy = random.choice([prox.strip() for prox in open("proxies.txt")])
        self.session = tls_client.Session(client_identifier="chrome_115", random_tls_extension_order=True)
        self.usr = username
        try:
            self.token = random.choice(tokens)
            tokens.remove(self.token)
            self.token = self.token.split(":")[2]
        except IndexError:
            return
        self.session.proxies = {
            'https': 'http://{}'.format(self.proxy),
            'http': 'http://{}'.format(self.proxy)
        }
    
    def get_cookies(self):
        try:
            self.session.cookies = self.session.get("https://discord.com").cookies
        except:
            print("[X]: Error sending Friend Request")
            return FQ().begin()
        return

    def send_fq(self):
        url = 'https://discord.com/api/v9/users/@me/relationships'
        self.session.headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': self.token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'America/New_York',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIyMDcxNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        }
        try:
            usr, discrim = self.usr.split("#")[0], self.usr.split("#")[1]
        except:
            usr = self.usr
            discrim = None
        payload = {"username": usr,"discriminator":None if discrim is None else discrim}
        self.session.headers['content-length'] = str(len(json.dumps(payload)))
        try:
            res = self.session.post(url, json=payload)

        except:
            print("[X]: Error sending Friend Request")
            return
        if res.status_code == 204:
            print(f"[+]: Sent Friend Request --> ({self.token[:20]}..)")
        else:
            if 'You need to verify your account in order to perform this action' in str(res.text):
                print("[X]: Token Locked")
            elif "captcha-required" in str(res.text):
                print("[$]: Captcha Required")
            else:
                print("[X]: Error sending Friend Request")
        return FQ().begin()

    def begin(self):
        self.get_cookies()
        self.send_fq()
        return FQ().begin()

if __name__ == "__main__":
    tokens = [token.strip() for token in open("tokens.txt")]
    username = input("User to freind (pr0t0na | pr0t0na#0001):  ")
    for i in range(int(input("Threads: "))):
        Fq = FQ()
        threading.Thread(target=Fq.begin).start()
