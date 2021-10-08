tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets_2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets):
    answer = []
    routes = dict()

    for (start, end) in tickets: #ticket을 통해 인접그래프를 딕셔너리 형태로 생성
        routes[start] = routes.get(start, []) + [end] #출발지를 key값으로, 도착지를 value로 해서 묶음

    for arv in routes.keys(): #value들을 역순으로 정렬
        routes[arv].sort(reverse=True)
    
    #DFS로 탐색해서 경로(path) 결정
    stack  = ['ICN'] #문제에서 출발은 항상 ICN이라고 지정해줌
    path = [] #스택에서 pop 시킨 것을 path에 저장

    while stack: #스택이 빌 때까지 반복
        top = stack[-1] #스택에서 삭제하지 않고 일단 스택의 가장 위에 있는 값만 가져옴

        if top not in routes or len(routes[top]) == 0: #top을 출발지로 하는 곳이 없거나, 그래프에 top이 없는 경우
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1]) #top을 출발지로 하는 도착지 중에서 가장 마지막 지점을 꺼내서 스택에 저장
            routes[top] = routes[top][:-1]

 
    answer = path[::-1] #완성된 경로는 도착지부터 쌓여있으니 뒤집어 출력
    return answer

result = solution(tickets)
print(result)