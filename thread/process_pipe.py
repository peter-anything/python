# !/usr/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing
import time
import os

def func(name, process_name, pipe):
    p_info = 'Process[%s] hello %s' % (process_name, name)
    print('pipe send: %s' % p_info)
    pipe.send(p_info)


    print('sub pid: %d, ppid: ' % (os.getpid()))

def main():
    print('main pid: %d, ppid: ' % (os.getpid()))

    pipe_parent, pipe_child = multiprocessing.Pipe(duplex = False)

    process_list = []
    for i in xrange(4):
        pro = multiprocessing.Process(target=func, args = (i, 'Process-%d' % i, pipe_child))
        pro.start()
        process_list.append(pro)

    for pro in process_list:
        pro.join()

    pipe_child.send(None)

    while pipe_parent:
        p_info = pipe_parent.recv()
        print('Pipe get: %s' % p_info)

        if not p_info:
            print('Pipe get: None, then exit out')
            break

if __name__ == '__main__':
    main()