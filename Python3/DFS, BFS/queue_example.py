from collections import deque

queue = deque() #큐 구현을 위한 deque 라이브러리 사용

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #첫 번째 원소 삭제
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
#deque 객체를 리스트 자료형으로 변경
print(list(queue))

queue.reverse()

print(queue) #나중에 들어온 원소부터 출력
print(list(queue))
