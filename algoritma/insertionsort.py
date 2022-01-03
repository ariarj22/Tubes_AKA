import time

from colors import *

def insertionsort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]

        j = i -1
        while j >= 0 and key < data[j] :
            data[j+1] = data [j]
            drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )
            j -= 1
            time.sleep(timeTick)
        data[j+1] = key
    drawData(data, [BLUE for x in range(len(data))])