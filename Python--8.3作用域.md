# 局部作用域
:::info
所谓的局部作用域，可以理解所在一定范围内才生效的东西。看例子：
:::
```python
def number():
    a = 100
    print(a)
number()
```
:::info
此处的a变量，它的作用域仅限于number函数内。如果你想：
:::
```python
def number():
    a = 100
    print(a)
number()
a+=1
```
> 这是不允许的，因为已经超出作用域的范围了。a是在函数内定义了，作用范围只能是在number函数内。但是如果这样：

```python
def number():
    a = 100
    def sum_():
        print(a*10)
    return sum_

print(number())
```
> 函数嵌套函数，也是可以的。
> 注意了，这里的函数调用区别：

```python
def number():
    a = 100
    def sum_():
        print(a*10)
    return sum_

n = number()
n()
print(number())
"""
1000
<function number.<locals>.sum_ at 0x000001B0A68A6C10>
"""
```
> 简单的理解，n指向了number函数的地址，调用后，进入内层函数，n()再次调用，指向sum_函数，最终输出a*10

# 全局作用域
> 全局作用域，即是不论函数处于什么位置，都可以调用到这个全局变量或者其他

```python
a = 100
def number():
    print(a*10)
number()

def sum_():
    print(a+a)
sum_()

class A:
    def b(self):
        print(a-1)

A().b()
"""
1000
200
99
"""
```
> 不论怎么样，全局变量a都是可以在各个函数，类中使用。亦或者局部变量那样，函数嵌套

```python
a = 100
def number():
    def sum_():
        print(a + a)
    return sum_
n = number()
n()
```
> 都是没有问题的

# 小结
此外除去语句全局作用域所介绍的，后续还会介绍一个全局函数global。
