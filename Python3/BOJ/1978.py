n = int(input()) #수의 개수
numbers = list(map(int, input().split()))

result = 0 #소수의 개수(출력되어야 할 결과)

for i in numbers:
    cnt = 0
    #1은 소수가 아니므로 패스
    if i == 1:
        continue
    for j in range(2, i+1):
        if i%j == 0:
            cnt += 1
    if cnt == 1:
        result +=1
print(result) 