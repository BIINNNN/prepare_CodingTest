def solution(n, computers):
    answer = 0 #리턴 할 값 == 네트워크 개수
    queue = [] #탐색을 위한 큐
    visited = [False for i in range(n)] #방문한 노드 체크할 리스트(시작할때는 모든 노드 방문안 한 상태)
    
    while 0 in visited: #모든 컴퓨터(노드)에 방문할때까지 반복
        x = visited.index(0) #방문하지 않은 노드 추가
        queue.append(x) #첫 노드 방문
        visited[x] = 1 #방문 표시
        
        #bfs 사용
        while queue:
            node = queue.pop(0)
            for i in range(n):
                if visited[i]==0 and computers[node][i]==1: #방문한 적 없고, 인접한 노드라면
                    queue.append(i) #방문하기위해 큐에 집어넣음
                    visited[i] = 1 #방문표시
        answer += 1 #큐 다 돌고나면 연결된 모든 컴퓨터에 방문한 것이므로 네트워크 개수 한 개 증가
    return answer