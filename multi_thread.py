#coding=utf-8
"""
-lesson 4-
 1,多线程
 2,消费者和生产者
 多线程面对共享数据(global 变量 )会有数据错误,要引入线程锁机制,只针共享数据,或者是共同变量
"""
import threading
import time


# def greet(index):
#     print 'hello-%s' %index
#     time.sleep(1)
#
# def line_run():
#     for x in range(5):
#         greet(x)
#
# def async_run():
#     for x in range(5):
#         th = threading.Thread(target=greet,args=[x])
#         th.start()
import random

MONEY = 0
gLock = threading.Lock()

def Procuder():
    while True:
        global MONEY
        random_money = random.randint(10,100)
        gLock.acquire()
        MONEY += random_money
        gLock.release()
        print '生产者%s-生产了: %d' % (threading.current_thread,random_money)
        time.sleep(0.5)

def Customer():
    while True:
        global MONEY
        random_money = random.randint(10,100)
        if MONEY > random_money:
            # print '消费者%s-消费了:%d' %(threading.current_thread,random_money)
            gLock.acquire()
            MONEY-= random_money
            print '需要消费的钱是:%d,余额为:%d' % (random_money, MONEY)
            gLock.release()
        else:
            print '余额不足'
        time.sleep(0.5)

def p_c_test():
    for x in range(3):
        th = threading.Thread(target=Procuder)
        th.start()


    for x in range(3):
        th = threading.Thread(target=Customer)
        th.start()

if __name__ == '__main__':
    # greet(1)
    # line_run()
    # async_run()
    p_c_test()