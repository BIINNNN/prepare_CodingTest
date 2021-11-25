n = list(input()) #str 형태로 저장됨
n.sort(reverse=True)
sum = 0

for i in n:
    sum += int(i) #이 때 0은 합에 영향을 미치지 않음. 따라서 조건 체크할 때 10의 자리 만들 수 있는지 체크해줘야 함
    
    
if sum % 3 == 0 and '0' in n: #30의 배수가 될 수 있는 조건 만족하는지 체크
    print(''.join(n))
else:
    print(-1)