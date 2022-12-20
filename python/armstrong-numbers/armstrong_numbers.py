def is_armstrong_number(number):
    is_armstrong = True
    myList = [int(d) for d in str(number)]
    lenList = len(myList)
    x = 0
    count = 0
    for x in range(lenList):
        count = int(count)+(myList[x]**lenList)
        print(count)
    if number != count:
        is_armstrong = False
    return is_armstrong
    