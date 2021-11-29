k = int(input()) #입력받을 스택 안 숫자의 개수
numbers = [] #숫자 입력받을 스택 

for i in range(k):
    num = int(input())
    if (num==0): #숫자 잘못 불렀을 때 삭제 해야함을 의미
        numbers.pop() #리스트에서 숫자 삭제
    else:
        numbers.append(num) #해당 턴의 숫자를 스택에 추가
    
print(sum(numbers))