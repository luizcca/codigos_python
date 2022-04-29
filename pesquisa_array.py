a = [3,2,5,4]
b = [2,4,2]

def find_matches(x, y):
    if y == []:            # nothing more to find
        return
    n = y.pop()
    if n in x:
        print (n, "matches")
        x.remove(n)
    find_matches(x, y)

find_matches(list(a), list(b))      # copy the list as they get consumed in process
