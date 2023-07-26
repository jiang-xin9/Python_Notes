import csv
import os
import re
import time
import requests
from chatgpt.util import Util


class CHAT:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def __init__(self):
        pass


    def get_textresponse(self,title="打开天选之子",new_session=True):

        header={
            "Conent-Type":"application/json;charset=UTF-8",
            "Authorization": "Bearer d8741989-2cd6-44f1-9be3-e4b85d13c267",#测试
            #"Authorization": "Bearer d83028b6-8826-4b44-b6ea-36fdbf174e6e",#手表版
            #"Authorization": "Bearer b5506c19-5775-4481-b474-299e28e098f7",#手机版
            "User-Agent": "CentAssist/1.1.9 (iPhone; iOS 12.4.8; Scale/3.00)",
            "App-Channel-Id": "oppochildwatch-watch-sdk-test"#测试
            #"App-Channel-Id":"xtcv1-watch-sdk-test",#手表版
            #"App-Channel-Id": "xiaomiad-phone-mobileapp-test",#手机版
        }
        data={
            "msg":title,
            "new_session":new_session
        }
        response = requests.post("https://sdk-test.centaurstech.com/api/sdk/chat", headers=header,json=data)
        #print(response.json())
        time.sleep(1)
        response.encoding="utf-8"
        result = response.text.encode('utf-8').decode('unicode-escape').encode('raw_unicode_escape').decode()  # 将 Unicode 转换为中文字符
        result=result.encode('unicode-escape').replace(b'\\\\', b'\\').decode('unicode-escape')
        print(result)
        pattern = r'<br>|☛.*?☚'
        result = result.replace("\n", "").replace(r'"', "")
        res = re.search(r"msg:(.*?),", result)
        if res:
            result = res[0].replace("msg:", "").replace(",", "")
            result_text = re.sub(pattern, '', result)
            #print(result_text)
            return result_text
        else:
            return "未提取到msg"


    def text_jump(self,path,name):
        util = Util(path)
        text1, text2, text3, text4, zipped = util.open_text()
        first_value=self.get_textresponse(title="打开{}".format(name),new_session=True)
        print(first_value)
        nowtime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        with open(self.BASE_DIR + "/reports_final/" + nowtime + text1[0] + ".csv", encoding='utf-8', mode='w',newline='') as file:
            writer = csv.writer(file)
            report_header = ["剧情点序号", "剧情点内容", "提问序号", "ask", "msg", "预期回复","预期跳转序号", "预期跳转", "结果"]
            writer.writerow(report_header)
            for m in text2:
                number1 = re.search("\d+", m[3:6])
                if number1:
                    number1 = number1.group(0)
                    for k in zipped:
                        number2 = re.search("\d+", k[1][3:6])
                        number2_1 = re.search("\d+", k[1][5:8])
                        number2_2 = re.search("\d+-\d+-\d+", k[1][1:7])
                        if number2 and number2_1:
                            number2 = number2.group(0)
                            number2_1 = number2_1.group(0)
                            number2_2 = number2_2.group(0)
                            if number1 == number2:
                                ask_list = k[1].split("|")
                                for ask in ask_list:
                                    index = re.search("\d+-\d+", m[1:6])
                                    if index:
                                        p = self.get_textresponse(title="☛打开剧情点{}☚".format(index[0]), new_session=False)
                                        print("第{}个剧情点:".format(index[0]), p)
                                    ask = re.sub(r"\[.*?]", "", ask)
                                    msg = self.get_textresponse(title=ask, new_session=False)
                                    print("输入语：{}".format(ask), "接口给出的回复：{}".format(msg))
                                    time.sleep(3)
                                    expect = re.sub(r"\{.*?}|（.*?）| ", "", k[0])  # 回复包含文本提取的预期结果
                                    print("预期结果：{}".format(expect))
                                    index_jump = re.search("\d+-\d+", k[0][-6:-1])  # 提取预期结果中的需要跳转的序号
                                    if index_jump:
                                        print("预期跳转序号："+index_jump[0])
                                        for d in text2:
                                            number3 = re.search("\d+-\d+", d[1:6])  # 提取主剧情点的序号
                                            if number3:
                                                if index_jump[0] == number3[0]:
                                                    expect_jump = re.sub(r"\{.*?}", "", d)  # 得到预期 需要跳转到的剧情点
                                                    print("预期跳转结果：{}".format(expect_jump))
                                                    if msg.__contains__(expect[0:15]) and msg.__contains__(expect_jump[0:15]):
                                                        result = "T"
                                                        print(result)
                                                    else:
                                                        result = "F"
                                                        print(result)
                                                    writer.writerow([str(index[0]+"剧情"),m,str(number2_2+"剧情"),ask,msg,expect,str(index_jump[0]+"剧情"),expect_jump,result])
                                            # else:
                                            #     writer.writerow([str(index[0]), m, str(number2_2), ask, msg, expect,"未找到跳转序号", "未找到跳转剧情", "F"])
if __name__ == '__main__':
    #CHAT().text_jump("/report/2023_05_19_16_43_51天选之子","天选之子")
    CHAT().get_textresponse("继续",new_session=False)