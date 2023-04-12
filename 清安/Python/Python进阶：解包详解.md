# 各数据结构解包小例子
## 列表解包
```python
a,b,c = [1,2,3]
print(a,b,c)    # 1 2 3
```
## 元组解包
```python
a,b,c = (1,2,3)
print(a,b,c)    # 1,2,3
```
## 字符串解包
```python
a,b,c = "123"
print(a,b,c)    # 1,2,3
```
## 集合解包
```python
a,b,c = {1,2,3}
print(a,b,c)    # 1,2,3
```
## 字典解包
```python
a,b,c = {"a":1,"b":2,"c":3}
print(a,b,c)    # a,b,c
```
## 生成器解包
```python
a,b,c = (x+1 for x in range(3))
print(a,b,c)	# 1，2，3
```
## 多元素解包
```python
a, b, *c = [1, 2, 3, 4, 5]
print(a, b, c)  # 1 2 [3, 4, 5]

a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)  # 1 [2, 3, 4] 5
```
:::success

- 在某个变量面前加一个星号
- 而且这个星号可以放在任意变量
- 每个变量都分配一个元素后，剩下的元素都分配给这个带星号的变量
:::
# 函数解包
```python
def num(a, b, c):
    print(a, b, c)

num(1, 2, 3)
num(*[4, 5, 6])
num(*(7, 8, 9))
num(*{11, 22, 33})
num(**{"a": 111, "b": 222, "c": 333})
"""
1 2 3
4 5 6
7 8 9
33 11 22
111 222 333
"""
```
## 多类型参数解包
```python
def num(a, b, c):
    print(a, b, c)


num(*[4], *(5,), **{"c": 6})
"""
4 5 6
"""
```
## 函数元组解包
```python
def name(*args):
    print(args)
    print(*args)

name('清安','拾贰')
"""
('清安', '拾贰')
清安 拾贰
"""
```
## 函数字典解包
```python
def name(**kwargs):
    print(kwargs)
    print(*kwargs)


name(name1='清安', name2='拾贰')
"""
{'name1': '清安', 'name2': '拾贰'}
name1 name2
"""
```
### 扩充
```python
def name(**kwargs):
    print(kwargs)
    print(kwargs["name1"])


name(**{"name1":'清安',"name2":"拾贰"})
"""
{'name1': '清安', 'name2': '拾贰'}
清安
"""
```
# 表达式解包
```python
print(range(3),3)
print(*range(5),5)
print([*range(5)])
print(*[range(5)])
print(*{"a": 111, "b": 222, "c": 333})
print(**{"a": 111, "b": 222, "c": 333})
"""
range(0, 3) 3
0 1 2 3 4 5
[0, 1, 2, 3, 4]
range(0, 5)
a b c
TypeError: 'a' is an invalid keyword argument for print()
"""
```
# 解包拼接
## 列表
```python
list_ = [1,2]
list_1 = range(3,5)
list_2 = [*list_,*list_1]
print(list_2)
"""
[1, 2, 3, 4]
"""
```
## 字典
```python
dict1 = {"a": 111, "b": 222, "c": 333}
dict2 = {"d": 444, "e": 555, "f": 666}
dict3 = {**dict1,**dict2}
print(dict3)
"""
{'a': 111, 'b': 222, 'c': 333, 'd': 444, 'e': 555, 'f': 666}
"""
```
# 小结

- 自动解包支持一切可迭代对象
- 函数调用时，可以用 * 或者 ** 解包可迭代对象
