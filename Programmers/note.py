# 2-1.
L = [20, 37, 58, 72, 91]
def solution(L, x):
    L.append(x)
    L.sort()
    return L

  
# 2-2. 
L = [64, 72, 83, 72, 54]
def solution(L, x):
    if x in L:
        return [i for i, y in enumerate(L) if y == x]
    else:
        return [-1]
