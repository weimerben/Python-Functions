#This function prints a list of all perfect squares before a given x
import math
def perfectbefore(x):
    perfects = []
    for i in range(0,x):
        if math.sqrt(i) % 1 == 0:
            perfects.append(i)
    return perfects

    