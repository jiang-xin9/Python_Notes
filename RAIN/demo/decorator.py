import time
def timer(func):
    def gf():
        start_time=time.time()#记录当前时刻
        func()
        end_time=time.time()#记录结束时刻
        print('函数运行时间为：',end_time-start_time)
    return gf


@timer
def foo():
    sum=0
    for i in range(100000000):
        sum+=i
    print(sum)
foo()
#二者等同

def foo():
    sum=0
    for i in range(100000000):
        sum+=i
    print(sum)
foo=timer(foo)
foo()
