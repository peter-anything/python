# !/usr/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing
import time
import os

def func(name, process_name, num, arr):
    num.value = int(name) * 2
    for i in xrange(len(arr)):
        arr[i] = arr[i] + 10

    p_info = 'Process[%s] name %s, num.value: %f' %(process_name, name, num.value)
    print(p_info)

def main():
    print('main pid: %d, ppid: ' % (os.getpid()))

    num = multiprocessing.Value('d', 0.0)
    arr = multiprocessing.Array('i', range(10))
    print('main init num: %f' % num.value)
    print('main int arr: %s' % arr[:])

    process_list = []
    for i in xrange(4):
        pro = multiprocessing.Process(target=func, args = (i, 'Process-%d' % i, num, arr))
        pro.start()
        process_list.append(pro)

    for pro in process_list:
        pro.join()

    print('main result num: %f' % num.value)
    print('main result arr: %s' % arr[:])

if __name__ == '__main__':
    main()