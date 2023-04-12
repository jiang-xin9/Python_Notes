# 列表推导式
## 例一
```python
list_ = [58,59,60,61,89,100,20,30]
print([i for i in sorted(list_,reverse=False)])
"""[20, 30, 58, 59, 60, 61, 89, 100]"""
# 等价于
for i in sorted(list_,reverse=False):
    list1.append(i)
print(list1)
```
## 例二
```python
list_ = [58,59,60,61,89,100,20,30]
print([i for i in sorted(list_,reverse=False) if i>60])
# 等价于
for i in sorted(list_,reverse=False):
    if i >60:
        list1.append(i)
print(list1)
"""[61, 89, 100]"""
```
## 例三
```python
list_ = [58,59,60,61,89,100,20,30]
list_1 = []
list_2 = []
print([list_1.append(i) if i>60 else list_2.append(i) for i in sorted(list_,reverse=False)])
print(list_1,list_2)
"""
[None, None, None, None, None, None, None, None]
[61, 89, 100] [20, 30, 58, 59, 60]
"""
# 等价于
for i in sorted(list_,reverse=False):
    if i > 60:
        list_1.append(i)
    else:
        list_2.append(i)
print(list_1,list_2)
```
## 例四
```python
list_ = [[1,2,3],[4,5,6],[7,8,9]]
list_1 = []
print([[row[i] for row in list_] for i in range(3)])

# 等价于
for i in range(3):
    list_row = []
    for row in list_:
        list_row.append(row[i])
    list_1.append(list_row)
print(list_1)

"""
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""
```
# 字典推导式
## 例一
```python
li = [11,22,33,44,55,66,77,88,99,90]
num = {"k1":[],"k2":[]}

res = {num["k1"].append(i) if i>60 else num["k2"].append(i) for i in li}
print(res)

# 等价于
for i in li:
    if i > 66:
        num["k1"].append(i)
    else:
        num["k2"].append(i)
print(num)
"""
{'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55, 66]}
"""
```
## 例二
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
# 等价于
res = {i['name']:i['score'] for i in students if i['score']<=60}
print(res)

"""
{'明明': 40, 'Tom': 59}
"""
```
## 例三
```python
a = {"name":"清安","age":18,"sex":"男"}
b = {"name":"拾贰","age":18,"sex":"男","home":"深圳"}
res = {k: v for d in [a, b] for k, v in d.items()}
print(res )

# 等价于
res = {}
for i in [a,b]:
	for k,v in i.items():
         res[k] = v
print(res)

"""{'name': '拾贰', 'age': 18, 'sex': '男', 'home': '深圳'}"""
```
## 例四
```python
b = {"name":"拾贰","age":18,"sex":"男","home":"深圳"}
print({(keys,values) for keys,values in b.items()})
```
# 集合推导式
```python
set_ = set(range(5))
print({x**2 for x in set_})
"""{0, 1, 4, 9, 16}"""
```
# 三元运算符
```python
a = 1
b = 2
print(a if a > b else b)
```
## 进阶用法
```python
def number(a, b):
    # 如果a>b, re1=a, 否则, re1=b
    re1 = a if a > b else b  
    # 如果条件成立, re2=True对应的值a, 反之, re2 =False对应的值
    re2 = {True: a, False: b}[a > b]  
    # (不成立的值, 成立的值)[条件]
    re3 = (b, a)[a > b]  
 
    return re1, re2, re3
 
print(number(10, 20))
```
# 关于内置函数的三元表达式
## filter
```python
def is_odd(value):
    if value[1] >= 18:
        return value[1]
    # return True if value[1] >= 18 else False
     
newlist = filter(is_odd, [("清安",18),("拾贰",20),("QA",17)])
print(list(newlist))
```
