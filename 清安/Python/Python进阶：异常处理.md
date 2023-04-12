这里需要注意的是错误是Error，异常是Exception。
异常是可以被捕捉的，被处理的，但是错误是不能被捕获的。
[异常官方文档](https://docs.python.org/3/library/exceptions.html)
> 我们一般情况下，习惯性的叫pycharm控制台给出的红色字体叫报错。其实不然，是异常。

:::danger
异常产生：
raise语句显示的抛出异常
Python解释器自己检测到的异常，并引发它
:::
```python
print(1/0)
"""
	print(1/0)
ZeroDivisionError: division by zero
"""
```
```python
def fuc(num):

    if num == 1:
        raise Exception('错了呢')
fuc(1)
"""
    raise Exception('错了呢')
Exception: 错了呢
"""
```
:::danger
看示例一中带有Error，实则并非正真的错误，它是由一层一层代码结构继承下来的，可以理解为继承自异常类下的Error类名。
:::
# 捕获异常
```python
try:
    print("正在捕捉")
    print(1/0)
except ZeroDivisionError:
    print("不可以除0")
"""
正在捕捉
不可以除0
"""
```
## 多个except
```python
try:
    n = int(input('请输入一个数字:'))
    print(n)
except ValueError:
    print("输入整数啦")
except KeyError:
    print("key not found")
except FileNotFoundError:
    print("file not found")
```
:::danger
在try后面，可以接多个except，在异常后，会精准输出对应的异常提示。
:::
## except与打印指定信息
:::danger
正常情况下，except可以捕捉错误类型，且打印指定的错误信息
:::
:::info
那么有没有一种方法可以直接访问捕捉异常呢，俗称：只想捕捉异常并直接打印对应信息。肯定有的
:::
```python
class Myexception(Exception):
    def __init__(self,code,message):
        self.code = code
        self.message = message

try:
    raise Myexception(code="404",message="Not")
except ValueError:
    print("输入整数啦")
except KeyError:
    print("key not found")
except FileNotFoundError:
    print("file not found")
except:
    print("我啥都捕捉")
"""
我啥都捕捉
"""
```
:::info
不论在何时都可以使用except。这里写的复杂例子后续还有其他内容要说。
Myexception继承自Exception，并且初始化了。这跟源码有关系。
:::
### 不同层次的打印信息
> 正常情况下我们是直接捕捉错误并且print的。
> 还有另一种方式：

```python
class Myexception(Exception):
    def __init__(self,code,message):
        self.code = code
        self.message = message

try:
    raise Myexception(code="404",message="Not")
except ValueError:
    print("输入整数啦")
except KeyError:
    print("key not found")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(e)
    print(e.code,e.message)
    print("我就是猖狂，我全部揽下来")
```
> 那就是as e的方式，我们需要在抛出异常的时候传入初始化参数，也就是报错提示，随后捕捉的时候使用.code,.message的方式输出。这里的e，也可以是其他的东西，类似于变量。

# finally
> 可以理解为只要写了它，不论如何都会执行先关语句。在退出try的时候总是会执行。

```python
try:
    f  = open('test')
except ValueError as e:
    print(e.args,e.__dict__,sep='||')
except Exception as e:
    print(e.args,e.__dict__,sep='||')
finally:
    print("不论怎么样，我都会执行")
"""
(2, 'No such file or directory')||{}
不论怎么样，我都会执行
"""
```
> 可以看到即使异常了，也还是会执行的。sep的用法，请看[零散小方法](https://www.yuque.com/docs/share/864f1b44-8931-42d1-8881-33db0765787e?#) 

# else
> 在没有异常的时候执行这个语句

```python
try:
    print(1//1)
except ValueError as e:
    print(e.args,e.__dict__,sep='||')
except Exception as e:
    print(e.args,e.__dict__,sep='||')
else:
    print("No Exception,action")
"""
1
No Exception,action
"""
```
# finally和else
```python
try:
    print(1//1)
except ValueError as e:
    print(e.args,e.__dict__,sep='||')
except Exception as e:
    print(e.args,e.__dict__,sep='||')
else:
    print("No Exception,action")
finally:
    print("Start Action , Show Time")
"""
1
No Exception,action
Start Action , Show Time
"""
```
> 这二者可以结合使用，此外你也可以在这其中加入一系列的代码，例如for循环，if判断等

# 小结
> 1、如果try中语句执行时发生异常，搜索except子句，并执行第一个匹配该异常的except子句
> 2、如果try中语句执行时发生异常，却没有匹配的except子句，异常将被递交到外层的try，如果外层不处理这个异常，异常将继续向外层传递。如果都不处理该异常，则会传递到最外层，如果还没有处理，就终止异常所在的线程
> 3、如果在try执行时没有发生异常，如有else子句，可执行else子句中的语句
> 4、无论try中是否发生异常，finally子句最终都会执行

