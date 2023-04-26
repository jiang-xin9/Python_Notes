> lambda函数又称匿名函数。仅限于单个表达式，可以用在常规功能的任何地方。

# 一个简单的匿名函数
```python
x = 2
lam = lambda x: x * x
print(lam)
```
> 常规操作，这样写得出的结果是：
> <function <lambda> at 0x0000018DE511F040>
> 告诉你，这是一个lambda函数方法。所以，因该这样写：

```python
lam = lambda x: x * x
print(lam(2))
# 4
```
> 需要对其进行调用才行。

## 多看一个例子
```python
sum = lambda x,y : x+y
print(sum(1,2))
```
> lambda的书写格式至此不在叙述

# 结合map()函数
```python
nums = [1,2,3,4,5]
lam = map(lambda x: x * x,nums)
for i in lam:
    print(i)
"""
1
4
9
16
25
"""
```
> map函数，又称映射。此处的例子，将nums列表值迭代出来，并赋值给x，也可以称之为映射给x。从而进行运算乘方的值。
> 又会问，为什么不直接输出lam，你可以试试，打印lam，会告诉你是map函数。所以需要得到lambda运算后的值，需要迭代取值。不论用for还是next，都可以。while也成。

## 多看个例子
```python
nums = [1, 2, 3, 4, 5, 6]
lam = list(map(lambda x: x +1 ,nums))
print(lam)
# [2, 3, 4, 5, 6, 7]
```
> 即使不用for循环，直接转为list输出也是可以的。
> list源码中可以传入参数，也可以不传入，不传入则是一个新的列表，传入则必须是可迭代的。
> map是一个类，也可以称之为可迭代对象，内置__next__方法，所以list()同时，其实可以理解为将nums列表中的元素先迭代出来并完成+1操作，然后添加进list中。

# lambda与fitler()函数
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list(filter(lambda x: x % 2, nums)))
# [1, 3, 5, 7, 9, 11]
```
> 上述例子达到了一个过滤的效果，当然有的人会认为用for循环%2，list转一下一样可以得出基数列表，确实是这样。不过这样的写法是否更加的简洁一点呢？
> 如果还是看不懂，那么：

```python
def func(nums):
    return nums % 2
temps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
value = filter(func,temps)
print(list(value))
```
# if-else
> 在三元表达式一章节，讲过if-else，那么lambda中的if-else是什么样子的？

```python
def func(x):
    if x > 1:
        print("X大")
    else:
        print("x小")
func(1)
```
```python
func = lambda x:'X大' if x > 1 else "x小"
print(func(1))
```
# sorted()
```python
list_ = [-1, 0, 6, 9, 3, -2, 1]
# 普通函数使用
print(sorted(list_,reverse=False))
# lambda函数使用
func = sorted(list_, key=lambda x: x)
print(func)
```
> 此处不做多的叙述，不懂sorted可以去看看列表章节。

