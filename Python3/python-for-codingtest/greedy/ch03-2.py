n, m = map(int, input().split())

result = 0

for i in range(n):
  cards = list(map(int, input().split())) 
  min_val = min(cards) #해당 행에서 가장 작은 값
  result = max(result, min_val) #가장 작은 것 중 가장 큰 값

print(result)