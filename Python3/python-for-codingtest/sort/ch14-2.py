n = int(input()) # 집의 개수
houses = list(map(int, input().split()))

result = 0

houses.sort()
if n%2 == 0: #집의 개수가 짝수인 경우
    result = houses[n//2 - 1]
else:
    result = houses[n//2]

print(result)