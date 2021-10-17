#import sys
#sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    string = str(input())
    arr = list(string)
    result = 1
    stack = []

    for i in range(0, len(arr)):
        if arr[i] == '(' or arr[i] == '{':  # 만약 ( or { 가 나오면
            stack.append(arr[i])  # stack에 추가
        elif arr[i] == ')' or arr[i] == '}':  # ) or } 가 나왔을때
            if not stack:  # 스택에 아무것도 없을 경우
                result = 0
                break  # 여는 괄호 없이 닫히는 괄호만 나왔으므로 잘못된 것

            P = stack.pop()
            if arr[i] == ')' and P != '(':  # )가 나왔을 때, 스택에서 꺼낸 괄호가 맞지 않을 경우
                result = 0
            elif arr[i] == '}' and P != '{':  # }가 나왔을 때, 스택에서 꺼낸 괄호가 매칭되지 않을 경우
                result = 0
    if stack:  # 반복문을 다 돌았는데, 스택에 남은것이 있는 경우
        result = 0  # 짝이 맞지 않는 것이므로 잘못된 것

    print("#{} {}".format(test_case, result))