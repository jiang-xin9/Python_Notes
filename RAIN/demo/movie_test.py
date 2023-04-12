import requests


class video:
    url = "https://www.wangci.net/dongman/qyqx/"
    def get_url(self):
        headers = {
            "referer": "https://www.wangci.net/dongman /",  # 防盗链
            "user - agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            #"P3P": "CP=CAO PSA OUR"  # 解决跨域问题
            "authority":"www.wangci.net",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "cookie": "PHPSESSID=ufgcqq5ac4enld5fbq1e3t9m06; Hm_lvt_b03ff183d08088cd060bd95d7ccd0740=1680975557; Hm_lpvt_b03ff183d08088cd060bd95d7ccd0740=1680975557",
            "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests":"1",
            "alt-svc":'":443"; ma=86400',
            "method":"GET",
            "path": "/dongman/qyqx/"
        }
        response1 = requests.get(self.url, headers=headers)  # 请求网页
        response1.encoding = 'utf-8'
        print(response1.text)
if __name__ == '__main__':
    vi=video()
    vi.get_url()