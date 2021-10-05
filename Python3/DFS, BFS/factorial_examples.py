#팩토리얼을 반복적으로 구현
def factorial_iterative(n):
    result = 1
    #1~n까지의 수를 차례로 곱하기
    for i in range(1, n+1):
        result *= i #1*2*3*4*5
    return result

#팩토리얼을 재귀함수로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n*factorial_recursive(n-1) #5*4*3*2*1

print('n!을 반복적으로 구현 : ', factorial_iterative(5))
print('n!을 재귀적으로 구현 : ', factorial_recursive(5))