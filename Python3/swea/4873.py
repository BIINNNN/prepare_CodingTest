import sys
sys.stdin = open("sample/input_4873.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    s = list(str(input())) #주어지는 문자열 s

    stack = [s[0]] # 연속된 문자를 삭제한 문자열을 저장할 스택, 입력받은 문자열의 첫 번째 문자를 저장

    for i in range(1, len(s)): #첫 번째 문자는 이미 들어간 상태이므로, 인덱스 1부터 시작
        if not stack: #stack에 아무것도 없는 예외 상황 대비
            stack.append(s[i])
        elif stack[-1]==s[i]: #stack의 top과 다음 문자가 같은 경우
            stack.pop() #스택에서 문자 중복되는 문자 제거
        else: #stack의 top과 다음 문자가 다른 경우
            stack.append(s[i])

    print("#{} {}".format(test_case, len(stack)))
