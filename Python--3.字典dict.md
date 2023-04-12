# 前言
有问题可以加V：qing_an_an，最后有习题赠送！
如果看不懂如下例子，那么请移步到：
![1657106540296.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/25452484/1657106560610-b661c077-57c2-4333-a04b-be57b5a51b06.jpeg#averageHue=%23a0a0a0&clientId=u4d0176ef-f829-4&from=paste&height=152&id=dUjOd&name=1657106540296.jpg&originHeight=152&originWidth=151&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20432&status=done&style=none&taskId=u42fce756-3cdf-4ee3-b17d-8df6e784146&title=&width=151)
注意代码详解部分出自于源码，这里都只是增加了例子，帮助理解如何运用。
# 思维导图
![](https://cdn.nlark.com/yuque/0/2022/jpeg/25452484/1658805522905-225ee8bd-7493-4d16-9c8f-8c951506cdfa.jpeg)
# 基础部分
## 创建字典
```python
dict_ = {}
dict_1 = {"name":"清安"}
dict_2 = dict([("name","清安")])
dict_3 = dict({"name":"清安"})
dict_4 = {"name":"清安","age":[18,19,20]}
print(dict_)
print(dict_1)
print(dict_2)
print(dict_3)
print(dict_4)
"""
{}	空字典
{'name': '清安'}	普通字典
{'name': '清安'}	序列转字典
{'name': '清安'}	使用字典，这个有点废话
{'name': '清安', 'age': [18, 19, 20]}		混合字典
"""
```
## 获取字典的值
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
print(dict_["name"])	# 第一种取值方式
print(dict_["age"][0])	# 第二种取值方式
"""
清安
18
"""
```
## 修改字典的值
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
dict_["age"] = 20
"""
{'name': '清安', 'age': 20, 'home': '深圳钱深圳花，一分别想带回家'}
"""
```
## 添加键值对
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
dict_["sex"] = 18
print(dict_)
"""
{'name': '清安', 'age': [18, 19, 20], 'home': '深圳钱深圳花，一分别想带回家', 'sex': 18}
"""
```
# 代码详解
## clear清除
 从字典中删除所有项目。  
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
print(dict_.clear())
print(dict_)
"""
None
{}
"""
```
## copy复制
 返回字典的浅表副本。  
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
dict_copy = dict_.copy()	# 复制
print(id(dict_))
print(id(dict_copy))
dict_copy["age"] = 20	# 修改值
print(dict_copy)
print(dict_)
"""
2157763270976
2157763271168
{'name': '清安', 'age': 20, 'home': '深圳钱深圳花，一分别想带回家'}
{'name': '清安', 'age': [18, 19, 20], 'home': '深圳钱深圳花，一分别想带回家'}
"""
```
## fromkeys创建新字典
 创建一个新字典，其中键来自iterable，值设置为value。
```python
list_ = ["清安"]
print(dict.fromkeys("username"))
print(dict.fromkeys("username",list_))
"""
{'u': None, 's': None, 'e': None, 'r': None, 'n': None, 'a': None, 'm': None}
{'u': ['清安'], 's': ['清安'], 'e': ['清安'], 'r': ['清安'], 'n': ['清安'], 'a': ['清安'], 'm': ['清安']}
"""
"""--------------------------------------------------------------------------"""
list_ = ["清安"]
list_2 = [11,22,11,33,44]
print(dict.fromkeys(list_2,list_))
"""{11: ['清安'], 22: ['清安'], 33: ['清安'], 44: ['清安']}"""
```
## get获取值
 返回键的值。 如果key不存在，则返回d（默认为None）。  
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
print(dict_.get("name"))
print(dict_.get("sex"))
"""
清安
None
"""
```
## items遍历键, 值
 返回可遍历的(键, 值) 元组数组。  
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
res = dict_.items()
print(res)
for i in res:
    print(i)
"""
dict_items([('name', '清安'), ('age', [18, 19, 20]), ('home', '深圳钱深圳花，一分别想带回家')])
('name', '清安')
('age', [18, 19, 20])
('home', '深圳钱深圳花，一分别想带回家')
"""
for i in dict_.items():
    print(i)		# 上述的写法可以写成这样
	
"""也可以写成这样，直接打印出键值更明了"""
for keys,values in dict_.items():
    print(f"keys:{keys}",f"values:{values}")
"""
keys:name values:清安
keys:age values:[18, 19, 20]
keys:home values:深圳钱深圳花，一分别想带回家
"""
```
## keys返回键
 返回字典中的所有的键。
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
for keys in dict_:
    print(keys)
"""
name
age
home
"""
for keys in dict_.keys():
    print(keys)		# 这样的写法也是ok的	
```
## pop删除
删除指定的键并返回相应的值。如果未找到键，则返回默认值（如果给定），否则会引发KeyError
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
print(dict_.pop('name'))
print(dict_.pop('sex',"未找到键")	# 此处给定默认值
"""
清安
未找到键
"""
```
## popitem删除任意项
 删除并返回任意项（键，值）。如果字典为空则引发KeyError  
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
print(dict_.popitem())
print(dict_.popitem())
print(dict_.popitem())
print(dict_.popitem())
"""
('home', '深圳钱深圳花，一分别想带回家')
('age', [18, 19, 20])
('name', '清安')
KeyError: 'popitem(): dictionary is empty'
"""
```
## setdefault返回指定键
 返回指定键的值，如果指定键的值不在字典中，返回指定值，默认为 None。  
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
print(dict_.setdefault("name"))
print(dict_.setdefault("sex","键不在这"))
"""
清安
键不在这
"""
```
## update更新
 使用来自other的键/值对更新字典，覆盖现有键。  
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
dict_.update({"name":"拾贰","sex":"男"})
print(dict_)
dict_.update(name = "拾贰",age = 18)
print(dict_)
dict_.update([("name","拾贰"),("age",20)])
print(dict_)

"""
{'name': '拾贰', 'age': [18, 19, 20], 'home': '深圳钱深圳花，一分别想带回家', 'sex': '男'}
{'name': '拾贰', 'age': 18, 'home': '深圳钱深圳花，一分别想带回家', 'sex': '男'}
{'name': '拾贰', 'age': 20, 'home': '深圳钱深圳花，一分别想带回家', 'sex': '男'}
"""
```
## values返回所有值
 以列表形式返回字典中的所有值。  
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
for values in dict_.values():
    print(values)
"""
清安
[18, 19, 20]
深圳钱深圳花，一分别想带回家
"""
```
# 拓展
## get的另一种用法
```
dict_ = {"name":"清安"}
print(dict_.get('age',[]))
"""
[]
"""
```
意思是在获取不到值的时候返回一个空列表
## zip创建字典
```python
list_ = ["name","sex","age"]
list_2 = ["拾贰","男",18]
print(dict(zip(list_,list_2)))
"""
{'name': '拾贰', 'sex': '男', 'age': 18
"""
```
## del删除键值对
```python
dict_ = {"name":"清安","age":[18,19,20],"home":"深圳钱深圳花，一分别想带回家"}
del dict_["age"]
print(dict_)
"""
{'name': '清安', 'home': '深圳钱深圳花，一分别想带回家'}
"""
```
## 去重值
```python
dict_ = {"name":1,"name1":2,"name3":3,"name4":2}
for values in set(dict_.values()):
    print(values)
"""
1
2
3
	"""
```
## |合并字典
```python
dict_1 = {"name":"清安","age":18,"sex":"男"}
dict_2 = {"name":"拾贰","age":18,"sex":"男","home":"深圳"}
res  = (dict_1 | dict_2)
print(res)
"""
{'name': '拾贰', 'age': 18, 'sex': '男', 'home': '深圳'}
"""
```
### 解析式合并
```python
a = {"name":"清安","age":18,"sex":"男"}
b = {"name":"拾贰","age":18,"sex":"男","home":"深圳"}
res = {k: v for d in [a, b] for k, v in d.items()}
print(res )
"""
等同于下面的写法
# res = {}
# for i in [a,b]:
#     for k,v in i.items():
#         res[k] = v
# print(res)
"""
```
# 例题
## 例题一
统计重复出现的元素次数，并将元素以及出现的次数输出出来，重复元素打印一次
```python
a = [33,44,22,33,44,88,99,55,66,66,55]
dic = {}
for i in a:
    dic[i] = a.count(i)
print(dic)
"""
{33: 2, 44: 2, 22: 1, 88: 1, 99: 1, 55: 2, 66: 2}
"""
```
## 例题二
以字典形式，打印出成绩不合格的学生姓名以及成绩
```python
students = [
{'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
'15300022838'},
{'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
'15300022428'},
{'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
'15300022839'},
{'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
'15300022839'}
]

lis = {}
for i in students:
    if i['score'] <= 60:
        lis[i['name']] = i['score']
print(lis)

res = {i['name']:i['score'] for i in students if i['score']<=60}
print(res)
```
## 例题三
 有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
即： {‘k1’: 大于66的所有值列表, ‘k2’: 小于66的所有值列表}  
```python
li = [11,22,33,44,55,66,77,88,99,90]
li1 = []
num = {"k1":[],"k2":[]}
for i in li:
    if i > 66:
        num["k1"].append(i)
    else:
        num["k2"].append(i)
print(num)

res = {num["k1"].append(i) if i>60 else num["k2"].append(i) for i in li}
print(num)
```
## 例题四
发散题
```python
money = {"蔡狗": {"一整只":200,"腰子":0,"手脚":"白送"},"露猪":"200元"}

while True:
    for keys,values in money.items():
        print(f'商品如下：{keys}')
    n = input("请输入你要了解的商品：")
    if isinstance(n,str):
        if n in money:
            print(money[n])
            n1 = input("请问还需要了解什么：")
            if n1 == "一整只" or "腰子" or "手脚":
                print(money[n][n1])
            else:
                print("请重新选择")
        else:
                print("没有这个商品")
    if n == 'q' or 'Q':
        exit("退出成功")
```
