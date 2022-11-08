# 1st way
L = [20, 37, 58, 72, 91]
def solution(L, x):
    L.append(x)
    L.sort()
    return L

# 2nd way
def solution(L, x):
    answer = L
    index = 0
    for i in range(len(L)):
        if L[i]<x:
            index += 1
    answer.insert(index, x)
    return 
