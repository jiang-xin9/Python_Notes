> 什么是函数？函数有什么用。

# 定义函数
:::info
在Python中定义函数需要用到def关键字。如下：
:::
```python
def 函数名称():
    内容
```
:::info
使用函数书写代码可以使我们的代码看起来更整洁，更具有可阅读性。
也可以一定程度上减少我们的重读代码书写。并且具有很好的可扩展性
:::
# 调用函数
```python
def number():
    print("清安，本次考试100分")
number()
```
> 最下行的number()就是调用函数。也就是告诉解释器，本次运行我需要运行指定的这个函数。

> 那么如果不加()呢。

```python
def number():
    print("清安，本次考试100分")
number
```
> Pycharm中，会友好的告诉你，number那里有问题，给你一个不同颜色的背景提示。但是真的有问题吗，可以运行看看，实际结果告诉我们并不会有什么异常，只是得不到想要的结果：清安，本次考试100分

# 参数
> 参数可以使得函数变得更加的灵活，例如上述例子中，有多个人得了一百分，你会怎么做呢？
> 写多个函数？还是写多个不同内容的print？

```python
def number(name):
    print(f"{name}，本次考试100分")
number('清安')
number('拾贰')
"""
清安，本次考试100分
拾贰，本次考试100分
"""
```
> 这样写是不是要比说的那两种更好呢？其实这已经实现了一个很不错的功能了。在后续中你会了解到excel、yaml等配置文件读取，可用于这里。

> 这里还是有点小瑕疵的，因为，你想传多个值，那么就必须多次重复调用number这个函数。改一下：

```python
def number(*name):
    for i in name:
        print(f"{i}，本次考试100分")
number('清安','拾贰')
```
> 用*用于接收多个参数传值，在使用for循环即可简化步骤。具体的介绍后续都会说明！

## 默认值
```python
def number(name='拾贰'):
     print(f"{name}，本次考试100分")
number()
number("清安")
```
> 默认值的作用下，可以不传参数，也可以传参数。默认值根据自己的需求来定，可以是数字也可以时其他的数据。

## 任意传参
```python
def number(*name):
    for i in name:
        print(f"{i}，本次考试100分")
number("清安","拾贰","Jon")
"""
清安，本次考试100分
拾贰，本次考试100分
Jon，本次考试100分
"""
```
> 上述中有提到过，*在函数中可以表示解包，也可以是接受元组传值，也就是多参数。在自动化中这样的传值方式用的比较的多。

## 关键字传参
```python
def number(name1,name2):
        print(f"{name1}，本次考试100分")
        print(f"{name2}，本次考试100分")
number(name1="清安",name2="拾贰")
```
> 关键字传参也不一定非要指定参数，也可以这样：

## 位置实参
```python
def number(name1,name2):
        print(f"{name1}，本次考试100分")
        print(f"{name2}，本次考试100分")
number("清安","拾贰")
```
> 解释器会自动帮助你识别，所以这样的方式，根据自己的实际情况来定即可。

## *arg**kwargs
```python
def number(*args,**kwargs):
        print(f"{args[0]},{args[1]}，本次考试100分")
        print(f"{kwargs['name1']},本次考了99分")
number("清安","拾二",name1="清安")
```
> *args**,****kwargs只是惯用的形参名称，大可以写成*name,**ages都可以。注意传值方式，**kwargs是要以字典的格式进行传值的。具体的可以看看本篇[https://www.yuque.com/docs/share/b1ca5613-1f7b-4893-9daf-f8da97e5884a?#](https://www.yuque.com/docs/share/b1ca5613-1f7b-4893-9daf-f8da97e5884a?#) 《Python解包详解》

# return语句
```python
def number(**kwargs):
        return f"{kwargs['name1']},本次考了99分"
print(number(name1="清安"))
```
> 什么时候用return？在这里只能说想用就用，具体如何需要自己体验。唯一需要注意的是，使用return的话，如果想要看到打印结果，那么久需要跟上述代码一样，print函数调用。
> return后，已经代表了函数以及执行结束了，在return 的后面以及不能够在继续写其他的代码了。

# pass语句
```python
def number():
        pass
number()
```
> 一般用于写函数的时候先不写内容的时候写一个pass，或者处理某项事务/错误的后使用pass

# 例题
> 关于例题，可以参考一下：
> 
> 

