def solution(L, x):
    if x in L:
        return [i for i, y in enumerate(L) if y == x]
    else:
        return [-1]
