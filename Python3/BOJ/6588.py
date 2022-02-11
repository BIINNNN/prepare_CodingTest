Max = 1000001

# 에라토스테네스의 체 사용
arr = [True for _ in range(Max)] #가능한 전체 수만큼 True로 채워진 리스트 생성 (인덱스 번호가 값)

# 2부터 시작하면서 배수에 해당하는 인덱스에 False 를 넣도록 해주는 과정 반복
# i 만큼씩 증가하는 것은 즉, 해당 수의 배수를 의미
# 소수가 아닌 수를 True -> False 처리해주어서, arr에 소수에 해당하는 값만 True를 갖도록 변환해주는 과정
for i in range(2, 1001):
    if arr[i]:
        for k in range(i+i, Max, i):
            arr[k] = False 
            
while True:
    n = int(input())
    
    if n == 0:
        break #마지막엔 항상 0을 input 해준다고 명시되어 있음
    
    for i in range(3, len(arr)): # 두 홀수 소수의 합이므로 시작이 3
        if arr[i] and arr[n-i]:
            print(n, "=", i, "+", n-i) # 가장 작은 소수부터 시작하므로 b-a가 가장 큰 것을 출력하는 조건을 그냥 만족하게 됨.
            break        