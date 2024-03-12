# 라이브러리
import heapq, sys

T = int(input())
heap = []

instructions = []
for _ in range(T):
    instructions.append(int(sys.stdin.readline()))

for instruction in instructions:
    if instruction!=0:
        heapq.heappush(heap, instruction)
    else:
        if not heap:
            sys.stdout.write('0' + '\n')
        else:
            sys.stdout.write(f'{heapq.heappop(heap)}' + '\n')

# 재귀
import sys

def upheap(heap, idx):
    parents_idx = (idx-1)//2
    if parents_idx >= 0 and heap[parents_idx]>heap[idx]:
        heap[parents_idx], heap[idx] = heap[idx], heap[parents_idx]
        upheap(heap, parents_idx)

def downheap(heap, idx):
    left_child, right_child = idx*2+1, idx*2+2
    min_idx = idx
    len_heap = len(heap)
    if left_child<len_heap and heap[left_child] < heap[min_idx]:
        min_idx = left_child
    if right_child<len_heap and heap[min_idx] > heap[right_child]:
        min_idx = right_child

    if min_idx != idx:
        heap[min_idx], heap[idx] = heap[idx], heap[min_idx]
        downheap(heap, min_idx)

T = int(input())
heap = []

instructions = []
for _ in range(T):
    instructions.append(int(sys.stdin.readline()))

for instruction in instructions:
    if instruction!=0:
        heap.append(int(instruction))
        upheap(heap,len(heap)-1)
    else:
        if not heap:
            sys.stdout.write('0' + '\n')
        else:
            sys.stdout.write(f'{heap[0]}' + '\n')
            tmp = heap.pop()
            if heap: 
                heap[0] = tmp
                downheap(heap, 0)

# 반복문
import sys

def upheap(heap, idx):
    parents_idx = (idx-1) >> 1
    new_item = heap[idx]
    while parents_idx>-1:
        if heap[idx] < heap[parents_idx]:
            heap[idx] = heap[parents_idx]
            idx = parents_idx
            parents_idx = (idx-1) >> 1
            heap[idx] = new_item
        else:
            break

def downheap(heap, idx):
    child_idx = idx*2+1
    last_pos = len(heap)
    new_item = heap[idx]

    while child_idx<last_pos:
        right_idx = child_idx+1
        if right_idx < last_pos and heap[child_idx]>heap[right_idx]:
            child_idx = right_idx

        heap[idx] = heap[child_idx]
        idx = child_idx
        child_idx = idx*2+1
    heap[idx] = new_item

    upheap(heap, idx)

T = int(input())
heap = []

instructions = []
for _ in range(T):
    instructions.append(int(sys.stdin.readline()))

for instruction in instructions:
    if instruction!=0:
        heap.append(int(instruction))
        upheap(heap,len(heap)-1)
    else:
        if not heap:
            sys.stdout.write('0' + '\n')
        else:
            sys.stdout.write(f'{heap[0]}' + '\n')
            tmp = heap.pop()
            if heap: 
                heap[0] = tmp
                downheap(heap, 0)
