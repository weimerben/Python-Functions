#This function returns a list of all even values in a list
def AllEven(list):
    Evens = []
    for x in list:
        if x % 2 == 0:
            Evens.append(x)
    return Evens        
