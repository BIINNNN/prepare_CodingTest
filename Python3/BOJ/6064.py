t = int(input())

def cal(m, n, x, y):
    # 마지막해는 m, n의 최소공배수가 되는 해이므로 최대가 되는 상황은 m*n 이므로
    while x <= m*n:
        if (x-y)%n == 0:
            return x
        x += m
    return -1

for i in range(t):
    m, n, x, y = map(int, input().split())
    print(cal(m, n, x, y))