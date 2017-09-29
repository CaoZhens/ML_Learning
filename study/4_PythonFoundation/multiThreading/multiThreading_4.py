# coding: utf-8

# 4. 多线程 - 继续改造函数
from time import ctime, sleep
import threading

# 超级播放器
def superPlayer(file, time):
    for i in range(2):
        print 'Start Playing: %s. %s'%(file, ctime())
        sleep(time)

# 都看完以后就准备去睡觉了
if __name__ == '__main__':
    
    # 待播放的文件与时长
    list = {u'爱情买卖.mp3':3, u'阿凡达.mp4':5, u'我和你.mp3':4}
    threads = []
    
    #创建线程
    for f, t in list.items():
        t = threading.Thread(target=superPlayer, args=(f, t))
        threads.append(t)
    
    # 启动线程
    # 注意：先启动，再阻塞
    for i in range(len(list)):
        threads[i].start()
    for i in range(len(list)):
        threads[i].join()
    
    # 主线程
    print 'All over. I will go to sleep. %s'%ctime()