#反射的概念
#通过字符串的形式在运行时动态修改程序的变量，方法以及属性的操作。注意，对于反射操作中所有的修改都会在内存中进行，所以它并不会实际修改代码。主要目的是提高代码在运行时的灵活性
#hasattr:输入一个字符串，判断对象有没有这个方法或属性
#getattr：获取对象属性或方法的引用。如果是方法，则返回方法的引用，如果是属性，直接返回属性值。如果该属性或方法不存在，则抛出异常
#setattr:动态添加一个方法或属性
#delattr“动态删除一个方法或属性
class Reflex:
    def __init__(self,name):
        self.name=name

    def test1(self):
        print('{}今年十八'.format(self.name))

    def test2(self):
        print('{}太菜了'.format(self.name))

reflex=Reflex("RAIN")
func=input('请输入你要执行的方法名：')
if hasattr(reflex,func):
    try:
        getattr(reflex, func)()  # getattr返回的是一个方法名
    except TypeError:
        print(getattr(reflex, func)) #打印属性值
else:
    print("没有这个属性或方法")

def test3(city):
    print('{}太冷了'.format(city))

print(dir(reflex))  #在绑定前先查询reflex对象默认的属性和方法名
attr_name=input("请输入一个属性名：")
attr_value=input("请输入一个属性值：")
setattr(reflex,attr_name,attr_value)
print(dir(reflex))  #在绑定后查询reflex对象默认的属性和方法名
print('RAIN的年龄为',getattr(reflex,attr_name))

method=input("请输入要绑定的方法名：")
setattr(reflex,method,test3)
print(dir(reflex))
getattr(reflex,method)('深圳')

delattr(reflex,method)