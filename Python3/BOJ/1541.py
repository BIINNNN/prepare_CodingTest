exp = input().split('-') #- 기준으로 입력식을 나눠줌

result = 0

for i in range(len(exp)):
    #ex) exp = ['55', '50+40']과 같은 형태일 때, 합으로 이루어진 식들을 계산하도록 반복문 구현
    exp[i] = sum(map(int, exp[i].split('+')))
    if i == 0:
        result = exp[i]
    else: #합도 해결 했으니 계산된 모든 값을 가장 앞의 수부터 뺄셈을 해주면 됨
        result -= exp[i]
        
print(result)