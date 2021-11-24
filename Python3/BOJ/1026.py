n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0

#a와 b의 가장 큰 수와 가장 작은 수끼리 곱해서 더한 결과를 구하면 됨.
#이 때, B에 있는 수는 재배열 하면 안된다는 조건이 있음
#따라서 a만 작은수부터 차례로 정렬해주고, b 배열에서는 pop()함수를 이용해서 최댓값부터 뽑아서 계산에 사용하도록 함

a.sort() 

for i in a:
    x = i
    y = b.pop(b.index(max(b)))
    
    result += x*y
    
print(result)