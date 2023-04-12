import os
import re
import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Picture:
    url="https://www.doutuwang.com/"
    #driver = webdriver.Chrome()
    def picture(self):
        headers = {
            "sec-ch-ua":'.Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103',
            "sec-ch-ua-mobile":"?0",
            "sec - ch - ua - platform":"Windows",
            "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 103.0.0.0Safari / 537.36"
        }
        response = requests.get(self.url, headers=headers) # 请求网页
        # response.encoding='GBK'
        response.encoding='utf-8'
        path = os.getcwd()  # 获取当前路径
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取项目根目录
        #self.driver.find_element(By.XPATH, "//*[@id='s1']").click()
        # with open(BASE_DIR+'/data/picturename',encoding='utf-8') as f:
        #     byt=f.readlines()
        #     print(byt)
        print(response.request.headers)
        print(response.status_code)
        t='<img src="(.*?)" width="142" height="95" alt="(.*?)"'
        result=re.findall(t,response.text)
        print(result[1])
        print(len(result))
        #print(response.text)
        print(BASE_DIR)
        print(path)
        for img in result:
            if img==result[0]:
                continue
            res = requests.get(img[0], headers=headers)
            print(res.status_code)
            s = img[0].split(('.'))[-1]
            with open(BASE_DIR+'/data/picture'+'/' + img[1] + '.' + s, mode='wb') as file:
                file.write(res.content)



if __name__ == '__main__':
    pc=Picture()
    pc.picture()




