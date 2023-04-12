# 类
```python
class Person:
    """这是个Person类"""
    x = '拾贰'  # 也是类属性

    def show(self):  # show就是函数，也叫方法
        """不可以直接外部访问，show。只能通过限定名进行访问Person.show"""
        return __name__


# 类的成员、.运算符访问，类属性、类变量
print(Person)  # 打印类标识符
print(Person.__name__)  # 成员属性
print(Person.__class__, type(Person))  # 这两一回事,都是type
print(Person.__doc__, Person.show.__doc__)  # 9.0 类/方法文档，
print(Person.x)
```
代码中不可以直接外部访问的意思是：
:::success
print(show)
:::
.运算符访问是什么意思？
:::success
类.属性
类.方法
:::
# 实例化
```python
class Person:
    """这是个Person类"""
    x = '拾贰'  # 也是类属性

    def show(self):  # show就是函数，也叫方法
        """不可以直接外部访问，show。只能通过限定名进行访问Person.show"""
        return __name__


pe = Person()   # 实例化
```
实例化实例化后，会自动调用__init__方法。这个方法的第一个形式参数必须留给self，其他形式随意
```python
class Person:
    """这是个Person类"""

    def __init__(self, name,age=18):
        self.name = name
        self.age = age

    def show(self):  # self永远指向当前实例自身,this
        print("我是show方法")


pe = Person('拾贰',20)  # 实例化和初始化
pe1 = Person("清安")
print(f"实例1，{pe}",f"实例2，{pe1}")
print(f"实例1，{pe.name}",f"实例2，{pe1.age}")
print(id(pe),id(pe1))
"""
实例1，<__main__.Person object at 0x000002132C88FFD0> 
实例2，<__main__.Person object at 0x000002132C88FF70>
实例1，拾贰 实例2，18
2281374810064 2281374809968
"""
```
理解：实例化同一个类，但是他们是不同的个体。id打印后可以看到，进一步理解他们不是同一个东西
:::success
self.name ----self 当前实例，name则是实例属性
:::
实例化分为两阶段：

   - 构造实力过程，实例化	先调__new__
   - 初始化过程，初始化		再掉__init__

初始化的前提，必须要实例化
> pe = Person('拾贰',20)
> 等式右边做了两个阶段的事情，实例化和初始化，pe = 实例  赋值

## 示例
```python
class Person:
    """这是个Person类"""

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def show(self):  # self永远指向当前实例自身,this
        print(f"{self.name} is {self.age} yeas old!")


pe = Person('拾贰', 20)  # 实例化
pe.show()
"""拾贰 is 20 yeas old!"""
```
# 绑定
```python
class Person:
    """这是个Person类"""

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def show(self):  # self永远指向当前实例自身,this
        print(f"{self.name} is {self.age} yeas old!")


pe = Person('拾贰', 20)  # 实例化
pe.show()   # 相当于show(pe)  解释器会把pe赋值给self
print(id(pe),hex(id(pe)))
```
看下面的示例更加明显
```python
class Person:
    """这是个Person类"""

    def __init__(self, name, age=18):
        print(id(self))
        self.name = name
        self.age = age

    def show(self):  # self永远指向当前实例自身,this
        print(f"show id is {id(self)}")
        print(f"{self.name} is {self.age} yeas old!")


pe = Person('拾贰', 20)  # 实例化
pe.show()   # 相当于show(pe)  解释器会把pe赋值给self
print(f"id is {id(pe)}")
"""
2241487503312
show id is 2241487503312
拾贰 is 20 yeas old!
id is 2241487503312
"""
```
实例化的时候首先运行Person('拾贰', 20")，再赋值给左边。调用方法的时候，将实例本身传入self中，self可以单独形参进行传参
