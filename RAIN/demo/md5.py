import hashlib

import requests


class Md5:
    @classmethod
    def test_md5(self):
        uid,name,password,salt='3','qcj','123456','LZ7dYxCj5S68ucAh'
        hl=hashlib.md5()
        hl.update(('{}-{}-{}-{}'.format(uid,name,password,salt)).encode('utf-8'))
        sign=hl.hexdigest()#对hl对象中保存的字段进行md5加密算法
        print(sign)
        data={
            'uid':'3',
            'sign':sign
        }
        resp=requests.post("http://www.fanyunedu.com:5000/general/userinfo_sign",json=data)
        print(resp.text)
        #测试测试测试测试
if __name__ == '__main__':
    Md5.test_md5()