直译就是子程序。作用类似于OS模块。可用于执行系统命令。
# run()
```python
def run(*popenargs,
        input=None, capture_output=False, timeout=None, check=False, **kwargs):
```
> timeout：超时后，子进程将被终止并等待。超时过期异常将在子进程后重新引发已终止。
> capture_output：为真，则将捕获标准输出和标准
> check：如果_检查_为 true，并且进程以非零退出代码退出，则会引发CalledProcessError异常。
> input：如果使用，它必须是字节序列，如果指定了_编码_或_错误_或_文本_为 true，则必须是字符串。

```python
import subprocess

sub = subprocess.run('asy.py',shell=True)
print('sub',sub)
res = subprocess.run('asy.py',shell=True,capture_output=True)
print(res)
res1 = b'\xc7\xe5\xb0\xb2\r\n'
print("解码后",res1.decode('gbk'))
"""
清安
sub CompletedProcess(args='asy.py', returncode=0)
CompletedProcess(args='asy.py', returncode=0, stdout=b'\xc7\xe5\xb0\xb2\r\n', stderr=b'')
解码后 清安
"""
```
> shell=True，调用 shell，命令参数由 shell 直接解释。简单的理解通过shell来跑命令

# Popen()
**推荐使用**
```python
def __init__(self, args, bufsize=-1, executable=None,
                 stdin=None, stdout=None, stderr=None,
                 preexec_fn=None, close_fds=True,
                 shell=False, cwd=None, env=None, universal_newlines=None,
                 startupinfo=None, creationflags=0,
                 restore_signals=True, start_new_session=False,
                 pass_fds=(), *, user=None, group=None, extra_groups=None,
                 encoding=None, errors=None, text=None, umask=-1)
```
一大堆的参数
> 1.  arg 可以是一系列程序参数，也可以是单个字符串或类似路径的对象。 
> 2.  缓冲区 0 表示无缓冲，如果为 1，则表示行缓冲，如果给出任何其他正值，则表示使用大约该大小的缓冲区，如果为负，则将使用默认值。 
> 3.  executable 可执行参数是替换要执行的参数的程序 
> 4.  stdin 标准输入流是指作为 （os.pipe（）） 传递的标准输入流的值 
> 5.  stdout 标准输出是标准输出流的值 
> 6.  STDERR 用于处理从标准错误流中发生的错误（如果有） 
> 7.  可调用对象设置为 preexec_fn。此对象将在执行之前在子进程中调用 
> 8.  close_fds决定在执行子进程之前是应该关闭文件描述符还是应该遵循默认标志 
> 9.  外壳是布尔值。如果为 true，则程序在新的 shell 中执行。 
> 10.  CWD 设置为更改当前执行目录 
> 11.  env 应为 None 或定义新进程的环境变量的映射。将使用这些变量来代替当前进程环境中的默认变量。 
> 12.  universal_newlines是一个布尔值。如果设置为 true，则以通用换行模式打开标准输出和标准输出文件。 
> 13.  当我们将restore_signals设置为 true（默认值）时，Python 设置为 SIG_IGN 的所有信号都会在执行前恢复为子进程中的SIG_DFL 
> 14.  如果start_new_session为 true，则在执行之前将在子进程中调用 setsid（） 
> 15.  如果指定了编码或错误，或者文本为 true，则 stdin、stdout 和 stderr 的文件对象将使用给定的编码和错误以文本模式打开。默认情况下，它们将在 io 中打开。文本IOWrapper格式。 

```python
import subprocess

process=subprocess.Popen(['ipconfig','dir'],stdout=subprocess.PIPE,shell=True)
out_value=process.communicate()[0]
print(repr(out_value))
```
> communicate：返回的是个元组，所以此处是下标取值。

## communicate
Popen 类中的方法之一。它与进程交互，直到到达文件末尾，其中包括将数据发送到 stdin、从 stdout 读取数据和 stderr。
```python
import subprocess

process=subprocess.Popen(['echo','"我是清安"'],stdout=subprocess.PIPE,shell=True)
out_value=process.communicate()[0]
print(repr(out_value))

res1 = b'\"\xce\xd2\xca\xc7\xc7\xe5\xb0\xb2\"\r\n'
print("解码后",res1.decode('gbk'))
"""
b'\\"\xce\xd2\xca\xc7\xc7\xe5\xb0\xb2\\"\r\n'
解码后 "我是清安"
"""
```
# check_all
> 使用参数运行命令。等待命令完成。如果退出代码为零，然后返回，否则引发CalledProcessError
> 它相当于：run(..., check=**True**)

# check_output
> 如果返回代码不为零，则会引发CalledProcessError。对象将在返回代码属性中具有返回代码，在输出属性中具有任何输出。
> 这相当于：
> run(..., check=**True**, stdout=PIPE).stdout

