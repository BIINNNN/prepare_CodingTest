# 특정 거리의 도시 찾기
import sys
input = sys.stdin.readline

from collections import deque

n, m, k, x = map(int, input().split())

cities = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    cities[a].append(b) # 도시의 모든 거리 정보 입력받아서 저장. (a에서 b로 단방향 연결)
    
# 모든 도시의 최단 거리 초기화 (방문 여부 확인 가능한 리스트)
distance = [-1]*(n+1) # 1~N번 도시 번호에 맞춤 / 방문 전에는 -1로 초기화
distance[x] = 0 # 출발 도시

q = deque([x])
while q: # 큐에 남는 것이 없을 때까지
    now = q.popleft() # 처음 들어온 곳부터 빠져야 함.
    # 현재 도시(now)에서 이동 가능한 모든 도시 탐색
    for next_city in cities[now]:
        if distance[next_city] == -1: # 아직 방문하지 않은 도시라면
            distance[next_city] = distance[now] + 1 # 출발도시로부터 모든 도시까지의 거리를 계산하도록 함
            q.append(next_city)
            
check = False
# 모든 도시 중 출발도시로부터의 최단거리가 k인 도시만 골라내서 출력 (1번 도시부터 골라내기 때문에 오름차순으로 출력되게 됨)
for i in range(1, n+1):
    if distance[i] == k:
        check = True
        print(i)
        
if check == False:
    print(-1)