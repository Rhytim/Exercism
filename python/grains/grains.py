def square(number):
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    count=0
    x=1
    for x in range(65):
        #Have to convert it to int because numbers are too high and pythond rounds it!
        count = int(count)+(2**(x-1))
    return count
        
