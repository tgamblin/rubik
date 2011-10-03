#!/usr/bin/env python2.6

from blocker import *


if __name__ == "__main__":
    p = Partition.create([8,8,8])
    p.div([8,8,1])

    q = Partition.create([4,4])
    q.div([2,2])

    q.map(p)

    print q.box
    sys.exit(0)




    p = Partition.create([32,16,16,6,2])
    print p.box
    p.zorder()
    p.tilt(1, 0, 2)

    print p.box

    p.transpose([1,0])
    p.div([2,2])

    print p.box

    q = Partition.create([4,4])
    q.mod([2,2])
    q.div([4,1])
    q.map(p)

    print q.box

    q.write_map_file()