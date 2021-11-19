data = input()

count0 = 0 #모든 숫자를 0으로 만드는 경우
count1 = 0 #모든 숫자를 1로 만드는 경우

#첫 번째 원소에 대해서 처리
if data[0] == '1': #1인 경우에 0으로 만들어 줌
    count0 += 1
else:
    count1 += 1
    
#두 번째 원소부터 모든 원소를 확인하면서 변경
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1': #다음 값이 1인 경우에 0으로 만들어 줌
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1)) #0으로 바꾸는 경우와 1로 바꾸는 경우 중 뒤집는 횟수가 적은 경우가 결과        