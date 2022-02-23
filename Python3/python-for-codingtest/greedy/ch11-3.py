#int형이 아닌 문자열임을 주의!!!!!!!!!

s = input()

count0 = count1 = 0 #각각 0으로 뒤집히는 묶음수와 1로 뒤집히는 경우의 수

#첫번째 자리부터 탐색 시작
if s[0] == '0': 
    count1 += 1
if s[0] == '1': 
    count0 += 1
    
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0 += 1
        elif s[i+1] == '0':
            count1 += 1
            
print(min(count0,count1))