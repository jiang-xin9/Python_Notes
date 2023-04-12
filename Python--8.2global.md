global是一个修饰符。全局变量！
```python
x = 0
def num():
    x += 1
    print(x)
num()
```
> 这样的情况下，我们是无法使用x+1的，那么除了把x写入到函数中，还有什么方法可以解决呢。
> 那就是global

```python
x = 0
def num():
    global x
    x += 1
    print(x)
num()
```
> 这样，那么x就是全局变量了，而不再是局部变量了。

