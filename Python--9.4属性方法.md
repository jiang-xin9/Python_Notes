# 前言
```python
class Person:
    sex = '男'  # 类属性

    def __init__(self, name, age=18):
        self.name = name  # 实例属性
        self.age = age

    def run(self):  # 类方法
        return f"{self.name}在跑步唉，他今年{self.age}岁"

    def getsex(self):
        return f"我是{self.sex}生"


per = Person('清安')
print(Person.__class__, type(Person), Person.__class__ is type(Person))
print(Person.__name__)
print(Person.__dict__)  # 类字典，age,__doc__,__init__
# 可以通过Person.的方式进行访问。可以中放的是字符串
print(Person.__init__)
print(per.run())
"""
<class 'type'> <class 'type'> True
Person
{'__module__': '__main__', 'sex': '男', '__init__': <function Person.__init__ at 0x0000024FF573CCA0>, 'run': <function Person.run at 0x0000024FF596B550>, 'getsex': <function Person.getsex at 0x0000024FF596B5E0>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
<function Person.__init__ at 0x0000024FF573CCA0>
清安在跑步唉，他今年18岁
"""
```
# 实例
上面我们看了Person字典，也就是Person.__dict__。那么实例字典呢。
```python
class Person:
    sex = '男'  # 类属性

    def __init__(self, name, age=18):
        self.name = name  # 实例属性
        self.age = age

    def run(self):  # 类方法
        return f"{self.name}在跑步唉，他今年{self.age}岁"

    def getsex(self):
        return f"我是{self.sex}生"


per = Person('清安')
print(Person.__dict__)  # 类字典，age,__doc__,__init__
print(per.__dict__)
"""
{'__module__': '__main__', 'sex': '男', '__init__': <function Person.__init__ at 0x0000015B4AD3C820>, 'run': <function Person.run at 0x0000015B4AD3CCA0>, 'getsex': <function Person.getsex at 0x0000015B4AE6B550>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
{'name': '清安', 'age': 18}
"""
```
# 方法
```python
class Person:

    def func():		# func就是定义的类方法也称属性
        print("我是清安")

Person.func()   # 1、找类属性。2、因为无参，使用类限定名的普通函数调用
Person().func() # 1、func()是类属性，返回的不仅仅是普通函数。
#2、实际上调用，解释器注入第一个参数Person()，fun()没有形参可以注入
```
> 这样写的同时，代码已经报错了，不建议这么写。这里仅仅帮助理解

## classmethod
消耗更少的内存：实例方法也是对象，创建它们需要付出代价。使用静态方法可以避免这种情况。
静态方法的用途有限，因为它们无权访问对象的属性（实例变量）和类属性（类变量）。
```python
class Person:
    @classmethod	# 类方法
    def func(cls):  # 装饰器内部获取到类型信息，并绑定类型
        print("我是清安",cls)   # 注入的是类型

Person.func()
Person().func()

print(Person.func)  # 绑定类
print(Person().func)    # 绑定实例
"""
我是清安 <class '__main__.Person'>
我是清安 <class '__main__.Person'>
<bound method Person.func of <class '__main__.Person'>>
<bound method Person.func of <class '__main__.Person'>>
"""
```
深入了解classmethod用法
```python
class Person:
    num = 0

    def method(self):
        print("实例方法")

    @classmethod
    def func(cls):
        cls.num += 1	# 类方法实例化调用属性
        print("我是清安", cls.num)

Person.func()
"""
我是清安 1
"""
```
> classmethod只可以允许调用类属性，如果是__init__里面的属性，则需要通过其他方法进行调用

### 深入理解
> 我先创建一个配置文件config.py

```python
port = 3306
user = 'localhost'
```
> 另一个类如下：

```python
import config
class Person():
    def __init__(self,port,user):
        self.port = port
        self.user = user
        
Person(config.port,config.user)
```
> 调用Person的时候需要传入参数，这样显的麻烦，有没有调用的时候自动传参的方法！

```python
import config
class Person():
    def __init__(self,port,user):
        self.port = port
        self.user = user
        
    @classmethod
    def sql(c):
		# obj = Person(config.port,config.user)
        obj = c(config.port,config.user)
        return obj

Person.sql()
```
> 如上所示，注释部分如果还是用类来调用，那就太不方便了，如果类名改变，那么sql方法中的类名也需要变。
> 所以我们用了classmethod装饰器，c处只是一个变量，写什么都可以，但是根据命名因该要写cls。这样就能灵活变更了。不论类名怎么变，sql方法(类装饰器)都会实时绑定。

## staticmethod
```python
class Person:
    @staticmethod	# 静态方法
    def func():  # 装饰器内部获取到类型信息，并绑定类型
        print("我是清安")   # 注入的是类型

Person.func()
Person().func()
print(Person.func)
print(Person().func)
print(Person.__dict__)
"""
我是清安
我是清安
<function Person.func at 0x00000265BADBC820>
<function Person.func at 0x00000265BADBC820>
{'__module__': '__main__', 'func': <staticmethod object at 0x00000265BAEDFFD0>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
"""
```
### 注意
```python
class Person:
    def method(self):
        print("实例方法")

    @staticmethod
    def func():  # 装饰器内部获取到类型信息，并绑定类型
        print("我是清安")  # 注入的是类型


Person.func()
Person.method()
```
> Person.method()这样是不被允许的，缺少一个参数
> 正确写法：Person.method(Person())，Person.method([1,2,3])都可以

# 私有属性
```python
class Person:
    __run = '20'

    def __init__(self,sex):
        self.__sex = sex

    def set_name(self, name):
        return f"你就是{name}"

    def __info(self, name, age):
        return f"他是{name}，今年{age}岁了"

    def get_info(self,name, age):
        age += 1
        return f"{self.__info(name, age)},性别{self.__sex},能跑{self.__run}公里"
per = Person('男')
print(per.get_info('清安',18))
print(per.set_name('拾贰'))
"""
他是清安，今年19岁了,性别男,能跑20公里
你就是拾贰
"""
```
> 如上所示，私有的皆以__开头，所以此处就不解释了

> 私有的都不能在类外进行访问，如下，pycharm是没有提示的。如果说这样不够准确(确实不够准确)。你可以print看看提示你什么信息，让你更加的了解私有属性。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25452484/1660988317883-23b9e944-b2ea-4e46-a405-2c71d479dccf.png#clientId=u9aa539e3-db1b-4&from=paste&height=114&id=u434d3066&name=image.png&originHeight=114&originWidth=585&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15499&status=done&style=none&taskId=u4f69db57-8e94-4cef-8eab-eba3632a1d7&title=&width=585)
> 但是可以通过在类里面开辟一个通道的方式对外提供访问，例如上述代码中的get_info，如下：

```python
    def get_info(self,name, age):
        age += 1
        return f"{self.__info(name, age)},性别{self.__sex},能跑{self.__run}公里"
```
## 注意点：
```python
class Person:
    __run = '20'

    def __init__(self,sex):
        self.__sex = sex

    def set_name(self, name):
        return f"你就是{name}"

    def __info(self, name, age):
        return f"他是{name}，今年{age}岁了"

    def get_info(self,name, age):
        age += 1
        return f"{self.__info(name, age)},性别{self.__sex},能跑{self.__run}公里"

per = Person('男')
per.__sex = 'nan'
print(per.__sex)
print(per.__dict__)
print(per.get_info('清安',18))
```
如果我已这样的方式呢？那么__sex输出的是什么？
> nan
> {'_Person__sex': '男', '__sex': 'nan'}
> 他是清安，今年19岁了,性别男,能跑20公里

好了， 到了此处就解密了，为什么私有属性无法直接用per.__info这样的方式进行访问了。
> 私有成员__成员名，会被解释器改名为_当前类: 私有成员，也就是'_Person__sex': '男'。那么这样是不是在上述中直接通过实例化进行访问呢？

```python
class Person:
    __run = '20'

    def __init__(self,sex):
        self.__sex = sex

    def set_name(self, name):
        return f"你就是{name}"

    def __info(self, name, age):
        return f"他是{name}，今年{age}岁了"

    def get_info(self,name, age):
        age += 1
        return f"{self.__info(name, age)},性别{self.__sex},能跑{self.__run}公里"

per = Person('男')
print(per._Person__sex)
"""
男
"""
```
> 没错，它是可以的。

> 而per.__sex = 'nan'在类外定义的，基本上可以说与类中的私有没有关系了。所以可以进行访问。可称之为隐藏。

注意如果要访问私有，要了解它的类属性，可通过限定名(per).__dict__或者限定名.__class__.__dict__的方式查看
# 小结
:::success
静态方法

- 它跟类与对象无关
- 跟在模块中直接定义普通函数没有什么区别，只是把“静态方法”放到了类里面，所以只能设置形参
- 只能通过 类名.静态方法 来调用

类方法

- 类方法内部可以直接访问**类属性、类方法、实例方法**
- cls 可以理解成**类对象的引用**，哪一个类对象调用的方法， cls 就是哪个一个类的**引用**， 类对象.类方法 ；和实例方法中的 self 很像， 实例对象.实例方法 
- 调用其他**类方法**时，**不用**传递cls参数；但调用其他**实例方法**时，**需要**传递cls参数
- 在类方法**内部调用**的实例方法，**接收的是一个类对象而不是实例对象**，当实例对象绑定实例属性时，在实例方法中打印的仍然是**类属性；表明类方法无法访问实例属性**
- **一个类只有一个类对象**，即使通过实例对象调用类方法，传递的仍然是类对象的引用，所有类方法都被同一个类对象调用
:::

