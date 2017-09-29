# coding: utf-8

# 6. 多线程
# 利用线程池处理
from time import ctime, sleep
import threading
import Queue
# Python Queue用法：详见印象笔记

class ThreadPoolMgr():
    def __init__(self, work_queue, thread_num):
        self.threads = []
        self.work_queue = work_queue
        self.init_threadpool(thread_num)

    def init_threadpool(self, thread_num):
        for i in range(thread_num):
            self.threads.append(MyThread(self.work_queue))
    
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()


# MyThread
# 创建MyThread类，继承自threading.Thread类
class MyThread(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self):
        # 从任务队列中取任务，直至队列为空
        while not self.work_queue.empty():
            d = self.work_queue.get()
            superPlayer(d['f'], d['t'])


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

    # 初始化任务队列
    taskQueue = Queue.Queue()
    for f, t in list.items():
        taskQueue.put({'f':f ,'t':t})
    
    # 定义并执行线程池
    p = ThreadPoolMgr(taskQueue, 3)
    p.wait_allcomplete()
    
    # 主线程
    print 'All over. I will go to sleep. %s'%ctime()