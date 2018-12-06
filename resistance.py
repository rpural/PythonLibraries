#! /usr/bin/env python3

from functools import reduce

def resistanceSeries(*resistors):
    return reduce(lambda x,y: x+y, resistors)

def resistanceParallel(*resistors):
    return 1 / reduce(lambda x,y: x + (1 / y), resistors, 0)

if __name__ == "__main__":
    print("resistance in series: {} = {}".format((10, 20, 30),resistanceSeries(10, 20, 30)))
    print(" ")
    print("resistance in parallel: {} = {}".format((10, 20, 30), resistanceParallel(10, 20, 30)))
    print("resistance in parallel: {} = {}".format((4, 2, 4), resistanceParallel(4, 2, 4)))
    print("resistance in parallel: {} = {}".format((24, 12), resistanceParallel(24, 12)))
