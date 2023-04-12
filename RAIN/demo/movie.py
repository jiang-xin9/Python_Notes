import os
import re
import requests


class Movie:
    url="https://www.wangci.net/dongman/qyqx/"
    def movie(self):
        headers={
            "referer": "https: // www.wangci.net / dongman /",  #防盗链
            "user - agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62",
            "P3P": "CP=CAO PSA OUR"#解决跨域问题
        }
        response1 = requests.get(self.url, headers=headers)  # 请求网页
        response1.encoding = 'utf-8'
        t1='<li><a title="(.*?)" href="(.*?)" target="_blank">'
        result1 = re.findall(t1, response1.text)
        for mv in result1:
            mv=list(mv)
            res=re.search(r"[0-9][0-9]|[0-9]",mv[0])
            if res:
                mv[0]=res.group(0)
            elif "在线播放" in mv[0]:
                mv[0]=mv[0][:-4]
            response2= requests.get("https://www.wangci.net"+mv[1], headers=headers)
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取项目根目录
            m3u8 = []
            with open(BASE_DIR+"/data/movie/qyqx.m3u8", 'r') as file:
                lst = file.readlines()
                for i in lst:
                    i = i.strip()
                    if i.startswith('#'):
                        continue
                    else:
                        m3u8.append(i)
            with open(BASE_DIR+"/data/movie/qyqx.mp4", mode='ab') as f:
                for i in range(len(m3u8)):
                    videoContent = requests.get(m3u8[i], headers=headers).content
                    f.write(videoContent)
                    print(i)

            # t2='<iframe class="zanpiancms-play-iframe" src="(.*?)" allowfullscreen="true"'
            # print(response2.text)
            # result2=re.findall(t2, response2.text)
            # print(result2)






if __name__ == '__main__':
    mv=Movie()
    mv.movie()
