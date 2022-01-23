#회문 문자열 검사

import sys
sys.stdin = open("D:\input.txt","rt")

n = int(input())

for i in range(n):
    s = input()
    s=s.upper() #대소문자 구분 안하므로 통일
    if s == s[::-1]:
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))