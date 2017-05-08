# !/usr/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing
import time
import os

def func(name, process_name, queue):
    p_info = 'Process[%s] hello %s' % (process_name, name)
    queue.put(p_info)

    print('queue put: %s' % p_info)
    print('sub pid: %d, ppid: ' % (os.getpid()))

def main():
    print('main pid: %d, ppid: ' % (os.getpid()))

    q = multiprocessing.Queue()
    process_list = []
    for i in xrange(4):
        pro = multiprocessing.Process(target=func, args = (i, 'Process-%d' % i, q))
        pro.start()
        process_list.append(pro)

    for pro in process_list:
        pro.join()

    print('queue size %d' % q.qsize())
    while not q.empty():
        p_info = q.get(block=False)
        print('queue get: %s' % p_info)

if __name__ == '__main__':
    main()