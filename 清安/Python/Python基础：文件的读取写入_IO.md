# mode
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25452484/1660615923369-d48c0862-90c2-4161-8a6c-a2e3c2a5d2b4.png#clientId=ufae4ceae-9f21-4&from=paste&height=294&id=u83386624&name=image.png&originHeight=294&originWidth=642&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52722&status=done&style=none&taskId=u761df31f-29d2-4b12-ae95-b79d50278b7&title=&width=642)
# 读r
```python
f = open('test.txt')    # 打开一个文件,mode默认是r
print(f.read())
f.close()	# 关闭文件
```
> 需要先创建一个文件

# 写w
```python
f = open('test.txt',mode='w')    # 打开一个文件
f.write('我是清安，你是拾贰')		# 写入
f.close()
r = open('test.txt')
print(r.read())
r.close()
"""我是清安，你是拾贰"""
```
> 文件不存在时，会自动创建一个。如果文件存在内容会被清空。
> 如果想在本次持续写入内容可以在字符串后面加上"\n"，正常来说是\r\n表示回车换行，但是python已经帮我们做了优化。

# 创建写入x
```python
f = open('test.txt',mode='x')    # 打开一个文件
f.write('我是清安，你是拾贰')
f.close()
```
> 创建并写入文本。如果文件存在会抛出异常

# 追加a
```python
f = open('test.txt',mode='a')    # 打开一个文件
f.write('\n我是13，你是14\n')
f.close()
```
> 追加在文本尾部，可以加上\n进行换行写入。如果文本不存在也会自动创建一个

# 二进制b
```python
f = open('test.txt',mode='wb')    # 打开一个文件
f.write(b'xyz')
f.close()
```
不能单独使用，需要结合使用wb,rb,ab,xb
```python
f = open('test.txt',mode='wb')    # 打开一个文件
f.write('拾贰'.encode())
f.close()
r = open('test.txt',encoding='utf-8')
print(r.read())
r.close()
```
> 也可以使用encode编码写入，读取时需要指定utf-8的格式读取
> 二进制可以用来写入一个图片的数据。
> 二进制也可用来写入文本，可以指定格式，如上所述.encode()，encode里面可以是gbk的任意形式

# 缺省t
> t是text，文本模式，默认可以不写
> t模式不能单独使用，需要跟w、r、a、x一起使用wt,rt,at,xt用法跟上述类似

```python
f = open('test.txt',mode='at')    # 打开一个文件
f.write('我是13，你是14')
f.close()
————————————————————————————————--
f = open('test.txt',mode='wt')    # 打开一个文件
f.write('我是13，你是14')
f.close()
```
# +
> +不可单独使用，给r、w、a、x提供缺失的读或者写功能，并且保留原特征

```python
f = open('test.txt',mode='r+')    # 打开一个文件
f.write('拾贰121212')
print(f.read())
f.close()
```
> r+既读又能写。值得注意的时文件指针指向文本开头，如果文本中本就存在文字，那么会出现覆盖。根据字节进行覆盖。默认为gbk格式，所以一个汉字两个字节

```python
f1 = open('test.txt',mode='w+')    # 打开一个文件
f1.write('拾贰，你好啊')
print(f1.read())
f1.close()
```
> w+不能直接读取到内容

```python
f2 = open('test.txt',mode='a+')    # 打开一个文件
f2.write('\n清安，你好啊')
print(f2.read())
f2.close()
```
> a+也不能直接读取到内容

# seek偏移
:::info
.seek(n,偏移位置)，n表示字节
假如我有一个log.txt文本文件，内容是：我是清安QingAn
:::
```python
with open('log.txt',mode='rb') as r:
    # 以开头为参照，停在第二个字节位置
    r.seek(2,0)
    # 获取指针当前位置
    print(r.tell())
    """模式1"""
    r.seek(2,1) # 当前位置往后移动两个字节
    r.seek(3,1) # 在上一步的位置再向后移动三个字节
    """模式2"""
    r.seek(-2,2) # 末尾字节，所以需要反向移动
    r.seek(-4, 2)  # 在上一步的位置再反向移动四个字节
```
:::info
模式1以及模式2不能在t模式下使用，b模式可以使用三种模式
:::
# 小例子
```python
while True:
    res = input(">>>我充值了多少：")
    with open('11.txt', mode='a',encoding='utf8') as w:
        w.write(f'充值了{res}W\n')
```
```python
with open('11.txt',mode='rb') as r:
    r.seek(0,2)
    while True:
        res = r.readline()
        if res:
            print(res.decode('utf-8'),end='')
        time.sleep(0.2)
```
:::danger
上述是两个py文件，先运行rb的再运行a的
:::
# 总结
> read以及write只是其中的一个方法，还有很多其类似的方法，读取一行等等

:::info
有时候读取比较慢的时候，是因为一次性读取内容较大(从硬件直接读取到了内存)，可以尝试一次性读取固定长度的数据，循环读取：
:::
```python
with open('log.txt',mode='r') as r:
    r.read(1024)
```
