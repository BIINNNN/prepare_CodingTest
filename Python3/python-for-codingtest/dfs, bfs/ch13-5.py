# 연산자 끼워 넣기
n = int(input())

numbers = list(map(int, input().split()))
add, sub, mul, div  = map(int, input().split()) # 각 연산자의 개수

max_res = -1e9
min_res = 1e9

# DFS

def dfs(idx, now_res): 
    global max_res, min_res, add, sub, mul, div

    # 모든 연산자를 다 사용한 후에 최댓값과 최솟값 결과를 변수에 업데이트 하도록 함.
    # 연산자는 항상 n보다 1작은 개수가 존재. dfs(1, numbers[0])에서 시작하므로 idx==n이 되는 순간ㅇ; 모든 연산자를 다 사용한 순간이 됨.
    if idx == n:
        max_res = max(max_res, now_res)
        min_res = min(min_res, now_res)

    else: # 사용할 연산자 남은 경우라면 각 연산자에 대하여 재귀적 수행
        if add > 0:
            add -= 1 # 사용
            dfs(idx+1, now_res + numbers[idx])
            add += 1 # 각 경우에 대해 확인하고 다시 원래대로 돌려놔야 연산자 배치가 다른 경우에 대해서도 확인 가능
            
        if sub > 0:
            sub -= 1 # 사용
            dfs(idx+1, now_res - numbers[idx])
            sub += 1
            
        if mul > 0:
            mul -= 1
            dfs(idx+1, now_res * numbers[idx])
            mul += 1
            
        if div > 0:
            div -= 1
            # 나누기를 수행할 때 중요한 점은 // 연산자가 아닌 / 연산자를 사용해서 계산한 후, int 형으로 바꾸는 방법을 사용해야 한다는 점.
            # 파이썬에서 // 연산자는 항상 내림을 해준다. 그래서 음수 나눗셈을 할 경우 -3 // 2 == -2 와 같은 결과가 나온다. 
            # 그러나 문제에서 C++14의 기준을 따른다고 명시되어 있다. 이런 경우 -3 / 2 == -1 와 같은 결과가 만들어진다.
            # 따라서 위의 기준대로 파이썬에서 결과를 만들기 위해서는 int(-3 / 2) == int(-1.5) == -1 의 방식으로 계산되도록 구현해야 올바른 답을 구할 수 있다.  
            dfs(idx+1, int(now_res / numbers[idx])) # 나머지 제거
            div += 1
        
dfs(1, numbers[0])            

print(max_res, min_res, sep='\n')