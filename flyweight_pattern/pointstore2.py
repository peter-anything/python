import atexit
import os
import shelve
import sys
import tempfile
import time

class Point(object):

    __slots__ = ('x', 'y', 'z', 'color')
    __dbm = shelve.open(os.path.join(tempfile.gettempdir(), 'point.db'))

    def __init__(self, x=0, y=0, z=0, color=None):
        self.x = x
        self.y = y
        self.z = z
        self.color = color

    def __key(self, name):
        return '{:X}:{}'.format(id(self), name)

    def __getattr__(self, name):
        return Point.__dbm[self.__key(name)]

    def __setattr__(self, name, value):
        Point.__dbm[self.__key(name)] = value

    def __repr__(self):
        return 'Point({0.x!r}, {0.y!r}, {0.z!r}, {0.color!r})'.format(self)

    atexit.register(__dbm.close)

def main():
    regression = False
    size = int(1e6)
    if len(sys.argv) > 1 and sys.argv[1] == '-P':
        regression = True
        size = 20
    start = time.clock()
    points = []
    for i in range(size):
        points.append(Point(i, i ** 2, i // 2))
    end = time.clock() - start
    print(points[0])
    if not regression: # wait until we can see how much memory is used
        print("took {} secs to create {:,} points".format(end, size))
        input("press Enter to finish")

if __name__ == '__main__':
    main()