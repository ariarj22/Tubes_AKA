import time

from colors import *

def combsort(data, drawData, timeTick):
    length = len(data)
    shrink = 1.3
    _gap = length
    sorted = False
    while not sorted:
        _gap /= shrink
        gap = int(_gap)
        if gap <= 1:
            sorted = True
            gap = 1
        for i in range(length - gap):
            sm = gap + i
            if data[i] > data[sm]:
                data[i], data[sm] = data[sm], data[i]
                sorted = False
                drawData(data, [YELLOW if x == i or x == sm else BLUE for x in range(len(data))] )
    drawData(data, [BLUE for x in range(len(data))])