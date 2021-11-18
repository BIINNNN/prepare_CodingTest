n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
idx = k - 1 #원을 도는 주기 
answer = []

for i in range(n):
    if len(arr) > idx:
        answer.append(arr.pop(idx)) #해당 주기의 인덱스 값 제거 
        idx += (k - 1) #idx번째 수 제거된 후이고, k-1만큼 다음수가 시작됨으로 새롭게 리셋
        
    elif len(arr) <= idx: #한 바퀴를 다 돌아서 리스트 인덱스를 넘기는 경우
        idx = idx % len(arr) #주기로 나눈 나머지를 인덱스로 하는 값을 찾아서 제거하도록 함
        answer.append(arr.pop(idx))
        idx += k -1
        
print("<"+', '.join(map(str, answer))+">", sep = '')