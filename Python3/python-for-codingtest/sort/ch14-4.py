import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data) # 우선순위 큐
    
result = 0
while len(heap) != 1: # 힙에 원소가 1개 남을 때까지
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    
    sum_value = first+second
    result += sum_value
    heapq.heappush(heap, sum_value)
    
print(result)