# 前言
纯粹为了方便copy
# json配置
## json文件
```json
{
	"db_connect": {
		"host": "127.0.0.1",
		"user": "root",
		"password": "123456",
		"port": 3306,
		"database": "mysql"
	}
}
```
## py读取
```python
import json
import os
from selenium import webdriver

class JsonRead:
    def __init__(self, path):
        '''如果是第一次调用，读取Json文件，否则直接返回之前保存的数据'''
        if os.path.exists(path):
            self.path = path
        else:
            raise FileNotFoundError('Json文件不存在')
        self._data = None  # 保存yaml的数据

    def getData(self, keys=None):
        if not self._data: # 如果不是空数据
            with open(self.path, mode='rb') as f:	# 读取文件
                if keys:	# 如果有keys
                    self._data = json.load(f)[keys]
                else:
                    self._data = json.load(f)
        return self._data

Js = JsonRead('config.json')
print(Js.getData("db_connect"))
# {'host': '127.0.0.1', 'user': 'root', 'password': '123456', 'port': 3306, 'database': 'mysql'}
```
## 自动化示例
```json
{
	"url":"https://www.baidu.com"
}
```
```python
import json
import os
from selenium import webdriver



class JsonRead:
    def __init__(self, path):
        '''如果是第一次调用，读取Json文件，否则直接返回之前保存的数据'''
        if os.path.exists(path):
            self.path = path
        else:
            raise FileNotFoundError('Json文件不存在')
        self._data = None  # 保存yaml的数据

    def getData(self, keys=None):
        if not self._data:
            with open(self.path, mode='rb') as f:
                if keys:
                    self._data = json.load(f)[keys]
                else:
                    self._data = json.load(f)
        return self._data

Js = JsonRead('config.json').getData()

fox = webdriver.Firefox()
fox.get(Js['url'])
```
# ini配置
## ini文件
```python
[devicename]
name = emulator-5554
platform = Android
Package = com.mxchip.project352
Activity = com.mxchip.project352.activity.login.LoginActivity
Version = 7.1.2
Reset = True
```
## py文件
```python
import configparser

def INIRead(path, name, values):
    conf = configparser.ConfigParser()
    try:
        conf.read(path, encoding="utf-8")
        case_value = conf.get(name, values)
        return case_value
    except Exception as e:
        print(e)
i = INIRead('config.ini','devicename','name')
print(i)
# emulator-5554
```
## 注意点：
不好的一点就是，ini文件写的读取出来后都是str。
# yaml配置
## yaml文件
```yaml
webUrl:
    testurl: https://www.baidu.com
activity:
  ele:
      loca: kw
      sends: 清安无别事
  loc:
    loca: su
    clicks: click
```
## py文件
```python
import yaml

class YamlRead:
    def __init__(self, yamlPath):
        '''如果是第一次调用，读取yaml文件，否则直接返回之前保存的数据'''
        if os.path.exists(yamlPath):
            self.yamlPath = yamlPath
        else:
            raise FileNotFoundError('yaml文件不存在')
        self._data = None  # 保存yaml的数据

    @property  # 把一个方法变成属性来调用,
    def getData(self):
        if not self._data:
            with open(self.yamlPath, mode='r') as f:
                self._data = yaml.load(f, Loader=yaml.FullLoader)
        return self._data

yl = YamlRead('config.yaml').getData
print(yl)
```
## 自动化示例
```python
import os
import yaml
from selenium import webdriver

class YamlRead:
    def __init__(self, yamlPath):
        '''如果是第一次调用，读取yaml文件，否则直接返回之前保存的数据'''
        if os.path.exists(yamlPath):
            self.yamlPath = yamlPath
        else:
            raise FileNotFoundError('yaml文件不存在')
        self._data = None  # 保存yaml的数据

    @property  # 把一个方法变成属性来调用,
    def getData(self):
        if not self._data:
            with open(self.yamlPath, mode='r') as f:
                self._data = yaml.load(f, Loader=yaml.FullLoader)
        return self._data

yl = YamlRead('config.yaml').getData
print(yl)

fox = webdriver.Firefox()
fox.get(yl['webUrl']['testurl'])
fox.find_element_by_id(yl['activity']['ele']['loca']).send_keys(yl['activity']['ele']['sends'])
```
# PY配置
```python
class Config:
    url = "https://www.baidu.com"
    ele = 'kw'
    loca = '清安无别事'



def config():
    print(Config.url)
    print(Config.ele)
    print(Config.loca)

config()
```
这个先对而言最好理解了，但是用的也比较的少。

