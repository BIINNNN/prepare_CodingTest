#숫자만 추출
import sys
sys.stdin = open("D:\input.txt", "rt")

sen = input()
num = 0
cnt = 0
for x in sen:
    if x.isdecimal():
        num = num*10+int(x)

for i in range(1, num+1):
    if num % i == 0:
        cnt+=1

print(num,cnt, sep='\n')  