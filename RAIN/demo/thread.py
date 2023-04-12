import threading   #python中的多线程模块
import time

nameList=['woniu','python','interface']
def action(content):
    for item in content:
        print(threading.current_thread().getName()+item)
        time.sleep(1)
threads=[]
for i in range(1,4):
    #参数必须以元组形式传入，如果只有一个参数，必须打逗号
    t=threading.Thread(target=action,args=(nameList,))
    t.setDaemon(daemonic=True)
    t.start()
    threads.append(t)
for t in threads:
    t.join()
print ('主线程结束')
#线程常用方法
#join方法：用于阻塞主线程，等子线程运行完后再运行主线程（主线程等待子线程直到天荒地老）
#setDaemon方法：主线程结束，子线程也必须跟着结束（不求同年同月同日生，但求同年同月同日死）