import math
def distance_form(lst):
    if len(lst) > 2:
        raise "List too long"
    return math.sqrt(lst[0]**2 + lst[1]**2)
def disform(x, y):
    return math.sqrt(x**2 + y**2)

