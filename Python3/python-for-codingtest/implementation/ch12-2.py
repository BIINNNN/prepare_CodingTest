#문자열 재정렬
s = input()

result = []
num = 0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        num += int(i) #i 는 str 형태임 주의
        
result.sort()

if num != 0:
    result.append(str(num))
    
print(''.join(result)) # 그냥 result 출력하면 리스트 형태로 출력되기 때문에 문자열 형태로 변환해 주어야 함.