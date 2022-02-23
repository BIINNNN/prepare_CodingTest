s = input()

result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    
    if num <= 1 or result <= 1: # 1혹은 0이 연산에 포함되는 경우
        result += num
    else:
        result *= num

print(result)