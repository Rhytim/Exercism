def equilateral(sides):
    if all(item == 0 for item in sides):
        return False
    else:
        return (sides[0] == sides[1] == sides[2])

def isosceles(sides):
    return is_valid(sides) and len(set(sides)) < 3

def scalene(sides):
    return is_valid(sides) and len(set(sides)) == 3

def is_valid(sides):
    return all(sides) and (sum(sides) >= max(sides)*2)

        

          


            




