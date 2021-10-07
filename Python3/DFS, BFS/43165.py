def solution(numbers, target):
    answer=0 
    
    def dfs(idx, result, numbers, target):
        nonlocal answer
        if idx == len(numbers): #마지막 레벨 노드에 도착
            if result == target:
                answer += 1
            return
        else:
            dfs(idx+1, result-numbers[idx], numbers, target) #자식노드 앞에 -붙는 경우
            dfs(idx+1, result+numbers[idx], numbers, target) #자식노드 앞에 +붙는 경우
        
    dfs(0, 0, numbers, target)
    return answer