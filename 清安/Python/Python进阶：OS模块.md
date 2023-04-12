主要是一些常用部分。
# .getcwd()获取当前工作目录
```python
import os

print(os.getcwd())
"""
D:\Python_test\python开发\def_
"""
```
# .chdir()改变当前脚本工作目录
```python
import os

os.chdir('../')
print(os.getcwd())
"""
D:\Python_test\python开发
"""
```
相当于cd命令
# .listdir获取目录下的所有文件和文件夹
包括隐藏文件，返回一个列表
```python
import os

print(os.listdir('../def_'))
"""
['asy.py', 'log.conf', 'log_日志.py','read_yaml.py','__init__.py', '__pycache__']
"""
```
# .mkdir创建文件夹
```python
import os

os.mkdir('../OS_')
```
我是在Python开发的目录下有一个def_文件夹，在文件夹中创建了一个py文件跑的程序，所以，我想在Python开发的目录下再传教一个文件，就出现了上述代码中的../
# .mkedirs递归创建多层目录
```python
import os

os.makedirs('../os_/OS_')
```
运行完成后你就会发现多了一个os_文件夹，os_下还有一个OS_文件夹，也就是这样：D:\Python_test\python开发\os_\OS_
# .remove删除一个文件
```python
import os

os.remove('11.txt')
```
# .rmdir删除单级空目录
若目录不为空则无法删除,则报错
```python
import os
# os.rmdir('../os_/OS_')
os.rmdir('../os_')
```
先创建一个任意文件，此处我的时txt文件。OSError: [WinError 145] 目录不是空的。: '../os_'，是无法删除目录文件的。
# .rename重命名文件/目录
```python
import os
# os.rename('../os_','OS_')
os.rename('OS_/11.txt','OS_/11.py')
```
将上述的目录os_改成了OS_(此处以及修改了目录结构，如果不想修改目录结构记得把../加上)，第二个例子是基于修改目录后OS_下的文件重命名了。记得指定目录。
# .walk遍历工作目录
> 通过自上而下或自下而上遍历目录树来生成目录树中的文件名。对于树中的每个目录，根植于目录顶部（包括顶部本身），它会产生一个 3 元组（目录路径、目录名称、文件名）。

```python
def walk(top, topdown=True, onerror=None, followlinks=False):
```
> - **top** -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
>    - root 所指的是当前正在遍历的这个文件夹的本身的地址、路径
>    - dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
>    - files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
> - **topdown** --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
> - **onerror** -- 可选，需要一个 callable 对象，当 walk 需要异常时，会调用。
> - **followlinks** -- 可选，如果为 True，则会遍历目录下的快捷方式(linux 下是软连接 symbolic link )实际所指的目录(默认关闭)，如果为 False，则优先遍历 top 的子目录。

使用频率最高的也就是top参数。
```python
import os
if __name__ == "__main__":
    for (root,dirs,files) in os.walk('.', topdown=True):
        print (root)
        print (dirs)
        print (files)
        print ('--------------------------------')
"""
.
['.vscode', 'three_', 'zips']
['11.txt', '111.log', 'data_bool.py', 'Matplotlib_.py', 'test.py']
--------------------------------
.\.vscode
[]
['launch.json']
--------------------------------
.\three_
['build', 'dist', 'notes', '__pycache__']
['config.yaml', 'data.json', 'data.py', 'data.spec', 'run.py']
--------------------------------
.\three_\build
['data']
[]
--------------------------------
.\three_\build\data
['localpycs']
['Analysis-00.toc', 'base_library.zip', 'COLLECT-00.toc', 'data.exe', 'data.exe.manifest', 'data.pkg', 'EXE-00.toc', 'PKG-00.toc', 'PYZ-00.pyz', 'PYZ-00.toc', 'warn-data.txt', 'xref-data.html']
--------------------------------
.\three_\build\data\localpycs
[]
['pyimod01_archive.pyc', 'pyimod02_importers.pyc', 'pyimod03_ctypes.pyc', 'pyimod04_pywin32.pyc', 'struct.pyc']
--------------------------------
.\three_\dist
['data']
[]
--------------------------------
.\three_\dist\data
['numpy']
['11.txt', 'base_library.zip', 'data.exe', 'data.json', 'libcrypto-1_1.dll', 'libffi-7.dll', 'libopenblas.FB5AE2TYXYH2IJRDKGDGQ3XBKLKTF43H.gfortran-win_amd64.dll', 'libssl-1_1.dll', 'pyexpat.pyd', 'python39.dll', 'select.pyd', 'unicodedata.pyd', 'VCRUNTIME140.dll', '_asyncio.pyd', '_bz2.pyd', '_ctypes.pyd', '_decimal.pyd', '_hashlib.pyd', '_lzma.pyd', '_multiprocessing.pyd', '_overlapped.pyd', '_queue.pyd', '_socket.pyd', '_ssl.pyd']
--------------------------------
.\three_\dist\data\numpy
['core', 'fft', 'linalg', 'random']
[]
--------------------------------
.\three_\dist\data\numpy\core
[]
['_multiarray_tests.cp39-win_amd64.pyd', '_multiarray_umath.cp39-win_amd64.pyd']
--------------------------------
.\three_\dist\data\numpy\fft
[]
['_pocketfft_internal.cp39-win_amd64.pyd']
--------------------------------
.\three_\dist\data\numpy\linalg
[]
['headset.png', 'mouse.png', '清安.txt']
--------------------------------
.\three_\__pycache__
[]
['data.cpython-39.pyc', 'run.cpython-39.pyc']--------------------------------
.\zips
[]
['headset.png', 'mouse.png', '╟σ░▓.txt']
--------------------------------
"""
```
会将指定的当前根目录下所有的路径都遍历一遍并输出。也可以指定其中一个路径。
## 小示例-文件压缩成zip
```python
from zipfile import ZipFile
import os
  
def get_all_file_paths(directory):
  
    # 将文件写入列表
    file_paths = []
  
    # 获取指定路径的文件
    for root, directories, files in os.walk(directory):
        for filename in files:
            print(root,files)
            # 路径拼接
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # 返回所有
    return file_paths        
  
def main():
    # 需要压缩的路径
    directory = r'three_\notes\zips'
  
    # 传入遍历路径
    file_paths = get_all_file_paths(directory)
  
    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
  
    # 写入压缩文件
    with ZipFile('my_python_files.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
  
    print('All files zipped successfully!')        
  
  
if __name__ == "__main__":
    main()
```
# .system运行终端命令
```python
import os
os.system('ipconfig')
```
# .environ获取系统环境变量
```python
import os

print(os.environ)
```
## 美观打印
```python
import os
import pprint
res = os.environ
pprint.pprint(dict(res))
```
这样打印出来的就是字典格式的了。既然如此字典操作的大部分操作(修改，增加。。)此处都可以使用的。例如：
```python
# 访问特定环境变量
import os
import pprint
res = os.environ['APPDATA']
pprint.pprint(res)
```
## .get获取系统环境变量的某一个值
跟字典取值一致，如果不会，说明基础不好。
```python
import os
import pprint
res = os.environ.get('APPDATA')
pprint.pprint(res)
```
# .getenv获取系统环境变量的某一个值
跟上述差不多的用法
```python
import os
res = os.getenv('APPDATA')
print(res)
```
# .start获取文件/目录信息
```python
import os
print(os.stat('OS_'))
```
# .name输出字符串指示当前使用平台
```python
"""win->'nt'; Linux->'posix'"""
import os
print(os.name)
# nt
```
# .split将目录分割成目录和文件名
返回一个元组
```python
import os
path = r'D:\Python_test\python开发\def_\OS_\11.py'
print(os.path.split(path))
"""
('D:\\Python_test\\python开发\\def_\\OS_', '11.py')
"""
```
# .dirname返回path的父级目录
其实就是os.path.split(path)的第一个元素
```python
import os
path = r'D:\Python_test\python开发\def_\OS_\11.py'
print(os.path.dirname(path))
"""
D:\Python_test\python开发\def_\OS_
"""
```
# .basename返回path最后的文件名
如path以／或\结尾，那么就会返回空值。即 os.path.split(path)的第二个元素
```python
import os
path = r'D:\Python_test\python开发\def_\OS_\11.py'
print(os.path.basename(path))
"""11.py"""
```
# .exists判断path是否存在
存在返回True否则返回False
```python
import os
path = r'D:\Python_test\python开发\def_\OS_\11.py'
print(os.path.exists(path))	# True
```
# .isabs判断path是绝对路径
```python
import os
path = r'D:\Python_test\python开发\def_\OS_\11.py'
print(os.path.isabs(path))	# True
```
# .isfile判断path是一个存在的文件
```python
import os
path = r'D:\Python_test\python开发\def_\OS_\11.py'
print(os.path.isfile(path))	# True
```
# .isdir判断path是一个存在的目录
```python
import os
path = r'D:\Python_test\python开发\def_\OS_'
print(os.path.isdir(path))	# True
```
# .join将多个路径组合后返回
```python
import os

print(os.path.join('D:\Python_test','python开发\def_',r'OS_\11.PY'))
print(os.path.join('D:\Python_test','python开发\def_',""))
"""
D:\Python_test\python开发\def_\OS_\11.PY
D:\Python_test\python开发\def_\
"""
```
# .getatime的最后读取时间
```python
import os
import time
path = r'D:\Python_test\python开发\def_\OS_\11.py'
time_ = os.path.getatime(path)
local = time.ctime(time_)
print('未转化时间',time_)
print('time转化后',local)
"""
未转化时间 1669091559.4411013
time转化后 Tue Nov 22 12:32:39 2022
"""
```
# .getmtime的最后修改时间
```python
import os
import time
path = r'D:\Python_test\python开发\def_\OS_\11.py'
time_ = os.path.getmtime(path)
local = time.ctime(time_)
print('未转化时间',time_)
print('time转化后',local)
"""
未转化时间 1669091559.4411013
time转化后 Tue Nov 22 12:32:39 2022
"""
```
# .getctime文件或者目录的创建时间
```python
import os
import time
path = r'D:\Python_test\python开发\def_\OS_\11.py'
time_ = os.path.getctime(path)
local = time.ctime(time_)
print('未转化时间',time_)
print('time转化后',local)
"""
未转化时间 1669091559.4411013
time转化后 Tue Nov 22 12:32:39 2022
"""
```
# .getsizepath的大小
```python
import os
import time
path = r'D:\Python_test\python开发\def_\OS_\11.py'
res = os.path.getsize(path)
print(res)	# 0
```
# .abspath获取文件的绝对路径
```python
import os

base1 = os.path.abspath('11.tml')
print(base1)
"""
E:\selenium_test\login\11.tml
"""
```
有时候会遇见非绝对路径的情况。我们可以：
```python
import os

base1 = os.path.abspath(__file__)
print(base1)
"""
E:\selenium_test\login\func.py
"""
```
## 作为配置文件获取路径
```python
import os

base1 = os.path.abspath('../')
print(base1)
"""
E:\selenium_test
""“
```
### 拼接路径
```python
base1 = os.path.abspath('../')+'\login'
print(base1)
"""
E:\selenium_test\login
"""
```
## 结合dirname
```python
import os

base = os.path.abspath(os.path.dirname(__file__))
print(base)
"""
E:\selenium_test\login
"""
```
建议这样：
```python
import os

base = os.path.abspath(os.path.dirname('../'))
print(base)
"""
E:\selenium_test
"""
```
更可以：
```python
import os

Base_Path = os.path.abspath(os.path.dirname(os.path.abspath(__file__))+'/..')
print(Base_Path)
```
# 获取磁盘空间
linux可用
```python
disk = os.statvfs('/')
total_space_bytes = disk.f_frsize * disk.f_blocks
free_space_bytes = disk.f_frsize * disk.f_bavail

total_space_gb = round(total_space_bytes / (1024 ** 3), 2)
free_space_gb = round(free_space_bytes / (1024 ** 3), 2)

print("当前磁盘总空间为：", total_space_bytes, "Bytes (", total_space_gb, "GB)")
print("当前磁盘剩余空间为：", free_space_bytes, "Bytes (", free_space_gb, "GB)")
```
window可以用
```python
import ctypes
import os

# 获取当前目录磁盘信息
current_path = os.path.abspath('.')
free_bytes, total_bytes, _ = ctypes.windll.kernel32.GetDiskFreeSpaceExW(current_path)

print("当前目录总空间：", total_bytes // 1024**3, "GB")
print("当前目录可用空间：", free_bytes // 1024**3, "GB")
```
也可以使用psutil模块
```python
pip install psutil
```
```python
disk_size = psutil.disk_usage('/').total
free_size = psutil.disk_usage('/').free
print("当前磁盘内存大小为：{} Bytes".format(disk_size), round(disk_size / 1024 ** 3, 2), "GB")
print("当前磁盘可用内存大小为：{} Bytes".format(free_size), round(free_size / 1024 ** 3, 2), "GB")
```
