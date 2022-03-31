# 부품 찾기
n = int(input())
arr = list(map(int, input().split())) # 전체 부품
arr.sort()
m = int(input())
orders = list(map(int, input().split())) # 손님이 주문한 부품

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
    
for order in orders:
    result = binary_search(arr, order, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        
'''
# 계수 정렬을 이용한 풀이

n = int(input())
arr = [0]*1000001

for i in input().split():
    arr[int(i)] = 1
    
m = int(input())
orders = list(map(int, input().split()))

for order in orders:
    if arr[order] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
'''

'''
# 집합 자료형(set)을 이용한 풀이

n = int(input())
arr = set(map(int, input().split()))

m = int(input())
orders = list(map(int, input().split()))

for order in orders:
    if order in arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''