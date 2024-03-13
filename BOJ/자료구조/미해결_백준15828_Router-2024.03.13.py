'''
<예제>
5
1
2
0
3
4
0
5
6
0
0
-1
<정답>
5 6
'''
# 덱을
import sys
from collections import deque
n = int(input())
queue = deque([],n)
while True:
    inp = int(sys.stdin.readline())
    if inp > 0 and len(queue) < n:
        queue.append(inp)
    elif inp == 0:
        queue.popleft()
    elif inp < 0:
        break

res = ' '.join(map(str,queue))
print('empty' if res == '' else res)

# 100점

# class Queue:
#     def __init__(self) -> None:
#         pass

#     def __repr__(self) -> str:
#         print_list = []
#         f, r = self.front, self.rear
#         if self.is_full():
#             for i in range(self.max_len):
#                 print_list.append(str(self.queue[(i+self.front)%self.max_len]))
#         else:
#             while f != r:
#                 print_list.append(str(self.queue[f]))
#                 f=(f+1)%self.max_len

#         return ' '.join(print_list)

#     def is_empty(self) -> bool:
#         if self.queue[self.rear%self.max_len] is None and self.rear%self.max_len == self.front:
#             return True
#         else:
#             return False

#     def is_full(self) -> bool:
#         if self.queue[self.rear%self.max_len] is not None:
#             return True
#         else:
#             return False

# class CircularQueue(Queue):
#     def __init__(self, list=[], max_len=1) -> None:
#         super()
#         list_len = len(list)
#         self.max_len = max_len

#         if self.max_len <= 1 or len(list)>self.max_len:
#             raise Exception(f"입력으로 주어진 max_len의 값({self.max_len})이 너무 작습니다.")

#         self.queue = [list[i] if i<list_len else None for i in range(self.max_len)]
#         self.front, self.rear = 0, list_len
        

#     @classmethod
#     def create_queue(self, list, max_len):
#         return CircularQueue(list, max_len=max_len)

#     def enqueue(self, element):
#         if not self.is_full():
#             self.queue[self.rear] = element
#             self.rear += 1
#             self.rear %= self.max_len

#     def dequeue(self) -> int:
#         if not self.is_empty():
#             ret = self.queue[self.front]
#             self.queue[self.front] = None
#             self.front += 1
#             self.front %= self.max_len
#             return ret

# import sys
# n = int(input())
# queue = CircularQueue([], n)
# while True:
#     inp = int(sys.stdin.readline())
#     if inp > 0:
#         queue.enqueue(inp)
#     elif inp == 0:
#         queue.dequeue()
#     elif inp < 0:
#         break

# print('empty' if queue.is_empty() else queue)
