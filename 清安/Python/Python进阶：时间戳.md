# time模块
## time()
一般用于计算时间差，也称之为时间戳，例如：
```python
import time

def s_time():
    start = time.time()
    for i in range(5):
        time.sleep(1)
    end = time.time()
    print(f"共花费{end-start}S")
s_time()
```
计算循环总计花费多长时间，这里可能出现5.0012545这类的值。问题不大，这是因为time.time获取是值是从1970年到现在的时间。
## strftime()
```python
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身
```
看不懂是吧，举个例子：
```python
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 2022-07-19 17:24:25
```
获取当前时间，上述的参数也就是例子中的参数，组合起来用。
## localtime()
```python
print(time.localtime())
"""time.struct_time(tm_year=2022, tm_mon=7, tm_mday=19, tm_hour=17, tm_min=25, 
tm_sec=52, tm_wday=1, tm_yday=200, tm_isdst=0)"""
```
他得到的是这么一个玩意，啥意思很明显了吧，年-月-日-时-分-秒-本周过去了几天(这里是从0开始的,1也就是过去了两天，今天是今年的第多少天(此处过去200天),最后这个参数用不上，不管)
```python
res = time.localtime()
print(res.tm_year,"-",res.tm_mon)
# 2022 - 7
```
# datetime模块
```python
from datetime import datetime
```
```python
import datetime
```
同样是使用datetime。上面二者是有一定区别的，例如：
```python
from datetime import datetime

print("当前时间是：",datetime.now())
print("今天的时间是：",datetime.today())


import datetime
print("当前时间是：",datetime.datetime.now())
print("今天的日期是",datetime.date.today())

"""
当前时间是： 2022-07-19 17:45:08.527419
今天的时间是： 2022-07-19 17:45:08.527420
当前时间是： 2022-07-19 17:45:08.527419
今天的日期是 2022-07-19
"""
```
一个是datetime类，一个是datetime模块
## strftime()
常用的也就是这个了。
```python
import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now)
# 2022-07-19 17:49:19
```
同理，也是可以分配的，犹如time模块中所提到的谁看谁懵逼系列。里面的参数可以搭配。
## date
获取当前日期
```python
print(datetime.date.today())
# 2022-07-19
```
### 其他用法
```python
d = datetime.date(2022, 7, 19)
print(d)
# 2022-07-19
```
### fromtimestamp转换时间戳
```python
import time
from datetime import date
now = time.time()
timenow =date.fromtimestamp(now)
print(timenow)
# 2022-07-19
```
此处写import datetime也是可以。只是写fromtimestamp处的时候没有提示罢了。
### today分别获取年月日
```python
from datetime import date

# 今天的日期对象
today = date.today()

print("当前年:", today.year)
print("当前月:", today.month)
print("当前日:", today.day)

"""
当前年: 2022
当前月: 7
当前日: 19
"""
```
## time
他需要自己传入时间
```python
import datetime

print(datetime.time(12,13,14))
"""12:13:14"""
```
也可单独获取时分秒微秒
```python
import datetime

a = datetime.time(12,13,14,520)
print("小时=", a.hour)
print("分钟=", a.minute)
print("秒=", a.second)
print("微秒=", a.microsecond)

"""
小时= 12
分钟= 13
秒= 14
微秒= 520
"""
```
## datetime
与上述类似了，用法上有点区别
```python
# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime.datetime(2022, 12, 13, 14, 52, 00, 131421)
print(b)
"""
2022-12-13 14:52:00.131421
"""
```
易可
```python
# datetime(year, month, day, hour, minute, second, microsecond)
a = datetime.datetime(2022, 12, 13, 14, 52, 00, 131421)
print("年 =", a.year)
print("月 =", a.month)
print("日 =", a.day)
print("时 =", a.hour)
print("份 =", a.minute)
print("时间戳 =", a.timestamp())

"""
年 = 2022
月 = 12
日 = 13
时 = 14
份 = 52
时间戳 = 1670914320.131421
"""
```

# 自动化示例
## 截图并以时间戳方式命名
```python
import datetime
from selenium import webdriver

fox = webdriver.Firefox()
fox.get('https://www.baidu.com')
file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
print(file_name)
fox.get_screenshot_as_file(file_name+'.png')
fox.quit()
```

