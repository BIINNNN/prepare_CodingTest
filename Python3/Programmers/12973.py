def solution(s):
    stack = []

    for i in range(len(s)):
        # stack이 비어있다면
        if not stack:
            stack.append(s[i])
        # stack에 값이 있을 때
        else:
            # stack의 마지막 값과 s[i]가 같은 경우 해당 값을 꺼냄
            if stack[-1] == s[i]:
                stack.pop()
            # stack의 마지막 값과 s[i]가 다른 경우 s[i]를 stack에 넣음
            else:
                stack.append(s[i])

    # stack에 남은 값이 있는 경우 성공적인 짝짓기가 이루어지지 않은 것
    if stack:
        return 0
    else:
        return 1