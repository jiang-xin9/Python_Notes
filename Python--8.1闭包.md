# 示例
> 是一种概念，指的是内层函数引用到了外层函数的自由变量

```python
def num():
    c = [0]
    def inc():
        c[0] += 1
        return c[0]
    return inc	# return inc()
n = num()   # 产生了2个局部变量c和inc
print(n(),n())
c = 100
print(n())
```
> return inc跟return inc(),inc是把函数返回了，inc()是把函数的返回值返回了

:::warning
inc会指向引用地址。num()函数执行完，局部变量inc和c标识符都消亡了，但是inc跟c指向的对象并没有消亡
外层函数以及执行结束了，内存函数对象没有消亡，内层函数用到外层函数自由变量c。当n指向的函数对象要使用num的c，c指向的列表不消亡，由这个不消亡的内存函数对象来保存这个列表，这就是闭包
:::
# nonlocal
```python
def number():
    a =100
    def sum_():
        nonlocal a
        a += 1
        return a
    return sum_
n = number()
print(n())
```
Python3中比较简单、容易实现闭包方式的就是nonlocal关键字。
:::warning
定义：
nonlocal 关键字用于在嵌套函数内部使用变量，其中变量不应属于内部函数。
请使用关键字 nonlocal 声明变量不是本地变量。
:::
