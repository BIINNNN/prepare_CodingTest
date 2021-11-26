s = int(input())
n = 0
sum = 0 #s까지 1을 순차적으로 더한 결과를 저장할 변수

#숫자를 1씩 키워가며 합을 구하고, 그 결과(sum)이 s보다 커지는 순간 n-1을 출력
for i in range(1, s+1):
    sum += i
    n += 1
    if sum>s:
        n -= 1
        break

print(n)