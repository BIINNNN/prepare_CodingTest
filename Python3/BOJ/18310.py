n = int(input())

house = list(map(int, input().split()))

result = 0

house.sort()
if n%2 == 0: #집의 개수가 짝수인 경우
    result = house[len(house)//2 - 1]
else:
    result = house[len(house)//2]

print(result)