# K번째 수
def solution(array, commands):
    answer = []
    array_slice = []
    
    for command in commands:
        array_slice = array[command[0]-1 : command[1]]
        array_slice.sort()
        answer.append(array_slice[command[2]-1])
        
    return answer