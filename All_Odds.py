#This function returns all odd numbers in a list
def AllOdd(list):
    Odds = []
    for x in list:
        if x % 2 != 0:
            Odds.append(x)
    return Odds
    