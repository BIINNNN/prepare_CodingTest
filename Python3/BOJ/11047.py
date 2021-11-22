n, k = map(int, (input().split()))
coins = []

for i in range(n):
    coins.append(int(input()))

count = 0 #코인의 총 개수

coins.sort(reverse=True) #가장 큰 동전부터 시작하도록 reverse

for coin in coins:
    if k == 0:
        break
    count += k // coin 
    k %= coin #동전으로 나눈 나머지값을 k로 해서 반복문 실행

print(count)