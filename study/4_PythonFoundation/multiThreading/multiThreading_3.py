# coding: utf-8

# 3. 多线程 - 调整
from time import ctime, sleep
import threading

# 播放两次音乐，每次1秒
def music(terms):
    for i in range(2):
        print 'I was listening to %s. %s'%(terms, ctime())
        sleep(1)

# 看2场电影，每个5秒
def movie(terms):
    for i in range(2):
        print 'I was watching %s. %s'%(terms, ctime())
        sleep(5)

# 都看完以后就准备去睡觉了
if __name__ == '__main__':
    threads = []
    
    #创建线程t1和t2
    t1 = threading.Thread(target=music, args=(u'双截棍',))
    threads.append(t1)

    t2 = threading.Thread(target=movie, args=(u'无间道',))
    threads.append(t2)

    for t in threads:
        # setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，
        # 如果不设置为守护线程程序会被无限挂起。
        # 子线程启动后，父线程也继续执行下去，
        # 当父线程执行完最后一条语句print "all over %s" %ctime()后，
        # 没有等待子线程，直接就退出了，同时子线程也一同结束。
        t.setDaemon(True)
        # 开始线程活动
        t.start()

    t.join()
    # 增加join()方法，用于等待线程终止。
    # join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。

    print 'All over. I will go to sleep. %s'%ctime()