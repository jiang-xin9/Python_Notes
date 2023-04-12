:::success
1、必须是子类
2、子类中实现对父类方法的覆盖
### 多态

- 不同的子类对象调用相同的父类方法，产生不同的执行结果
- 以继承和重写父类方法为前提
- 是调用方法的技巧，不会影响到类的内部设计
:::
```python
class Animal:
    def shout(self):
        return "Animao ~~~"


class Cat(Animal):
    def shout(self):
        print('喵 ~~~')


class Dog(Animal):
    def shout(self):
        print("汪 ~~~~")


def animals(obj):
    obj.shout()


c = Cat()
d = Dog()
for i in (c, d):
    animals(i)
"""
喵 ~~~
汪 ~~~~
"""
```
例二
```python
class qingan():
    def pay(self):
        print('买了包子')


class wangwu():
    def pay(self):
        print('买了饼')


class lisi():
    def pay(self):
        print('买了炒粉')


class zhifubao():
    def maidan(self, obj):
        print('买了什么？')
        obj.pay()


z = qingan()
l = lisi()
w = wangwu()

fukuan = zhifubao()
fukuan.maidan(z)
fukuan.maidan(l)
"""
买了什么？
买了包子
买了什么？
买了炒粉
"""
```
