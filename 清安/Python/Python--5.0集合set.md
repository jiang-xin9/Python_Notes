# 前言
有问题可以加V：qing_an_an，最后有习题赠送！
如果看不懂如下例子，那么请移步到：
![1657106540296.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/25452484/1657106560610-b661c077-57c2-4333-a04b-be57b5a51b06.jpeg#clientId=u4d0176ef-f829-4&from=paste&height=152&id=dUjOd&name=1657106540296.jpg&originHeight=152&originWidth=151&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20432&status=done&style=none&taskId=u42fce756-3cdf-4ee3-b17d-8df6e784146&title=&width=151)
注意代码详解部分出自于源码，这里都只是增加了例子，帮助理解如何运用。
# 基础部分
## 创建集合
```python
a = {1,2,3}
print(type(a),a)
b = set(range(5))
print(type(b),b)
c = [1,2,3]
print(set(c))
print({i for i in range(5)})
"""
<class 'set'> {1, 2, 3}
<class 'set'> {0, 1, 2, 3, 4}
{1, 2, 3}
{0, 1, 2, 3, 4}
"""
```
## 去重
> 去重是集合惯用的手法，其内部的逻辑是更具hash来判断的，只有hash值一直时才会去重。在魔术方法中 有介绍

```python
set_ = {1,1,2,2,3,3,4,5,6}
print(set_)
list_ = [1,1,2,2,3,3,4,4,5,6]
set_1 = set(list_)
print(set_1)
"""
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
"""
```
## 取值
> 集合并不能像字符串元组列表那样下标取值

```python
set_ = {1,"a",True,2.1}
print(set_[0])
"""TypeError: 'set' object is not subscriptable"""
```
> 这里会告诉你集合不可下标取值。那么如果需要取值，因该怎么样呢。可以使用转换，将集合转换成列表或者其他的数据结构。当然，你也可以迭代取值，不限于for循环以及while循环等。

## 长度
```python
set_ = {1,"a",True,2.1}
print(len(set_))
"""3"""
```
> 长度为3，因为True是布尔值

## 转换
```python
set_ = {1,"a",True,2.1}
print(list(set_))
print(tuple(set_))
"""
[1, 2.1, 'a']
(1, 2.1, 'a')
"""
```
## 统计
```python
set_ = {1,2,3,4,5}
print(min(set_))
print(max(set_))
print(sum(set_))
"""
1
5
15
"""
```
# 代码详解
## add添加
```python
set_ = {1,2,3,4,5}
set_.add(6)
print(set_)
"""
{1, 2, 3, 4, 5, 6}
"""
```
> 不可添加列表数据结构的元素。

## clear清除
```python
set_ = {1,2,3,4,5}
set_.clear()
print(set_)
"""
set()
"""
```
## copy拷贝
```python
set_ = {1,2,3,4,5}
set_1 = set_.copy()
set_1.add(7)
print(id(set_),id(set_1))
print("set_:",set_,"set_1",set_1)
"""
1809520936768 1809523530880
set_: {1, 2, 3, 4, 5} set_1 {1, 2, 3, 4, 5, 7}
"""
```
> 这也就是浅拷贝

## difference差集
> 返回两个或多个集合的差值作为新集合

```python
set_ = {1,2,3,4,5}
set_1 = {4,5,6,7,8}
print(set_.difference(set_1))
print(set_1.difference(set_))
"""
{1, 2, 3}
{8, 6, 7}
"""
```
## difference_updat差集删除
> 从这个集合中删除另一个集合的所有元素

```python
set_ = {1,2,3,4,5}
set_1 = {4,5,6,7,8}
# set_.difference_update(set_1)
# print(set_)
set_1.difference_update(set_)
print(set_1)
"""
{6, 7, 8}
"""
```
## discard移除
> 从集合中移除一个元素，如果它是成员。如果元素不是成员，则不执行任何操作。

```python
set_ = {1,2,3,4,5}
set_.discard(1)
set_.discard(0)
print(set_)
"""
{2, 3, 4, 5}
"""
```
## intersection 交集
> 返回两个集合的交集作为新集合

```python
set_ = {1,2,3,4,5}
set_1 = {4,5,6,7,8}
res = set_.intersection(set_1)
print(res)
"""
{4, 5}
"""
```
## intersection_update更新交集
> 更新一个集合与另一个集合的交集

```python
set_ = {1,2,3,4,5}
set_1 = {4,5,6,7,8}
set_.intersection_update(set_1)
print(set_)
set_1.intersection_update(set_)
print(set_1)
"""
{4, 5}
{4, 5}
"""
```
## isdisjoint判断空交集
> 如果两个集合有空交集，则返回True。

```python
set_ = {1,2,3,4,5}
set_1 = {4,5,6,7,8}
set_2 = {9}
print(set_.isdisjoint(set_2))
print(set_.isdisjoint(set_1))
"""
True
False
"""
```
## issubset判断包含
> 另一个集合是否包含此集合。这个是那set_1判断是否被set_包含

```python
set_ = {1,2,3,4,5}
set_1 = {1,2,3}
set_2 = {1,2,3,4,5}
print(set_1.issubset(set_))
print(set_.issubset(set_1))
"""
True
False
"""
```
## issuperset
> 这个集合是否包含另一个集合

```python
set_ = {1,2,3,4,5}
set_1 = {1,2,3}
set_2 = {1,2,3,4,5}
print(set_.issuperset(set_2))
print(set_.issuperset(set_1))
"""
True
True
"""
```
## pop删除
> 删除并返回一个任意的集合元素。如果集合为空则引发KeyError异常。

```python
set_ = {1,2,3,4,5}
print(set_.pop())
"""
1
"""
```
## remove删除
> 从集合中移除一个元素;它必须是一个成员。如果元素不是成员，则引发KeyError。

```python
set_ = {1,2,3,4,5}
set_.remove(1)
print(set_)
"""
{2, 3, 4, 5}
"""
```
## symmetric_difference对称差
> 返回两个集合的对称差作为一个新集合

```python
set_ = {1,2,3,4,5}
set_1 = {4,5,6,7,8}
print(set_.symmetric_difference(set_1))
"""
{1, 2, 3, 6, 7, 8}
"""
```
## symmetric_difference_update
> 用一个集合本身和另一个集合的对称差来更新它

```python
set_ = {1, 2, 3, 4, 5}
set_1 = {4, 5, 6, 7, 8}
set_.symmetric_difference_update(set_1)
print(set_)
# set_1.symmetric_difference_update(set_)
# print(set_1)
"""
{1, 2, 3, 6, 7, 8}
"""
```
## union并集
> 返回集的并集作为一个新集

```python
set_ = {1, 2, 3, 4, 5}
set_1 = {4, 5, 6, 7, 8}
print(set_1.union(set_))
"""
{1, 2, 3, 4, 5, 6, 7, 8}
"""
```
## update更新
> 用集合本身和其他的并集更新集合

```python
set_ = {1, 2, 3, 4, 5}
set_1 = {4, 5, 6, 7, 8}
set_1.update(set_)
print(set_1)
"""
{1, 2, 3, 4, 5, 6, 7, 8}
"""
```
# 推导式/解析式
```python
print({i for i in range(5)})
print(set(range(5)))
"""
{0, 1, 2, 3, 4}
{0, 1, 2, 3, 4}
"""
```
# 小结
集合多用于去重，其他的用的少。
