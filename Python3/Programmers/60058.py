#입력 문자열 p를 u, v로 분리
#divide 함수의 결과는 더 이상 분리할 수 없어야 함
def divide(p):
    count = [0, 0] #open, close

    for i in p:
        if i == '(':
            count[0] += 1
        else:
            count[1] += 1
        if count[0] == count[1]:
            return p[:sum(count)], p[sum(count):]

#올바른 괄호 문자열인지 확인
def check(u):
    stack = []

    for i in u:
        if i == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    return True

#문제에 주어진 단계대로 구현
def solution(p):
    #입력 문자열이 빈 경우, 빈 문자열 반환
    if not p:
        return ""
    
    u, v = divide(p) #문자열 w를 균형잡힌 괄호 문자열 u, v로 분리

    #문자열 u가 올바른 괄호 문자열이라면
    if check(u):
        #수행 결과 문자열을 u에 이어붙임
        return u + solution(v)
    #문자열 u가 올바른 괄호 문자열이 아니라면
    else:
        #빈 문자열 첫 번째 문자
        answer = '('
        #분자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어붙임
        answer += solution(v)
        #')'를 다시 붙임
        answer += ')'

        #u의 첫 번째와 마지막 문자 제거, 괄호 방향을 뒤집어서 붙임
        for p in u[1:len(u) - 1]:
            #서로 반대로 이어 붙이도록 조건문
            if p == '(':
                answer += ')'
            else:
                answer += '('
        #생성된 문자열 반환
        return answer