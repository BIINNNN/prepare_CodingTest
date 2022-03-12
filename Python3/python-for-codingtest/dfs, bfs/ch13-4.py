# 괄호 변환
def solution(p):
    answer = ''
    if isCorrect(p): 
        return p
    
    answer = rep(p)
    
    return answer

# (u, v 분리)
# 2단계
# u는 더이상 분리할 수 없어야 함 = 최소단위
def sep_uv(p):    
    open_cnt, close_cnt = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            open_cnt += 1
        else:
            close_cnt += 1
        if open_cnt == close_cnt: # 여는 괄호와 닫는 괄호의 개수가 같아지면 균형 맞는 것 => 최소를 맞춰야 하므로 개수로 비교 가능
            u = p[:i+1]
            v = p[i+1:] if i+1 < len(p) else "" # v는 빈 문자열도 가능하기 떄문에 out of index 오류 방지하기 위해 길이 비교 후, 빈 문자열 v에 할당
            break
    return u, v
    
# 3단계
# 올바른 괄호 문자 판별 - 올바른 괄호 문자일 경우
def isCorrect(p):
    stack = []
    for c in p:
        if c == '(': # 문자열 p를 순회하면서 여는 괄호를 만나면 스택에 저장. 
            stack.append(c)
        else: # 닫는 괄호를 만나는 경우, 
            if not len(stack): # 스택이 비어있다면 배치 순서에 따른 짝이 맞지 않는 상황이므로 올바르지 않은 괄호 문자열
                return False
            elif stack[-1] == '(': # 스택에 여는 괄호가 있다면
                stack.pop() # pop 해서 짝 제거
    return False if len(stack) else True # 마지막까지 진행했을 때, 스택 비었다면 올바른 문자열, 그렇지 않다면 짝이 안맞는 것이므로 False

# 전체 단계 재귀적으로 반복
def rep(p):
    result = ""
    if not len(p): 
        return "" # 1단계 - 입력이 빈 문자열인 경우, 빈 문자열 반환
    
    u,v = sep_uv(p) # 2단계 수행
    
    if isCorrect(u): # 3단게 수행
        result = u + rep(v) # 3-1 수행
    else: # 4단계
        tmp = "(" # 4-1 수행
        tmp += rep(v) # 4-2 수행
        tmp += ")" # 4-3 수행
        u = u[1:-1] # 4-4 수행 - 첫 번째와 마지막 문자 제거
        for c in u: # 4-4 수행 - 반복문으로 순회하며 나머지 괄호 방향을 뒤집음
            if c == '(':
                tmp+=')'
            else:
                tmp+='('
        result += tmp
    return result # 4-5 수행