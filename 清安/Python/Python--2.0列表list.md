# 前言
有问题可以加V：qing_an_an，最后有习题赠送！
如果看不懂如下例子，那么请移步到：
![1657106540296.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/25452484/1657106560610-b661c077-57c2-4333-a04b-be57b5a51b06.jpeg#clientId=u4d0176ef-f829-4&from=paste&height=152&id=dUjOd&name=1657106540296.jpg&originHeight=152&originWidth=151&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20432&status=done&style=none&taskId=u42fce756-3cdf-4ee3-b17d-8df6e784146&title=&width=151)
注意代码详解部分出自于源码，这里都只是增加了例子，帮助理解如何运用。
# 思维导图
![](https://cdn.nlark.com/yuque/0/2022/jpeg/25452484/1658805415450-e3dc232c-6d25-4e5f-b5e0-6c95ddaf4e88.jpeg)
# 基础部分
## 创建列表的几种方式
```python
list1 = [1,True,False]
print(list1)
list2 = list("abc")
print(list2)
list3 = list((1,2,3))
print(list3)
list4 = list(range(0,5))
print(list4)
list5 = [i for i in range(0,5)]
print(list5)

"""
[1, True, False]
['a', 'b', 'c']
[1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
"""
```
## 切片\取值
```python
list_ = ['清','安','安','静','了']
print(list_[0:2])
print(list_[-1:])
print(list_[::-1])
print(list_[0:6:2])
print(list_[-4:-1])
print(list_[-1:-4:-1])
"""
['清', '安']
['了']
['了', '静', '安', '安', '清']
['清', '安', '了']
['安', '安', '静']
['了', '静', '安']
"""
print(list_[-1:-4])
# 这个取出的是个空列表，索引取值本身即是自左向右，自小向大。
# 自右向左的取值再不指定反向的情况下，取不到值
# 反向就是print(list_[-1:-4:-1])
```
## 修改值
```python
list_ = ['清','安','安','静','了']
list_[0] = '拾贰'
print(list_)
"""
['拾贰', '安', '安', '静', '了']
"""
```
## 列表长度
```python
list_ = ['清','安','安','静','了']
print(len(list_))

# 5
```
## 转换
```python
print(list(range(0,6)))
a = '123456'
print(list(a))

"""
[0, 1, 2, 3, 4, 5]
['1', '2', '3', '4', '5', '6']
"""
```
## 统计
```python
a = [1,2,3,4,5,6]
print(max(list(a)))
print(min(list(a)))
print(sum(list(a)))
"""
6
1
21
"""
```
# 代码详解
## append添加
将对象追加到列表末尾
```python
list_ = ['欢','迎','来','到','清','安']
list_.append('小课堂')
print(list_)
list_1 = ['欢','迎','来','到','清','安']
list_1.append(['小','课','堂'])
print(list_1)
"""
['欢', '迎', '来', '到', '清', '安', '小课堂']
['欢', '迎', '来', '到', '清', '安', ['小', '课', '堂']]
	"""
```
注意print(list_.append([60]))，这是不可取的一种方式。具体情况见下面代码，如果还存疑惑，且看Python源码小经验部分。
```python
list_ = ['欢','迎','来','到','清','安']
list_.append('小课堂')
print(id(list_),type(list_))
print(id(list_.append(60)),type(list_.append(60)))
print(list_.append(60))
"""
2115122819456 <class 'list'>
140731478846680 <class 'NoneType'>
None
"""

a = list_.append('一拳80')
print(type(a))
"""
<class 'NoneType'>
"""
```
## extend添加/附加
通过附加iterable中的元素来扩展列表。_iterable_可以是序列、支持迭代的容器或迭代器对象。
```python
list_ = ['清','安']
list_.extend('一拳80')
print(list_)
list_.extend(['一拳','80'])
print(list_)
"""
['清', '安', '一', '拳', '8', '0']
['清', '安', '一拳', '80']
"""
```
## clear清除/删除
从列表中删除所有项目
```python
list_ = ['清','安']
list_.clear()
print(list_)
"""
[]
"""
```
## copy复制
返回列表的浅副本
```python
list_ = ['清','安']
a = list_.copy()
a[0] = 1
print(id(list))
print(list_)
print(id(a))
print(a)
"""
140731110529776
['清', '安']
2369222766720
[1, '安']
"""
# 二
list_ = ['清','安']
list_[0] = 1
a = list_.copy()
print(id(list))
print(list_)
print(id(a))
print(a)
"""
140731110529776
[1, '安']
2935660442496
[1, '安']
"""
# 三
list_ = ['清','安']
a = list_.copy()
list_[0] = 1
print(id(list))
print(list_)
print(id(a))
print(a)
"""
140731110529776
[1, '安']
2851386651584
['清', '安']
"""
```
注意区别，以及顺序，这里的copy浅拷贝，注意二三的拷贝以及修改值的顺序。先拷贝后修改，那么拷贝的变量对应的值不随之改变，反之，一起变。
## count统计
返回值的出现次数
```python
list_ = ['清','安','安','静','了']
print(list_.count('安'))
"""
2
"""
```
## index索引
返回值的第一个索引,如果值不存在，则引发ValueError
```python
list_ = ['清','安','安','静','了']
print(list_.index('安'))
"""
1
"""
```
## insert插入
在索引之前插入对象
```python
list_ = ['清','安','安','静','了']
list_.insert(2,'，')
print(list_)
"""
['清', '安', '，', '安', '静', '了']
"""
```
## pop删除/弹出
删除并返回索引处的项目（默认为最后一个）。如果列表为空或索引超出范围，则引发索引器错误。
```python
list_ = ['清','安','安','静','了']
print(list_.pop(2))
print(list_)
"""
安
['清', '安', '静', '了']
"""
print(list_.pop(6))
"""
IndexError: pop index out of range
"""
```
## remove删除
删除第一个出现的值。如果值不存在，则引发ValueError。
```python
list_ = ['清','安','安','静','了']
list_.remove('安')
print(list_)
"""
['清', '安', '静', '了']
"""
```
## reverse反转
反转*到位*
```python
list_ = ['清','安','安','静','了']
list_.reverse()
print(list_)
"""
['了', '静', '安', '安', '清']
"""
```
## sort排序
按升序对列表排序，并返回None。
```python
list_ = ['清','安','安','静','了']
list_.sort(reverse=True)
print(list_)
list_.sort(reverse=False)
print(list_)
"""
list_.sort()默认是list_.sort(reverse=False)

['清','安','安','静','了']
['了', '安', '安', '清', '静']
"""

```
## 补充
### del删除
```python
list1 = [i for i in range(0,5)]
del list1[0]
print(list1)

"""[1, 2, 3, 4]"""
```
### sorted排序
跟sort类似，sort操作原列表，sorted会建议新列表
```python
list1 = [4,3,5,6,2,1]
print(sorted(list1,reverse=False))
print(sorted(list1,reverse=True))
"""
[1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1]
"""
```
# 列表解析式
```python
# 1、一般形式
list1 = [i**2 for i in range(1,5)]
print(list1)
# 2、if解析式
list2 = [j for j in list1 if j > 4]
print(list2)
# 3、if else解析式
list3 = [f"{k}偶数" if k%2==0 else f"{k}奇数" for k in list1]
print(list3)

"""
[1, 4, 9, 16]
[9, 16]
['1奇数', '4偶数', '9奇数', '16偶数']
"""
# 3的拆分式：
for k in list1:
    if k%2==0:
        print("偶数")
    else:
        print("奇数")
```
# 拓展
```python
list1 = [1,2]
list2 = ["1","2"]
print(list1+list2)
print(list1*2)
"""
[1, 2, '1', '2']
[1, 2, 1, 2]
+号将一个列表添加到另一个列表，先当与列表拼接
*号可以为一个列表扩展为原来的N倍，先当与复制列表内的元素
列表内不同类型的元素只能用+号，不能用*
"""
```
# 例题
## 例题一
 已知一个数字列表，输出所有奇数的下标
```python
sum = [59, 54, 89, 45, 78, 43, 12, 96, 79, 47, 69]
for i in sum:
    if i %2!= 0:
        print("奇数下标值为：",sum.index(i))
"""
奇数下标值为： 0
奇数下标值为： 2
奇数下标值为： 3
奇数下标值为： 5
奇数下标值为： 8
奇数下标值为： 9
奇数下标值为： 10
"""
```
## 例题二
将所有元素成2
```python
list_ = [1,2,3,4,5]
print([i*2 for i in list_])
```
## 例题三
 找出以’A’或者’a’开头，并以’c’结尾的所有元素，并添加到一个新列表中,
```python
lis = ['libai','dufu','aasc','Asac','asjdw']
new = []
for i in lis:
    i.strip()
    if (i.startswith("a") or i.startswith("A") )and i.endswith("c"):
        new.append(i)
print(new)
```
