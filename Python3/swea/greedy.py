#BabyGin 예제 - 정렬하지 않을 경우
num = int(input()) #Baby Gin을 확인할 6자리 수

count=[0]*12 #6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6): #6자리 수로부터 각 자리 수를 추출하여 개수를 누적
    count[num%10]+=1
    num //= 10

i = 0
triplete = 0
run = 0
while i<10: #0~9까지 한 자리수 단위로 조사하기 떄문에 리스트 인덱스 10이 되는 순간 종료
    if count[i]>=3: #triplete 조사 후 데이터 삭제
        count[i]-=3
        triplete+=1
        continue
    if count[i]>= 1 and count[i+1]>=1 and count[i+2]>=1: #run 조사 후 데이터 삭제
        count[i]-=1
        count[i+1]-=1
        count[i+2]-=1
        run+=1
        continue

    i+=1

if run+triplete==2: #run과 triplete 모두 만족하는 경우
    print("Baby Gin")
else:
    print("Lose")