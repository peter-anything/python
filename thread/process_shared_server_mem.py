# !/usr/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing
import time
import os

def func(name, process_name, mydict, myarr):
    mydict[name] = int(name) * 2
    for i in xrange(len(myarr)):
        myarr[i] = myarr[i] + 100

    p_info = 'Process[%s] name %s, mydict: %s' %(process_name, name, mydict)
    print(p_info)

def main():
    print('main pid: %d, ppid: ' % (os.getpid()))

    manager = multiprocessing.Manager()
    mydict = manager.dict()
    myarr = manager.Array('i', range(10))
    print('main init mydict: %s' % mydict)
    print('main init arr: %s' % myarr[:])

    process_list = []
    for i in xrange(4):
        pro = multiprocessing.Process(target=func, args = (i, 'Process-%d' % i, mydict, myarr))
        pro.start()
        process_list.append(pro)

    for pro in process_list:
        pro.join()

    print('main result mydict: %s' % mydict)
    print('main result myarr: %s' % myarr[:])

if __name__ == '__main__':
    main()