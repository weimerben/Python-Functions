#This function returns all even numbers before a value of x
def EvensBefore(x):
    Evens = []
    for i in range(1,x):
        if i % 2 == 0:
            Evens.append(i)
    return Evens

print EvensBefore(100)