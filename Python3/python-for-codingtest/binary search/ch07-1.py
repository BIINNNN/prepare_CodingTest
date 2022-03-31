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