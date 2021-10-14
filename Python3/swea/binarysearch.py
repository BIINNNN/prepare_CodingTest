def binarySearch(a, key):
    start = 0
    end = (len(a)) - 1

    while start <= end:
        middle = start + (end+start) // 2
        if key == a[middle]: #검색 성공
            return True
        elif key < a[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return False

#재귀 함수를 이용한 이진 검색
def binarySearch2(a, low, high, key):
    if low > high: #검색 실패
        return False
    else:
        middle = (low+high)//2
        if key == a[middle]: #검색 성공
            return False
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle+1, high, key)