# coding: utf-8

# 5. 多线程 - 创建自己的多线程类
from time import ctime, sleep
import threading

# MyThread
# 创建MyThread类，继承自threading.Thread类
class MyThread(threading.Thread):
    # 使用类的初始化方法对func、args、name等参数进行初始化
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        # apply(func [, args [, kwargs ]]) 函数用于当函数参数已经存在于一个元组或字典中时，
        # 间接地调用函数。args是一个包含将要提供给函数的按位置传递的参数的元组。
        # 如果省略了args，任何参数都不会被传递，kwargs是一个包含关键字参数的字典。
        apply(self.func, self.args)


# 超级播放器
def superPlayer(file, time):
    for i in range(2):
        print 'Start Playing: %s. %s'%(file, ctime())
        sleep(time)


# 都看完以后就准备去睡觉了
if __name__ == '__main__':

    # 待播放的文件与时长
    list = {u'爱情买卖.mp3': 3, u'阿凡达.mp4': 5, u'我和你.mp3': 4}
    threads = []

    # 创建线程
    for f, t in list.items():
        # t = threading.Thread(target=superPlayer, args=(f, t))
        t = MyThread(superPlayer, (f, t), superPlayer.__name__)
        threads.append(t)
    
    # 启动线程
    for i in range(len(list)):
        threads[i].start()
    for i in range(len(list)):
        threads[i].join()
    
    # 主线程
    print 'All over. I will go to sleep. %s'%ctime()