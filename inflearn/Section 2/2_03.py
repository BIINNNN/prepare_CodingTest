#K번째 큰 수 
import sys
from itertools import combinations
sys.stdin=open("D:\input.txt","rt")

n, k = map(int, input().split())
a = list(map(int, input().split())) #n개의 수]
res = list(set()) #3개의 숫자 합을 저장할 리스트(k번째 수 찾기 위해 중복제거)

#Sol 1) 삼중 for문 사용 (3개만 뽑으면 되는 간단한 문제라 반복문으로 구현해도 크게 문제 없음)
# for i in range(n):
#     for j in range(i+1, n):
#         for m in range(j+1, n):
#             res.add(a[i]+a[j]+a[m])

# res = list(res) #set에는 sort기능이 없어서 리스트화 시켜줌
# res.sort(reverse=True) #내림차순 정렬

#Sol 2) combination 라이브러리 사용
for combination in list(combinations(a, 3)):
    res.append(sum(combination))
    res.sort(reverse=True)
    
print(res[k-1]) #k번 째