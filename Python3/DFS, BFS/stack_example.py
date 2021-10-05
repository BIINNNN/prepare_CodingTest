stack = [] #스택연산을 위한 배열 생성

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() #삭제
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #최하단의 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력