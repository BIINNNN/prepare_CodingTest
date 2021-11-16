T = int(input()) #테스트 케이스 수

for i in range(T):
    n, m = map(int, input().split()) #서쪽 n, 동쪽 m
    answer = 1
    
    #다리를 놓을 수 있는 개수는 조합으로 - mCn
    if n == m: #가능한 다리의 수가 1개밖에 되지 않음
        print(answer)
        
    else:
        for i in range(m, m-n, -1):
            answer *= i
            
        for j in range(n, 1, -1):
            answer //= j # / 를 사용 시, 실수형 계산에서 오차 발생
        
        print(answer)