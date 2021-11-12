def solution(n):
    answer = ''
    num = ['4','1','2']
    
    while n > 0:
        answer += num[n%3]
        if n % 3 == 0: #3으로 나누어 떨어지면
            n -= 1 #124 나라의 4는 숫자 3과 같이 연산(실제 연산은 3이므로 -1 해주는 것)
        n //=3
    
    answer = answer[::-1] #순서 역순으로
    return 