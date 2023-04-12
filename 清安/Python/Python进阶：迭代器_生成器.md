# 迭代器
重复取值的工具。必须要与上一次有一定关联
```python
num = 0
while True:
    print(num)
    num+=1
```
## 可迭代对象
`只要内置有__iter__()方法的就可以称之为可迭代对象。`
可以转换为迭代器的对象，就称之为可迭代对象。
```python
a = [1,2,3]
a.__iter__()

b = (1,2,3)
b.__iter__()

c = {'a':1,"b":2}
c.__iter__()

d = '123'
d.__iter__()

with open('111.yaml','r') as f:
    f.__iter__()
```
## 迭代器
```python
c = {'a':1,"b":2}
res = c.__iter__()
print(res)
"""<dict_keyiterator object at 0x0000027997DC3C20>"""
```
注意iterator，迭代器对象
```python
c = {'a':1,"b":2}
res = c.__iter__()
"""
只要是迭代器对象都会内置一个__next__方法
调用一次打印一次
"""
print(res.__next__())
print(res.__next__())
print(res.__next__())
"""
迭代器很节省内存资源
当没有可以__next__的时候就会抛出StopIteration异常
"""
```
## for循环原理
小总结
迭代器对象：内置有__next__()方法，并且还内置__iter__()方法的对象
迭代器对象调用__next__()方法，就会得到迭代器的下一个值
迭代器对象调用__iter__()方法，得到迭代器本身(和没调用一样)
```python
c = {'a':1,"b":2}
res = c.__iter__()
print(res.__iter__() is res)
```
```python
for i in 可迭代对象.__iter__()
for i in 迭代器对象.__iter__()
```
```python
c = {'a':1,"b":2}
for key in c:
    print(key)
	
"""
1、调用对象的__iter__()方法，得到一个迭代器对象
2、调用迭代器的__next__()方法，拿到一个返回值
3、循环执行第二步，知道抛出异常，就捕获异常，并结束循环
"""
```
for循环可以称之为迭代循环
不能说可迭代对象是迭代器对象，可以说迭代器对象也是可迭代对象。
```python
with open('111.yaml','r') as f:
    f.__iter__()
	f.__next__()
```
# 生成器
## yield
```python
def func():
    print("第一次执行") 
    yield 1
    print("第一次执行")
    yield 2
    print("第一次执行")
    yield 3
    print("第一次执行")
    
res = func()
print(res)
"""<generator object func at 0x000001A8142DA7B0>"""
```
generator生成器就是迭代器，自定义的迭代器
```python
def func():
    print("第一次执行")
    yield 1
    print("第一次执行")
    yield 2
    print("第一次执行")
    yield 3
    print("第一次执行")

res = func()
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
"""
第一次执行
1
第一次执行
2
第一次执行
3
第一次执行
StopIteration错误
"""
```
调用函数则会有一个生成器。当超出yield关键字后，就会抛出StopIteration错误，跟迭代器一致。
yield关键字存在这里，调用一次执行一次，不调用的时候就会停在此处，调用的时候使用__next__()方法，执行完print后会将yield后面的值进行返回。yield后面可以不跟任何东西，那么调用的时候返回的就是none。
## yield表达式
```python
def func(a= 1):
    print(f"我执行了{a}次")
    a += 1
    while True:
        x = yield
        print(f"我执行了第{a}次,并且{x}")

res = func()
# res.send(10)    # TypeError: can't send non-None value to a just-started generator
res.send(None)  # 相当于next(g)，触发函数代码的运行
res.send(10)
```
# 拓展
```python
def func():
    print("第一次执行")
    yield 1
    print("第一次执行")
    yield 2
    print("第一次执行")
    yield 3
    print("第一次执行")

res = func()
print(res.__iter__())
print(iter(res))
print(res.__next__())
print(res.__next__())
print(next(res))
print(next(res))
```
上述二者本质上是一样的，不论调用iter()还是next()，执行的时候都会调用到__iter__()或__next__()方法。
## 示例
```python
from selenium import webdriver

def func():
    while True:
        driver =  webdriver.Firefox()
        yield driver

driver = func()
res = next(driver)
res.get('https://www.baidu.com')
```
