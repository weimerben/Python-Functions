#Print Variance of list of values
def Variance(list):
    NList = []
    Avg = sum(list)/float(len(list))
    for i in list:
        NList.append((i-Avg)**2)
    return ((sum(NList)/(len(list) - 1)))
    