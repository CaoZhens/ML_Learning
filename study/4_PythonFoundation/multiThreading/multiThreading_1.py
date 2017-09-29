# coding: utf-8

# 1. 单线程
# music()和move()看作音乐和视频播放器
# 至于要播放什么歌曲和视频，使用时传参

from time import ctime, sleep

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
    music(u'双截棍')
    movie(u'无间道')
    print 'All over. I will go to sleep. %s'%ctime()
