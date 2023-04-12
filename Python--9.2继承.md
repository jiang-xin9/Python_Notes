# 简单小例子
```python
class People:
    """这是人类"""
    def run(self):
        print(f"{People.__doc__} This man is running, {self.__class__.__name__}")

p = People().run()

class Qingan(People):
    """这是清安"""
    pass

q = Qingan().run()
"""
这是人类 This man is running, People
这是人类 This man is running, Qingan
"""
```
> 可以看到，打印了不同的类名了吧。用的却是同一个类里面的方法。这就是继承。
> People就是父类，Qingan就是子类。这样可以达到复用的一个目的。
> 继承：子类可以继承父类中的属性以及方法

更直观的可以看看这个例子：
```python
class People:
    """这是人类"""
    def __init__(self,name):
        self._name = name

    def run(self):
        print(self.name)
        return f"{self._name} This man is running, {self.__class__.__name__}"

    @property
    def name(self):
        return self._name

p = People('拾贰')
print(p.run())
print(p.name)

class Qingan(People):
    """这是清安"""
    pass

q = Qingan('清安').run()
print(q)
"""
拾贰
拾贰 This man is running, People
拾贰
清安
清安 This man is running, Qingan
"""
```
## 一些其他的小方法
```python
class People:
    """这是人类"""
    def __init__(self,name):
        self._name = name

    def run(self):
        print(self.name)
        return f"{self._name} This man is running, {self.__class__.__name__}"

    @property
    def name(self):
        return self._name

p = People('拾贰')
print(People.__mro__)   # 方法的解析顺序
print(People.mro())

class Qingan(People):
    """这是清安"""
    pass

q = Qingan('清安').run()
print(Qingan.__subclasses__())
print(Qingan.__mro__)
print(Qingan.__base__,Qingan.__bases__)
print(People.__base__,People.__bases__)
"""
(<class '__main__.People'>, <class 'object'>)
[<class '__main__.People'>, <class 'object'>]
清安
[]
(<class '__main__.Qingan'>, <class '__main__.People'>, <class 'object'>)
<class '__main__.People'> (<class '__main__.People'>,)
<class 'object'> (<class 'object'>,)
"""
```
> 主要是用来看继承自哪里，以及先类似的方法之间的不同点。
> ### 什么是 MRO
> - MRO，method resolution order，方法搜索顺序
> - 对于单继承来说，MRO 很简单，从当前类开始，逐个搜索它的父类有没有对应的属性、方法
> - 所以 MRO 更多用在多继承时判断方法、属性的调用路径
> - Python 中针对类提供了一个内置属性 __mro__ 可以查看方法搜索顺序

# 继承实例
```python
class People:
    """这是人类"""
    __height = 178

    def __init__(self, name, age):
        self.__name = name
        self.age = age


    def run(self):
        return f"{self.__name} This man is running, {self.__class__.__name__}"


    @classmethod
    def info(cls):
        return "height:{} {}".format(cls.__height,cls.__dict__)

    @classmethod
    def __info1(cls):
        return f"cls:{cls},dict:{cls.__dict__},height:{cls.__height}"

    def info2(self):
        return self.__height

class Men(People):
    """这里是Men类"""
    __height = 180


wo = Men('清安',12)
print(wo.run())
print(wo._People__name)
print(wo._People__info1())
print(wo.info())
print(wo.info2())
"""
清安 This man is running, Men
清安
cls:<class '__main__.Men'>,dict:{'__module__': '__main__', '__doc__': '这里是Men类', '_Men__height': 180},height:178
height:178 {'__module__': '__main__', '__doc__': '这里是Men类', '_Men__height': 180}
178
"""
```
> 上述中，使用了类方法，主要是用于更好的区别/学习继承

可以看到一般情况下，子类继承父类是没有任何问题的。即使是使用子类进行实例化，去调用父类中的方法都是可以的。
```python
print(dir(wo))
print(Men.__mro__)
"""
['_Men__height', '_People__height', '_People__info1', '_People__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'info', 'info2', 'run']
(<class '__main__.Men'>, <class '__main__.People'>, <class 'object'>)
"""
```
在上述的例子中沿用下去。在这两个里面都可以看到，Men子类继承父类后，可以使用父类中的哪些方法。在mro中可以看到，还有个<class 'object'>。这是父类默认继承自object类。python自带的。每一个类都会默认继承。
> 继承父类后，私有类是不能够直接继承的。也是需要通过某些手段拿到。例如上述中
> print(wo._People__name)
> print(wo._People__info1())

# 覆盖
```python
class Animal:
    def shout(self):
        return "Animao ~~~"
        
class Cat(Animal):
    def shout(self):
        print("~~~")
        print(super())  # 解决类与实例对象的传递问题
        print(super(__class__, self))
        print(super(Cat, self).shout())
        print('喵 ~~~')

c = Cat().shout()
print("~"*30)
a = Animal().shout()
print(Animal.__dict__)
print(Cat.__dict__)
"""
~~~
<super: <class 'Cat'>, <Cat object>>
<super: <class 'Cat'>, <Cat object>>
Animao ~~~
喵 ~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{'__module__': '__main__', 'shout': <function Animal.shout at 0x000001A9EEDDC820>, '__dict__': <attribute '__dict__' of 'Animal' objects>, '__weakref__': <attribute '__weakref__' of 'Animal' objects>, '__doc__': None}
{'__module__': '__main__', 'shout': <function Cat.shout at 0x000001A9EEDDCCA0>, '__doc__': None}
"""
```
> 上述代码中我们可以看到super(Cat, self).shout()，返回的结果其实是父类中的值，这说明我们可以通过super方法进行实例化调用父类中的方法。
> 如果抱有疑问，大可以自己试试用子类方法中直接调用父类的方法。
> ## 什么是 super
> - 在 Python 中，super 是一个特殊的类
> - super() 就是使用 super 类创建出来的对象
> - 实际应用的场景：子类在重写父类方法时，调用父类方法

## 小例子
```python
class A:
    @classmethod
    def clsmtd(cls):
        print(f"A classmethod")

    @staticmethod
    def stmtd():
        print(f"A classmethod")

class B(A):
    @classmethod
    def clsmtd(cls):
        super().clsmtd()
        print(f"B classmethod")

    @staticmethod
    def stmtd():
        A.stmtd()
        print(f"B classmethod")

b = B()
b.clsmtd()
b.stmtd()
"""
A classmethod
B classmethod
A classmethod
B classmethod
"""
```
> 静态方法staticmethod写法不一样，无法用super进行调用。只能写死用A类。
> 此处的例子覆盖+调用

# 小例子--覆盖
```python
class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, b, c):
        self.b = b
        self.c = c

    def values(self):
        print(self.b)
        print(self.c)
        print(self.a)


b = B(200, 300)
b.values()
"""
200
300
AttributeError: 'B' object has no attribute 'a'
"""
```
> 这里会告诉你B中没有属性a。B中没有创建a的属性，则会找A类也没有a属性，则会找object类，object类中更加没有了，所以会报错。
> 可以在A类中创建一个类属性得以解决，或者如下方式：

```python
class A:
	# a = 100
    def __init__(self, a,):
        self.a = a


class B(A):
    def __init__(self, b, c):
		# super(B,self) 基类中会把self传递给父类，所以此处不需要写self
        super().__init__(100)
        self.b = b
        self.c = c

    def values(self):
        print(self.b)
        print(self.c)
        print(self.a)

b = B(200, 300)
b.values()
```
# 深入理解
```python
class A:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age


class B(A):
    def __init__(self, name, age=20):
        super().__init__(name, age)# 重载父类方法
        self.name = name
        self.age = age


b = B('清安')
print(b.age)
print(b.__dict__)
```
> 如果不进行重载也是可以的，python会给出你友好的提示，__init__出会给出不同颜色的背景提示。

```python
class A:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age


class B(A):
    def __init__(self, name, age=20):
        super().__init__(name, age)# 重载父类方法
        self.age = age + 10


b = B('清安')
print(b.age)
print(b.__dict__)
```
> 此处子类重载父类，将子类age覆盖掉父类中的age，将值传递过去后，父类则是age=20。重载完成后，回到子类，age=20+10所以age输出30

```python
class A:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age


class B(A):
    def __init__(self, name, age=20):
        # super().__init__(name, age)# 重载父类方法
        self.age = age + 10
        super().__init__(name, age)  # 重载父类方法


b = B('清安')
print(b.age)
print(b.__dict__)
```
> 这个情况则是相反，先覆盖，覆盖物父类中的age=20，随后age=20+10，然后再进行子类重载父类__init__方法，又成了age=20。

# 小结
```python
class A:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age


class B(A):
    def __init__(self, name, age=20):
        super().__init__(name, age)  # 重载父类方法
        self.name = '拾贰'
        self.age = age + 10


b = B('清安')
print(b.name, b.age)
print(b.__dict__)
```
:::success
在有__init__时，可以理解为把父类搬到了子类中，或者把父类中的实例属性搬到了子类中来使用。通过super()来帮助你完成，同时又符合继承。super()起到一个关联作用。关联父类后，可以使用父类中的方法/属性。
就好比print(super(Cat, self).shout())第一个例子中的方法。super会将Cat类与self实例(当前实例)绑定到这个这个超级对象中。从而调用父类中的方法。--这是其中一种方式方法
:::

