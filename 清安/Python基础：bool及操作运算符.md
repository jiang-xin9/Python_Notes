💥bool在后续的使用中是非常常见的，也许会在你不知不觉中就用上了bool。至于操作运算符就更不用说了，重中之重！
🎈注：本章示例来自于群友提供的py文件，感谢
# bool简单示例
```python
print(True)
print(False)
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False
```
> 上述都是基础的不能再基础的用法了，一起来看看其他的：

```python
# 示例：返回 True
bool("Hello")
bool(123456)
bool(["apple","cherry","banana"])

# 示例：返回False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```
# 算数运算符
```python
print(2 + 3)  # 加法
print(3 - 2)  # 减法
print(6 / 3)  # 除法，这里的结果带小数点，如果不想要小数点加个int整数型进行转换就好
print(6 // 3) # 除法，整除
print(2 * 3)  # 乘法
print(3 / 2) # 结果是3.0
print(1 + 2.0) # 结果是：3.0
print(2 * 3.0) # 结果是：6.0
print(2.0 ** 3) # 2.0的三次方，结果是：8.0
```
```python
print(0.2 + 0.1) # 打印后的结果是：0.30000000000000004
 
print(3 * 0.1) # 打印后的结果是：0.30000000000000004
 
print(0.2 + 0.3) # 打印后的结果是：0.5
```
# bool操作符
> 主要分为or、and、not，后续也是非常常用的。
> and: 如果两个语句都为真
> or:  如果其中一个语句为真   
> not: 反转结果，如果结果为True，则 not(x < 5 and x < 10)返回False
> 看看二元运算符：

```python
print(1 and 2) # 2
print(1 or 2) # 1
print(True and False) # False
print(True and True) # True
print(False and True) # False
print(False and False) # False
print(True or False) # True
print(True or True) # True
print(False or True) # True
print(False or False) # False
print(not True) # False
print(not False) # True
```
## 小例子
```python
print((4 < 5) and (5 < 6))   # True
print((4 < 5) and (5 > 6))    # False
print((4 < 5) or (5 > 6))    # True
print((4 > 5) or (5 > 6))    # False
print(1 + 1 == 2 or not 2 + 2 == 4)    # True
print(1 + 1 == 2 and not 2 + 2 == 4)    # False
```
# 比较操作符
| 操作符 | 含义 |
| --- | --- |
| == | 等于 |
| != | 不等于 |
| < | 小于 |
| > | 大于 |
| <= | 小于大于 |
| >= | 大于等于 |

## 小例子
```python
print(1,1 == 1)    # True
print(2,1 == 2)    # False
print(3,1 != 2)    # True
print(4,1 != 1)    # False
print(5,'hello' == 'hello')    # True
print(6,'hello' == 'world')    # False
print(7,'t' == 'T')    # False
print(8,True == True)    # True
print(9,True != False)    # True
print(10,1 < 2)    # True
print(11,1 > 2)    # False
print(12,1 <= 2)    # True
print(13,1 < 1)    # False
```
# 成员运算
> in、not in，适用于字符串以及容器类型
> in：判断是否在里面
> not in：判断是否不在里面

## in-小例子
```python
print('安' in "清安")
list_ = [1,2,3]
print(1 in list_)
dict_ = {"name":"清安"}
print("安" in dict_)
print("na" in dict_)
print("name" in dict_)
"""
True
True
False
False
True
"""
```
> 正常情况下，字典只能判断整个键是否存在于字典中

## not in-小例子
```python
print('安' not in "清安")
print(not '安' in "清安")
```
# 综合例子
```python
num = int(input("请输入一个数字：\n"))
if num < 18:
    print("年龄太小了")
elif num == 18:
    print("年龄刚刚好")
elif num >= 60:
    print("老年人了，注意点")
```
> 一个示范例子，至于拓展，看各位了，学会举一反三。

