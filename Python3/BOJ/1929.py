m, n = map(int, input().split())

#에라토스테네스의 체 활용
def is_prime(num):
    if num == 1:
        return False # 1은 소수가 아님!
    else:
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0: # num이 어떤 수로 나누었을 떄 나누어 떨어지면 = 어떤수의 배수 이므로 약수 조건을 만족하지 못함
                return False
        #for문을 다 돌았는데 False로 리턴되지 않았으면 그 수는 약수!
        return True
    
for i in range(m, n+1):
    if is_prime(i):
        print(i)