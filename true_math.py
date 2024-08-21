from math import inf
def divide(first, second):
    if second == 0:
        print(inf)
        return
    else:
        result = first / second
        print(result)
        return result
