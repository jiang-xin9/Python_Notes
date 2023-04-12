# 前言
有问题可以加V：qing_an_an，最后有习题赠送！
如果看不懂如下例子，那么请移步到：
![1657106540296.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/25452484/1657106560610-b661c077-57c2-4333-a04b-be57b5a51b06.jpeg#clientId=u4d0176ef-f829-4&from=paste&height=152&id=dUjOd&name=1657106540296.jpg&originHeight=152&originWidth=151&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20432&status=done&style=none&taskId=u42fce756-3cdf-4ee3-b17d-8df6e784146&title=&width=151)
注意代码详解部分出自于源码，这里都只是增加了例子，帮助理解如何运用。
> 此处思维导图略过。本章内容不多。

# 基础部分
## 创建元组
```python
a = (1,2,3)
print(a)
b = tuple((1,2,3))
print(b)
c = tuple(range(5))
print(c)
d = tuple(i for i in range(0,5))
print(d)
"""
(1, 2, 3)
(1, 2, 3)
(0, 1, 2, 3, 4)
(0, 1, 2, 3, 4)
"""
```
# 切片/取值
```python
tuple_ = ('I','am','QingAn','or','ShiEr')
print(tuple_[0],tuple_[1],tuple_[2])
print(tuple_[0:3])
print(tuple_[-3:])
print(tuple_[0:6:2])
print(tuple_[::-1])
"""
I am QingAn
('I', 'am', 'QingAn')
('QingAn', 'or', 'ShiEr')
('I', 'QingAn', 'ShiEr')
('ShiEr', 'or', 'QingAn', 'am', 'I')
"""
```
# 长度len
```python
tuple_ = ('I','am','QingAn','or','ShiEr')
print(len(tuple_))
"""
5
"""
```
# 转换
```python
tuple_1 = ['I','am','QingAn','or','ShiEr']
print(tuple(tuple_1))
"""
('I', 'am', 'QingAn', 'or', 'ShiEr')
"""
```
# 统计
```python
tuple_sum = (10,20,30,40,50)
print(min(tuple_sum))
print(max(tuple_sum))
print(sum(tuple_sum))
"""
10
50
150
"""
```
# 修改值
> 元组，本质上式不允许修改的，但是我们可以通过一些其他的手段进行修改

```python
tuple_ = ['I','am','QingAn','or','ShiEr']
tuple_1 = tuple_
tuple_1[0] = "My"
print(tuple_1)
print(id(tuple_),id(tuple_1))
"""
['My', 'am', 'QingAn', 'or', 'ShiEr']
2805877116160 2805877116160
"""
```
# 代码详解
## count
统计元素出现的次数
```python
tuple_ = ('I','am','QingAn','or','ShiEr')
print(tuple_.count('am'))
"""1"""
```
## index
返回一个值的索引，如果没有这个值则抛出异常
```python
tuple_ = ('I','am','QingAn','or','ShiEr')
print(tuple_.count('am'))
"""1"""
```
# 拓展
```python
tuple_ = ('I','am')
tuple_1 = ('QingAn','or','ShiEr')
print(tuple_+tuple_1)
"""
('I','am','QingAn','or','ShiEr')
"""
```
```python
tuple_ = ('I','am')
tuple_1 = ('QingAn','or','ShiEr')
tuple_2 = (1,2,3)
print(tuple_+tuple_2)
print(tuple_*2)
"""
('I', 'am', 1, 2, 3)
('I', 'am', 'I', 'am')
"""
```
## 遍历
```python
tuple_ = ('I','am','QingAn','or','ShiEr')
for i in tuple_:
    print(i)
"""
I
am
QingAn
or
ShiEr
"""
```
## 删除元组
> del删除后再次打印则会报错

```python
tuple_ = ('I','am','QingAn','or','ShiEr')
del tuple_
print(tuple_)
"""
NameError: name 'tuple_' is not defined

"""
```
# 推导式/解析式
```python
print(range(5))
print(tuple(range(5)))
print((i for i in range(0,5)))
print(tuple(j for j in range(0,5)))
"""
range(0, 5)
(0, 1, 2, 3, 4)
<generator object <genexpr> at 0x000001BC4ACF9B30>
(0, 1, 2, 3, 4)
"""
```
```python
j = (i for i in range(0,5))
print(type(j),j)
print(next(j),j.__next__())
for i in j:
    print(i)
"""
<class 'generator'> <generator object <genexpr> at 0x0000023D6402CBA0>
0 1
2
3
4
"""
```
> 可以看到，上述中的print((i for i in range(0,5)))，得出的是一个生成器，我们可以通过for循环的方式进行迭代输出。也可以通过print(tuple(j for j in range(0,5)))这样的方式得出。因为源码中提供， __iter__方法。可直接进行迭代。

# 小结
不用怀疑代码详解部分为什么这么少，因为源码只提供了这两种方法。剩下的皆是魔术方法。至于什么式魔术方法，建议将Python大全看完。
