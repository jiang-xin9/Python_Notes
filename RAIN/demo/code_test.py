import json

import requests


def Code():
    a = "'{\"msg\":\"【晓悟】你可以说收藏某作品，比如：\\u201c收藏环球大富翁\\u201d，就不用担心下次找不到啦<br>\'"
    b = "'{\"msg\":\"【晓悟】你可以说收藏某作品，比如：\u201c收藏环球大富翁\u201d，就不用担心下次找不到啦<br>\'"
    # print(a.encode('utf-8').decode("unicode_escape"))
    c = a.encode('unicode_escape').replace(b'\\\\', b'\\').decode("unicode_escape")
    print(a)
    print(b)
    print(c)
    #response.apparent_encoding预测网页当前使用编码
    #在解码的过程中, 可能会遇到字符集以外的未知标识导致解码中断并报错, 添加一个 errors 参数可以避免此问题
    #result = response.content.decode(encoding='GBK', errors="ignore")
    #result = response.content.decode(encoding='GBK', errors="replace")
    #印返回数据的时候会遇到  ‘\深\圳jnbzmel’  类型斜杠加字母的这种其实不是乱码是unicode编码，在传json格式参数的时候将json.dumps()的参数改为ensure_ascii=False，默认位True
    #data_str = json.dumps(data, ensure_ascii=False)

