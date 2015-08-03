#This function returns a list of all perfect squares in a list
import math
def allperfect(list):
    perfects = []
    for x in list:
        if math.sqrt(x) % 1 == 0:
            perfects.append(x)
    return perfects
