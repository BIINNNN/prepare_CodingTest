#소수(에라토스테네스 체)

import sys
sys.stdin = open("D:\input.txt","rt")

n = int(input())
check = [0]*(n+1) #소수인지 합성수인지 체크하기 위한 리스트(인덱스번호와 각 자연수 매칭)
count = 0 #소수의 개수 

for i in range(2, n+1): #1은 애초에 소수가 될 조건이 안되므로 2번 인덱스(즉, 자연수 2부터) 소수 여부 확인
    #해당 인덱스 값이 0이면 소수, 1이면 합성수
    if check[i] == 0: #소수인 경우
        #카운트 한 후, 해당 자연수의 배수 찾아서 합성수 체크
        count+=1         
        for j in range(i, n+1, i): #i 간격만큼 더해가며 체크하면 i의 배수들을 찾는 것
            check[j] = 1

print(count)        