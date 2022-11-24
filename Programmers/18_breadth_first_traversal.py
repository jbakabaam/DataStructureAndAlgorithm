# breadth first traversal

class ArrayQueue:

  def __init__(self):
    self.data = []

  def size(self):
    return len(self.data)

  def isEmpty(self):
    return self.size() == 0

  def enqueue(self, item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

  def peek(self):
    return self.data[0]


class Node:

  def __init__(self, item):
    self.data = item
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self, r):
    self.root = r

  def bft(self):
    # 1. 리스트 초기화(Empty List), 큐 초기화(Empty Queue)
    traversal = []
    visitQueue = ArrayQueue()
    
    # 2. 빈 트리(Empty Tree)가 아니면(= 루트 노드 존재), 큐에 루트 노드를 추가(Enqueue)
    if self.root:
      visitQueue.enqueue(self.root)
    
    # 3. 큐가 비어있지 않으면 반복
    while visitQueue.isEmpty()==False:
      node = visitQueue.dequeue() # 큐에서 꺼내서 node에 저장
      traversal.append(node.data) # 꺼낸 노드를 방문 리스트에 저장
      if node.left: # 왼쪽 자식 노드가 존재하는경우 큐에 저장
        visitQueue.enqueue(node.left)
      if node.right: # 오른쪽 자식 노드가 존재하는 경우 큐에 저장
        visitQueue.enqueue(node.right)
            
    return traversal


def solution(x):
  return 0
