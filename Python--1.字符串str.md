# 前言
请仔细阅读思维导图中的变量命名格式。有问题可以加V：qing_an_an，最后有习题赠送！
如果看不懂如下例子，那么请移步到：
![1657106540296.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/25452484/1657106560610-b661c077-57c2-4333-a04b-be57b5a51b06.jpeg#averageHue=%23a0a0a0&clientId=u4d0176ef-f829-4&from=paste&height=152&id=dUjOd&name=1657106540296.jpg&originHeight=152&originWidth=151&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20432&status=done&style=none&taskId=u42fce756-3cdf-4ee3-b17d-8df6e784146&title=&width=151)
注意代码详解部分出自于源码，这里都只是增加了例子，帮助理解如何运用。
# 思维导图
![](https://cdn.nlark.com/yuque/0/2022/jpeg/25452484/1657605518352-30a44872-e02f-477f-9f4a-f4d482ab119b.jpeg)
# 代码详解
## 常用
### count--统计
计数，可指定字符串在某字符串上出现的次数
```python
d = "QingAn An An"
print(d.count('An'))
# 3
```
### endswith--判断结尾
作用巨大。判断以什么为结尾
_S.endswith(suffix[, start[, end]]) -> bool_
如果S以指定后缀结尾，则返回True，否则返回False。
可以选择起始以及结束的位置。
条件也可以是字符串的元组。
```python
f = "我是Qingan"
# 检索是否以an字符串结尾
print(f.endswith('an'))
# 检索元组元素，存在f的字符串中返回True
print(f.endswith(('我','n')))
# 检索从下标0开始6结束的位置，是否以'是'结尾
print(f.endswith('是',0,6))
# 检索从下标0开始6结束的位置，是否以'g'结尾
print(f[0:6].endswith('g'))
# True
# True
# False
# True
```
### startswith--判断开始
如果S以指定前缀开头，则返回True，否则返回False。可选定开始位置，结束位置，以及前缀为字符串的元组
注意startswith跟endsswith可以互相借鉴用法
```python
y = "你好,QINGAN "
print(y.startswith('你'))
print(y.startswith('好',1,8))
print(y.startswith(',',1))
print(y.startswith(('你','好'),0,9))
# True
# True
# False
# True
```
### index--索引
索引，查找 出某个值第一个匹配项的索引位置。  如果没有则会抛出异常
```python
j = "我是Qingan,欢迎一起学习"
# 查找欢迎在某一位置
print(j.index('欢迎'))	# 9
# 在下标0，20中查找Qingan
print(j.index('Qingan',0,20))	# 2
print(f.index("，"))
＃　ValueError: substring not found
```
### rindex
跟上述ｉｎｄｅｘ类似
```python
f = "你好，清安"
print(f.rindex("，"))
print(f.rindex("好",0,9))
＃　2
＃　1
```
### join--连接
连接任意数量的字符串。调用其方法的字符串插入到每个给定字符串之间。结果将作为新字符串返回。
```python
v = " "
v1 = "-"
v2 = "*"
v3 = "~"
print(v.join('你好,QingAn'))
print(v1.join(['你','好']))
print(v2.join(("清","安")))
print(v3.join({"name":"清安","age":"5"}))
# 你 好 , Q i n g A n
# 你-好
# 清*安
# name~age
```
### replace--替换
替换字符串中的某个值，如果没有，则返回原字符串的副本。
```python
d = "你好，清安"
print(d.replace("你好","HELLO"))
print(d.replace("好你","HELLO"))
＃　HELLO，清安
＃　你好，清安
```
### split--分隔符
默认以空格作为分隔符，可以指定分隔次数，分隔的符号。且最后返回列表
```python
y = " 你好,QING,AN "
y1 = "Qing an "
# 以,分隔符
print(y.split(","))
# 以,分隔符，分隔一次
print(y.split(',',1))
print(y1.split())
# [' 你好', 'QING', 'AN ']
#  [' 你好', 'QING,AN ']
# ['Qing', 'an']
```
### rsplit--右边分隔
默认以空格作为分隔符，可以指定分隔次数，分隔的符号。且最后返回列表。从右边开始
也可以用于去除两端空格
```python
y = " 你好,QING,AN "
y1 = "Qing an "
print(y.rsplit(","))
print(y.rsplit(',',1))
print(y1.rsplit())
# [' 你好', 'QING', 'AN ']
# [' 你好,QING', 'AN ']
# ['Qing', 'an']
```
### lower--小写
返回转换为小写的字符串，注意：两个字符串不是同一个字符串了
```python
x = "你好QINGAN"
print(x.lower())
＃　你好qingan
```
### upper--大写
返回转换为大写的字符串的副本
```python
test = "my home 清安.com"
print(test.upper())
# MY HOME 清安.COM
```
### strip--删除两端空格
返回删除前导和尾随空格的字符串副本。注意：两个字符串不是同一个字符串了
```python
y = " 你好,QINGAN "
y1 = "清安 你好"
print(y.strip())
print(y1.strip())
# 你好,QINGAN
# 清安 你好
```
#### strip--也可删除两端指定字符
```python
a = """11112222\n
44444\t555\n"""
print(a.strip("1"))

a = """
11112222\n
44444\t555\n"""
print(a)
print(a.strip("\n"))
```
### lstrip--删除左边空格
返回删除字符串前面的空格的字符串副本。注意：两个字符串不是同一个字符串了
```python
y = " 你好QINGAN"
y1 = "Qing an"
y2 = " "
print(y.lstrip())
print(y1.lstrip())
print(y2.lstrip())
＃　你好QINGAN
＃　Qing an
＃　
```
### rstrip--删除右边字符
返回删除尾随空格的字符串副本。注意：两个字符串不是同一个字符串了
```python
y = " 你好QINGAN "
y1 = "Qing an "
y2 = " "
print(y.rstrip())
print(y1.rstrip())
print(y2.rstrip())
```
## 不常用
### capitalize--首字母大写

第一个字母大写其他字符串小写
```python
a = 'qing an'
print(a.capitalize())
# Qing an
```
### casefold--转小写
返回无大小写字符串
```python
b = 'Qing An'
print(b.casefold())
# qing an
```
### center--补全
此方法补全参数中的个数，例如下述例子，center(10,"-")，如果c中字符串不足10个，则用-不全
```python
c = "QingAn"
print(c.center(10,'-'))
# --QingAn--
```
### encode--编码
对字符串进行编码，同时也有对应的解码。编码不只一下两种！
```python
e = "我是清安"
print(e.encode(encoding='utf8',errors='strict'))
print(e.encode(encoding='gbk',errors='strict'))
e1 = e.encode('utf8')
print(e1.decode('utf8'))
# b'\xe6\x88\x91\xe6\x98\xaf\xe6\xb8\x85\xe5\xae\x89'
# b'\xce\xd2\xca\xc7\xc7\xe5\xb0\xb2'
# 我是清安
```
### expandtabs--制表符展开
制表符都使用空格展开。如果未给出tabsize，默认tab大小为8个字符
```python
g = "我是Qing\tan"
print(g.expandtabs())
print(g.expandtabs(16))
# 我是Qing  an
# 我是Qing          an
```
### find--索引查找
 如果包含子字符串返回开始的索引值，否则返回-1。  
```python
h = "我是Qingan"
h1 = "an"
# 查找a元素
print(h.find('a'))
# 查找'我'元素，从下标1开始，7结束
print(h.find('我',1,7))
# 在h中查找h1中的元素
print(h.find(h1))
# 6	-1	6
```
### rfind
跟上述的ｆｉｎｄ类似
```python
e = "你好，清安"
print(e.rfind("你",0,10))
print(e.rfind("清"))
```
### format--格式化输出
格式化输出，写法与print(f"{}")无异
```python
i = "我是Qingan"
i1 = 3.1415926
print(f"{i}")
print("{}".format(i))
# 顺序位置，可以理解为按照命名空间来，先写的i，后写的i1
print("{0}{1}".format(i,i1))
print("{1}{0}".format(i,i1))
# 保留小数
print("{:.1f}".format(i1))
print("{:.2f}".format(i1))
```
### format_map
使用映射中的替换返回j的格式化版本。
```python
j = "我是{name}，考试考了{number}"
j1 = {'name':'qingan','number':100}
print(j.format_map(j1))
# 我是qingan，考试考了100
```
### isalnum-判断纯数字字母
 str中至少有一个字符且所有字符都是字母或数字则返回 True,否则返回 False  
```python
k = "我是Qingan,欢迎一起学习"
k1 = "Qingan123"
k2 = "Qingan"
k3 = "123456"
print(k.isalnum())
print(k1.isalnum())
print(k2.isalnum())
print(k3.isalnum())
# False		True	True	True
```
### isalpha--判断纯英文
只能检测英文，其余都是false
```python
l = "我是Qingan,欢迎一起学习"
l1= "12"
l2 = "HELLOQingan"
l3 = "Qingan12"
print(l.isalpha())
print(l1.isalpha())
print(l2.isalpha())
print(l3.isalpha())
#False	False	True	False
```
### isascii
判断字符串中的所有字符都是ASCII，则返回True，否则返回False。
```python
l = "我是Qingan,欢迎一起学习"
l1 = "1234"
l2 = "Qingan"
print(l.isascii())
print(l1.isascii())
print(l2.isascii())
# False		True		True
```
### isdecimal
判断所有字符串中是否为十进制
```python
m = "我是Qingan,欢迎一起学习"
m1 = "1234"
m2 = "Qingan"
print(m.isdecimal())
print(m1.isdecimal())
print(m2.isdecimal())
#False		True		False
```
### isdigit
判断字符串是否为都为数字
```python
n = "我是Qingan,欢迎一起学习"
n1 = "1234"
n2 = "Qingan1"
print(n.isdigit())
print(n1.isdigit())
print(n2.isdigit())
# False		True		False
```
### isidentifier
判断合法标识符
```python
o = "_Qingan"
o1 = "1234"
o2 = "Qingan1"
print(o.isidentifier())
print(o1.isidentifier())
print(o2.isidentifier())
# True		False		True
```
### islower--是否都为小写
判断字符串都是小写字符串
```python
p = "Qingan"
p1 = "1234"
p2 = "QINGAN"
p3 = "qingan"
print(p.islower())
print(p1.islower())
print(p2.islower())
print(p3.islower())
# False		False		False		True
```
### isnumeric--是否都为数字
判断字符串是否都为数字
```python
q = "Qingan"
q1 = "1234"
q2 = "QINGAN"
q3 = "qingan"
print(q.isnumeric())
print(q1.isnumeric())
print(q2.isnumeric())
print(q3.isnumeric())
# False		True		False		False
```
### isprintable--是否可打印
判断字符串可打印或为空，确切的说判断字符串是否符合规范的字符串或为空则返回True
```python
r = "Qing\ran"
r1 = "12\n34"
r2 = "QING AN"
r3 = "qin\tgan"
r4 ="  "
print(r.isprintable())
print(r1.isprintable())
print(r2.isprintable())
print(r3.isprintable())
print(r4.isprintable())
# False		False	True	False		True
```
### isspace--都为空白字符串
判断字符串是都为"空白字符串"
```python
s = "Qingan"
s1 = "1234"
s2 = "QING AN"
s3 = ""
s4 = " "
print(s.isspace())
print(s1.isspace())
print(s2.isspace())
print(s3.isspace())
print(s4.isspace())
# False		False	False	False		True
```
### istitle--开头是否为字符串
 字符串是以标题格式开头的字符串，并且至少有一个字符大写。 大写字符只能跟在无大小写字符后面，而小写字符只能跟在大小写字符后面。  
```python
t = "Qing An"
t1 = "Q1234"
t2 = "QING AN"
t3 = "Qingan"
print(t.istitle())
print(t1.istitle())
print(t2.istitle())
print(t3.istitle())
# True		True	False	True		
```
### isupper--是否都是大写
判断字符串中是否都是大写，如果不是则判断是否有一个是大写(纯英文除外，可以是数字)
```python
u = "Qing An"
u1 = "Q1234"
u2 = "QING AN"
u3 = "Qingan"
u4 = "1234Q"
print(u.isupper())
print(u1.isupper())
print(u2.isupper())
print(u3.isupper())
print(u4.isupper())
# False		True	True	False	True	
```
### ljust--左填充
类似于填充的作用，但是以左对齐。如果填充长度小于字符串长度，则保持原字符串
```python
w = "清安"
w1 = "学习使我快乐"
w2 = "学习使我快乐"
print(w.ljust(10,'*'))
print(w1.ljust(10,'~'))
print(w2.ljust(4,"*"))
＃　清安********
＃　学习使我快乐~~~~
＃　学习使我快乐
```
### rjust--右填充
与ｌｊｕｓｔ相反，用法类似
```python
w = "清安"
w1 = "学习使我快乐"
w2 = "学习使我快乐"
print(w.rjust(4,"*"))
print(w1.rjust(10,"~"))
print(w2.rjust(4,"*"))
＃　**清安
＃　~~~~学习使我快乐
＃　学习使我快乐
```
### maketrans
如果只有一个参数，则它必须是映射Unicode的字典，序号（整数）或字符到Unicode序号、字符串或None。然后，字符键将转换为序数。
如果有两个参数，则它们必须是长度相等的字符串，并且在生成的字典中，x中的每个字符都将映射到字符在y中的相同位置。
如果有第三个参数，则必须是字符串，其字符将在结果中映射为“None”。
```python
z = {"a":1,"b":2,"c":3}
z1 = "QingAn"
z2 = "AnQing"
z3 = "H"
print(str.maketrans({"a":"清","b":"安","c":"安"}))
print(str.maketrans(z1,z2))
print(str.maketrans(z1,z2,z3))
＃　{97: '清', 98: '安', 99: '安'}
＃　{81: 65, 105: 110, 110: 103, 103: 105, 65: 110}
＃　{81: 65, 105: 110, 110: 103, 103: 105, 65: 110, 72: None}
```
### translate
 可配合maketrans使用。根据字符映射表对字符串进行删除和替换操作  。下述例子“将字母m转换为清，将字母y转换为安”
```python
y = "my"
y1 = "清安"
y2 = '.com'
test = "my home 清安.com"
t = str.maketrans(y,y1)		# 创建字符映射转换表
t1 = str.maketrans(y,y1,y2)	# 创建字符映射转换表，并删除指定字符
print(test.translate(t))
print(test.translate(t1))
# 清安 ho清e 清安.co清
# 安 he 清安
```
上述看的模糊可以看如下：
```python
test = "my home 清安.com"
t1 = str.maketrans("my",'清安')
print(test.translate(t1))
# 清安 ho清e 清安.co清
```
### partition--分隔符字符串为元组
使用给定的分隔符将字符串分成三部分。
如果找到分离器，返回一个3元组，其中包含分隔符之前的部分，即分隔符它本身和它后面的部分。
如果未找到分隔符，则返回包含原始字符串的3元组和两个空字符串。
```python
a = "清安，你好"
b = "学习IT，你可以吗"
print(str.partition(a,"，"))
print(str.partition(b,"IT"))
print(str.partition(b,"?"))
＃　('清安', '，', '你好')
＃　('学习', 'IT', '，你可以吗')
＃　('学习IT，你可以吗', '', '')
```
### rpartition
与partition类似
```python
a = "清安，你好"
b = "学习IT，你可以吗"
print(str.rpartition(a,"，"))
print(str.rpartition(b,"IT"))
print(str.rpartition(b,"?"))
# ('清安', '，', '你好')
# ('学习', 'IT', '，你可以吗')
# ('', '', '学习IT，你可以吗')
```
### removeprefix--去除指定字符串前缀
去除指定字符串前缀。**此方法需要手敲**
否则，返回原始字符串的副本。
```python
c = "QING"
c1 = "清安"
print(c.removeprefix('Q'))
print(c.removeprefix('A'))
print(c1.removeprefix('清'))
＃　ING
＃　QING
＃　安
```
### removesuffix--去除指定字符串后缀
去除指定字符串后缀。**此方法需要手敲**
否则，返回原始字符串的副本。
```python
c = "QING"
c1 = "清安 "
print(c.removesuffix('G'))
print(c.removesuffix('A'))
print(c1.removesuffix('清'))
＃　QIN
＃　QING
＃　安
```
### splitlines--去除\n
可去有效去除\r将\n转成空格，并返回一个列表
```python
y = "你\r好\n,QING\tAN "
# str.splitlines(y) 跟 y.splitlines()一致
print(str.splitlines(y))
print(y.splitlines(keepends=True))
# ['你', '好', ',QING\tAN ']
# ['你\r', '好\n', ',QING\tAN ']
```
### swapcase--大小写互转
大小写互转
```python
y = " Hellp,QINGan "
print(y.swapcase())
#  hELLP,qingAN 
```
### title--字符串首字母都大写
将字符串首字母都大写
```python
y = " hello,Qing An "
y1 = "wo shi qing an"
print(y.title())
print(y1.title())
#  Hello,Qing An 
# Wo Shi Qing An
```
### zfill--用零填充
左边用零填充数字字符串，以填充给定宽度的字段。
```python
y = "清安"
print(y.zfill(8))
# 000000清安
```
# 切片
```python
str_ = "我是清安，我学Python"
print(str_[0:7])
print(str_[-1:])    
print(str_[0:10:2])   # 0-10每隔2取一次值
print(str_[0:-1])		# 从0开始取到-1
print(str_[-7:-1])		# 从-7位开始取值
print(str_[::-1])		# 反序列
"""
我是清安，我学
n
我清，学y
我是清安，我学Pytho
学Pytho
nohtyP学我，安清是我
"""
```
![](https://cdn.nlark.com/yuque/0/2022/jpeg/25452484/1658299578525-81cce0aa-903d-4778-887f-4d88c3d261c1.jpeg)
# 填充数字/四舍五入
```python
y = 3.1415926
print("{:.2f}".format(y))
print("{:.0f}".format(y))
print(f"{y:.0f}")
print(f"{y:.2f}")
print('%.2f'%(y))

"""
3.14
3
3
3.14
3.14
"""
```
# 例题
## 链式编程
先用join使得字符串以,连接，然后分隔返回列表，再弹出，最后字符串大写
```python
a = 'abcde'
print(','.join(a).split(',').pop().upper())
# E
```
## 例题变量
```python
test = ' Hello, QingAn. 你今天学习了吗 '
```
### 例题一
将大写字母转为小写
```python
print(test.casefold())
```
### 例题二
将大写字母转为小写，小写字母转为大写。并删除两端空格
```python
print(test.swapcase().strip())
```
### 例题三
输入一串数字，判断其长度时候满足11位，如果满足，则打印后四位
```python
number = input("请输入十一位的数字:\n")
if len(number) == 11 and int(number):
    print(number[-4:])
else:
    print("请重新输入")
```
### 例题四
输入一个字符串，将字符串的开头以及结尾变成'安'
```python
number = input("请输入一个字符串:\n")
str = []
for i in range(len(number)):
    if (i == 0) or (i == len(number)-1):
        str += '安'
        continue
    str += number[i]
    print(str)
print(''.join(str))
```
### 例题五
输入一个字符串，判断时候合法。字符串只能由数字字母组成
```python
s = input('请输入用户名：')
for i in range(len(s)):
    if ( '0' < s[i] < '9') or ( 'a'< s[i] < 'z') or ( 'A'< s[i] < 'Z'):
        continue
    else:
        print('用户名不合法')
        break
else:
    print('用户名合法')
```
### 例题六
输入一串字符串，判断有多少个数字，字母，以及其他字符
```python
num = 0
char = 0
other = 0
s = input('请输入一个字符串：')
for i in range(len(s)):
    if ( '0' <= s[i] <= '9'):
        num +=1
        continue
    if (('a' <= s[i] <= 'z') or ('A' <= s[i] <= 'Z')):
        char +=1
        continue
    else:
        other +=1
print('字母有：%d个,数字有：%d个，其它符号有：%d个' % (char,num,other))
```
### 例题六
输入一串字符串，将字符串中的数字提取出来
```python
s = input('请输入一个字符串：')
str = []
for i in range(len(s)):
    if ( '0' <= s[i] <= '9'):
        str +=s[i]
print(''.join(str))
```
### 例题七
输入两个字符串，打印第二个字符串在第一个字符串中第一次出现的位置（位置用正索引值表示）
```python
str1 = 'how are you? Im fine, Thank you!'
str2 = 'yT'
for i in range(0, len(str1)):
    if str1[i] == str2[0]:
        if str1[i:i + len(str2)] == str2:
            print(i)
            break
else:
    print('不存在')
```
