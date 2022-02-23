""" 이 코드는 데이터 수 많아지면 시간이 오래걸림...
n, m = map(int, input().split())
balls = list(map(int, input().split()))

result = 0

for i in range(n):    
    for j in range(i+1, n):
        if balls[i] != balls[j]: 
            result += 1
       
print(result)
""" 
n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 리스트
array = [0]*11

for x in balls:
    #각 무게에 해당하는 볼링공의 개수 카운트해서 저장
    array[x] += 1
    
result = 0

#1부터 m가지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i] #무게가 i인 볼링공의 개수(A가 선택 가능한 개수) 제외
    result += array[i]*n #B가 선택하는 경우의 수와 곱하기
    
print(result)

# 답안 코드니까 꼭 다시 풀어볼 것!!!!!!!!!!!!!!!!!!