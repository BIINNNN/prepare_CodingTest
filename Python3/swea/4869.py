#import sys
#sys.stdin = open("sample_input.txt", "r")

T = int(input())

def function(N):
    if N%10 == 0:
        if N == 10:
            return 1
        elif N == 20:
            return 3
        else:
            return function(N-10)+2*function(N-20)
    else:
        print("10의 배수를 입력해주세요")

for test_case in range(1, T+1):
    N = int(input())

    result = function(N)
    print("#{} {}".format(test_case, result))