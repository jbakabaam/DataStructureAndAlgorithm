# 1st way: recursive
def solution(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return solution(x-1) + solution(x-2)
  
  
  # 2nd way: iter
  def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        a = b
        b = a + b
        
    return a
