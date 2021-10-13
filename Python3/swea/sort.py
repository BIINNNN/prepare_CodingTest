def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0,i):
            if a[j] >= a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

#카운팅 정렬: 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 함
#선형 시간에 정렬하는 효율적인 알고리즘이지만, 정수나 정수로 표현할 수 있는 자료에 대해서만 적용가능함
def CountingSort(A,B,k):
# A[1..n] -- 입력 리스트 사용된 숫자(1~k)
# B[1..n] -- 정렬된 리스트
# C[1..n] -- 카운트 리스트
    C = [0]*k

    for i in range(0, len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

x = [11, 27, 4, 8, 8, 3, 30, 16]
a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0]*len(a)


BubbleSort(x)
print("Result of Bubble sort :", x)

CountingSort(a,b,5)
print("Result of Counting sort :", b)
