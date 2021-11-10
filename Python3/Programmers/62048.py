import math

def solution(w,h):
    answer = 0
    total = w*h
    cutting = w+h-math.gcd(w, h) #최대공약수 구해주는 파이썬 내장함수 math.gcd()

    answer = total - cutting
    return answer