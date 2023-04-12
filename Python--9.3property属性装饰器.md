# 访问
首先定义一个类叫做Person，名字随意
```python
class Person:
    def __init__(self, name, age=18):
        self._name = name
        self.__age = age
```
想要反问私有成员变量，除了一些迫不得已的方法(Python是不建议)。所以我们需要通过定义一个方法进行访问。
```python
class Person:
    def __init__(self, name, age=18):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age
	
per = Person('拾贰')
print(per.get_age())  # 可以访问到__age
```
> 此处只是拿私有属性进行举例，不局限于私有属性

# 修改
访问是做到了，那么修改呢。私有变量一般是不会暴露出来的。所以需要修改或者写入值得时候怎么办？
:::danger
装饰器@property，可以称之为语法糖
:::
怎么写？
```python
class Person:
    def __init__(self, name, age=18):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age

    @property
    def age(self):
        # return self.__age + 300
        return self.__age
	
per = Person('拾贰')
print(per.get_age())  # 可以访问到__age
print(per.get_age)
print("我是语法糖age：",per.age)
"""
18
<bound method Person.get_age of <__main__.Person object at 0x000001866850DFD0>>
我是语法糖age： 18
"""
```
:::danger
加了语法糖我们可以通过per.age的方式进行访问
不加语法糖我们可以看到per.get_age，打印的其实是方法在类中对象地址
:::
如何修改值？
```python
class Person:
    def __init__(self, name, age=18):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age

    @property
    def age(self):
        # return self.__age + 300
        return self.__age

    """
    必须先有peoperty语法糖，且后续用的时候必须是 方法名.内建函数 的方法
    """
    @age.setter
    def age(self, value):    # 设置属性的方法成为setter，写入__age的值
        self.__age = value
		
per = Person('拾贰')
print(per.get_age())  # 可以访问到__age
print(per.get_age)
print("我是语法糖age：",per.age)
per.age = 30     # 给私有属性赋值
print(per.age)
"""
18
<bound method Person.get_age of <__main__.Person object at 0x000001866850DFD0>>
我是语法糖age： 18
30
"""
```
:::danger
上述已经说的很明白了，想要修改私有属性，最好是通过 @property装饰器进行，且修改的函数方法名必须保持一致。使用@property的方法名当作下一个方法的装饰器再配合setter进行使用。
:::
> 上文中注释了这个步骤return self.__age + 300，在@property作用下我们可以进行运算(即使不在也可以)

# 删除
最后介绍一下删除
```python
class Person:
    def __init__(self, name, age=18):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age

    @property
    def age(self):
        # return self.__age + 300
        return self.__age

    """
    必须先有peoperty语法糖，且后续用的时候必须是 方法名.内建函数 的方法
    """
    @age.setter
    def age(self, value):    # 设置属性的方法成为setter，写入__age的值
        self.__age = value

    @age.deleter     # 删除
    def age(self):
        print("del ~~~~")
        # del  per.__age	# 一般情况是要删除值的，这里展示调用了这个值
per = Person('拾贰')
print(per.get_age())  # 可以访问到__age
print(per.get_age)
print("我是语法糖age：",per.age)
per.age = 30     # 给私有属性赋值
del per.age
print(per.age)
"""
18
<bound method Person.get_age of <__main__.Person object at 0x000001866850DFD0>>
我是语法糖age： 18
del ~~~~
30
"""
```
此处使用del相当于调用了一次@age.deleter
# 小结
其实，一套看下来，加来装饰器property与不加，最直观可以看到的即使调用的时候方法变成属性，可以不加()，就可以访问到了。
