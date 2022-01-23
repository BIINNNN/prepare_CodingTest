#수들의 합
import sys
sys.stdin = open("D:\input.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt=0
rt=1
total = arr[0]
cnt = 0

while True:
    if total<m:
        if rt<n: 
            total += arr[rt]
            rt+=1
        # 리스트 끝까지 간 경우 더이상 합을 구할 여분의 숫자가 없으므로 반복문 종료
        else:
            break
    elif total == m:
        cnt+=1
        #왼쪽 포인터가 한 칸 이동하는 모양이므로 가장 왼쪽(lt가 포인팅 하고 있는 인덱스의 값)을 현재 토탈 값에서 빼줘야 함
        total -= arr[lt]
        lt+=1
    else: #total>m
        total -= arr[lt]
        lt+=1

print(cnt)        