#This function returns the standard deviation of a list of values
import math
def StandardDev(list):
    NList = []
    Avg = sum(list)/float(len(list))
    for i in list:
        NList.append((i-Avg)**2)
    return math.sqrt((sum(NList)/(len(list) - 1)))
    