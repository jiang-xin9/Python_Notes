> 序列化：把内存中的数据类型转换成一种特定格式，这种特定格式可以用于存储或者传输给其他平台

内存中的数据类型-----》序列化---》特定格式(json/pickle)
内存中的数据类型《-----反序列化<----特定格式(json/pickle)

用途：
    1、存储
    2、跨平台数据交互

# json
```python
import json

dic = {"name":'拾贰','age':18,'hobby':['篮球'],'Python':True}
json_dic = json.dumps(dic)
print(json_dic)
"""
{"name": "\u62fe\u8d30", "age": 18, "hobby": ["\u7bee\u7403"], "Python": true}
"""
```
可以看到这里汉字是unicode编码的，看如下：
```python
import json

dic = {"name":'拾贰','age':18,'hobby':['篮球'],'Python':True}
json_dic = json.dumps(dic,ensure_ascii=False)
print(json_dic,type(json_dic))
"""
{"name": "拾贰", "age": 18, "hobby": ["篮球"], "Python": true} <class 'str'>
"""
```
> 注意看符号，由单引号，变成了双引号。类型与就是字符串形式的。
> json只是数据格式。规定了True或者False要用小写的形式，以及""形式

## 序列化/反序列化第一种
```python
import json

dic = {"name":'拾贰','age':18,'hobby':['篮球'],'Python':True}
json_dic = json.dumps(dic)
with open('json_.json',mode='wt',encoding='utf-8') as j:
    json_write = j.write(json_dic)


# 反序列化
with open('json_.json',mode='rt') as r:
    json_read = json.loads(r.read())
    print(json_read)
```
> 这里对比上面，我将ensure_ascii=False去掉了，再反序列化后，这要与不要都可以。只是写入文本后展示的不一样，不要ensure_ascii=False，写入json就是unicode编码的。

:::danger
反序列化用的loads方法， 别搞混了
:::
## 序列化/反序列化第二种
```python
import json

dic = {"name":'拾贰','age':18,'hobby':['篮球'],'Python':True}
with open('json_1.json',mode='wt',encoding='utf-8') as j:
    json.dump(dic,j)    # 一步到位，自动调用dumps然后调用j完成序列化

with open('json_.json',mode='rt') as r:
    print(json.load(r))
```
:::danger
ensure_ascii=False依旧可以添加到序列化中去，只是我没有添加。
第二种方法，先对于第一种，代码上简化了一些
:::
## 反序列化第三种
```python
with open('json_.json',mode='rb') as r:
    # print(json.load(r))
    print(json.loads(r.read()))
```
:::danger
这里的mode是二进制的，需要注意一下
:::
值得注意的是，python的集合，是不被允许序列化的。、
```python
set_ = {1,2,3}
json.dumps(set_)
"""
TypeError: Object of type set is not JSON serializable
"""
```
# pickle
常用于存档
## 第一种
```python
import pickle

dic = {"name":'拾贰','age':18,'hobby':['篮球'],'Python':True,"set":{1,2,3}}
pickle_dic = pickle.dumps(dic,protocol=0)
with open('pickle_.pickle',mode='wb') as w:
    w.write(pickle_dic)
	
with open('pickle_.pickle',mode='rb') as r:
    read_pickle = pickle.loads(r.read())
    print(read_pickle)
```
:::danger
值得注意的是，这里我添加了集合进来。需要用二进制写入。
protocol=0，保证写入后不出现乱码的情况
注意文件的后缀名是pickle
:::
## 第二种
```python
import pickle

dic = {"name":'拾贰','age':18,'hobby':['篮球'],'Python':True,"set":{1,2,3}}

with open('pickle_.pickle',mode='wb') as r:
    pickle.dump(dic,r,protocol=0)
	
with open('pickle_.pickle',mode='rb') as r:
    read_pickle = pickle.load(r)
    print(read_pickle)
```
与json的及其相似
