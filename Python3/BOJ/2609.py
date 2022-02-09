a, b = map(int, input().split())

def gcd(a, b):
    while b > 0: #나머지가 0이 되는 순간 반복 멈춰야 함
        a, b = b, a%b
    return a #최대공약수 a = 두 수 나누기의 나머지가 0이 되는 순간, 나누는 수 (b가 a로 switch 되므로 a를 리턴)

def lcm(a, b):
    return a*b // gcd(a,b) # 두 수의 곱을 최대공약수로 나누면 최소공배수가 됨.

print(gcd(a, b))
print(lcm(a, b))