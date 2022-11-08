# 1.
def solution(x):
    answer = x[0]+x[-1]
    return answer


# 2-1. Linear Array
L = [20, 37, 58, 72, 91]
def solution(L, x):
    L.append(x)
    L.sort()
    return L

def solution(L, x):
    answer = L
    index = 0
    for i in range(len(L)):
        if L[i]<x:
            index += 1
    answer.insert(index, x)
    return answer

  
# 2-2. Linear Array
L = [64, 72, 83, 72, 54]
def solution(L, x):
    if x in L:
        return [i for i, y in enumerate(L) if y == x]
    else:
        return [-1]


# 3. Binary Search
L = [2,3,5,6,9,11,15]
def solution(L, x):
    lower = 0
    upper = len(L) - 1
    idx = -1
    
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            idx = middle
            break
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1
            
    return idx
