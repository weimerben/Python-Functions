#This function prints all odd numbers before a given x
def OddsBefore(x):
    Odds = []
    for i in range(0,x):
        if i % 2 != 0:
            Odds.append(i)
    return Odds
