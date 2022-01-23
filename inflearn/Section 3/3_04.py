#두 리스트 합치기
import sys
sys.stdin = open("D:\input.txt", "rt")

n = int(input()) #첫 번째 리스트의 크기
arr1 = list(map(int, input().split()))
m = int(input()) #두 번째 리스트의 크기
arr2 = list(map(int, input().split()))
'''
for _ in range(m):
    x = arr2.pop(0)
    arr1.append(x)
    
arr1.sort()
for i in arr1:
    print(i, end=' ')
'''
# 두 리스트가 이미 오름차순으로 정렬되어 있는 상태이므로 두 개 그냥 붙여서 다시 정렬함수 쓰는 것 보다 아래와 같이 구현하는게 시간복잡도가 더 효율적
p1=p2=0 #포인터 변수
new_arr = []

while p1<n and p2<m: # 둘 중 하나라도 끝까지 포인터 이동했다면 종료
    if arr1[p1] <= arr2[p2]:
        new_arr.append(arr1[p1])
        p1+=1
    else:
        new_arr.append(arr2[p2])
        p2+=1
#두 리스트를 비교하면서 새로운 리스트를 만드는 과정에서 포인터 변수 값이 해당 리스트의 길이보다 작은 것은
# 끝까지 가지 못했음을 의미한다. 즉, 새로운 리스트에 들어가지 못한 남은 값들이 있는 것이므로 해당 부분
# (포인터가 가리키는 곳 부터 끝까지)을 그대로 슬라이싱해서 붙여주면 된다.(이미 정렬 되어있기 때문)
if p1<n: 
    new_arr = new_arr+arr1[p1:]
if p2<m:
    new_arr = new_arr + arr2[p2:]

for x in new_arr:
    print(x, end=' ')