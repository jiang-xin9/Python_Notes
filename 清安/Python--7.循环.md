> 前面说了，条件判断使用的频率非常的高，除此之外，循环的使用频率也是非常的高。
> 循环又分了while循环，for循环，一起看看：

# while循环
```python
while 条件:
	内容
```
## 小例子
```python
a = 0
while a <= 5:
    print("现在数字是：", a)
    a += 1
print("循环结束")
"""
现在数字是： 0
....
现在数字是： 5
循环结束
"""
```
> 既然是循环，那么就存在死循环的问题，什么是死循环？就是一直不断的循环一个代码：

```python
while 1:
	print(1)
```
> while 1与while True一直，意思就是条件为真，既然是真条件，那么就会一直运行，打印1

## break
> 有没有什么，在条件为真的时候，满足条件后结束循环呢。
> 除了上述中的给while添加一个条件之外还有一种，就是break。

### 小例子
```python
a = 0
while True:
    if a == 2:
        break
    print("现在数字是：", a)
    a += 1
"""
现在数字是： 0
现在数字是： 1
"""
```
> 上述只是其中一部分的运用。

## continue
> continue用于跳过本次循环

```python
a = 0
while a < 6:
    if a == 2:
        a += 1
        continue
    print("现在数字是：", a)
    a += 1
"""
现在数字是： 0
现在数字是： 1
现在数字是： 3
现在数字是： 4
现在数字是： 5
"""
```
> while循环处如果是碰上continue记住不要写1或True，否则程序无法正常结束，一定要写明条件判断。

## else
> 除了if可以结合else使用，while一样可以

```python
a = 0
while a < 6:
    name = input("请输入名字：\n")
    age = int(input("请输入年龄：\n"))
    if name == 'qa' and age == 18:
        print("交个朋友吧")
    a += 1
else:
    print("结束了")
```
> 如果while中的条件都不满足时并且循环a=6的时候就会打印else中的内容了。

# for循环
> for循环取值要比while循环简介，for循环取值也叫遍历

```python
for 变量名 in 可迭代对象:
	代码块
```
## 小例子
```python
list_ = ['Python','Java','PHP','C']
for i in list_:
    print(i)
"""
Python
Java
PHP
C
"""
```
> for循环，循环多少次根据可迭代对象中有多少值来定的，什么时可迭代对象，现在不需要知道，只需要知道字符串，列表，元组，字典等都可以遍历取值即可。

## range
> range，结合for来使用的时候可以理解为次数：
> 注意：这里range顾头不顾尾

```python
for i in range(6):
    print(i)
"""
0
1
2
3
4
5
"""
```
> 指定6次就会循环6次，不过是默认从0开始循环遍历。
> 也可以指定从几开始：

```python
for i in range(1,6):
    print(i)
```
> 这样就是从1开始循环到6。
> 还可以指定步长：

```python
for i in range(1,6,2):
    print(i)
"""
1
3
5
"""
```
> 默认步长为1，这里步长为2意思就是每隔两个值取一次值。

### 小例子-结合break
```python
for i in range(1,6):
    if i == 2:
        print(i)
        break
"""
2
"""
```
### 小例子-结合continue
```python
for i in range(1,6):
    if i == 2:
        print(i)
        continue
    if i == 3:
        print(3)
        break
```
## 嵌套例子--99乘法表
```python
for i in range(1,10):
    for j in range(1,i+1):
        print(i, '*', j, '=', i*j, end='  ')
    print()
```
> end中写入\t也是可以的

# 
