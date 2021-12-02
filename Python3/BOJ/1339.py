n=int(input())
words = []
for _ in range(n):
    words.append(input())

dict = {}

#딕셔너리에 알파벳별로 값을 집어 넣어준다.
for word in words:
  # -1를 하는 이유는 맨뒤는 1의자리이기 때문에 0 제곱을 수행
  square_root = len(word) - 1
  for c in word:
    if c in dict:
        #값이 있는경우 더해준다.
        dict[c] += pow(10, square_root) #pow()는 n의 m 제곱 수행 (ex, pow(2, 4)는 2의 4제곱)
    else: #값이 없는경우 그대로 넣어준다.
        dict[c] = pow(10, square_root)
    
    square_root -= 1 

#딕셔너리를 큰값부터 쓰기 위해 정렬
dict = sorted(dict.values(), reverse=True)

result, m = 0, 9

#값 계산하기
for value in dict:
    result += value * m
    m -= 1

print(result)