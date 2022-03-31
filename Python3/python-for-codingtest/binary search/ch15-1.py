# 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

def count_by_range(arr, left_value, right_value):
    right_idx = bisect_right(arr, right_value)
    left_idx = bisect_left(arr, left_value)
    return right_idx- left_idx

count = count_by_range(arr, x, x)

if count == 0:
    print(-1)
else:
    print(count)