def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    # 사전값으로만 정렬하면 입출력 예 두 번째의 3, 30 같은 경우 3이 먼저 나와야 하는데 30이 먼저 나오게 됨.
    # 따라서 이런 문제를 해결하기 위해 number가 1000이하의 숫자임을 고려해(최댓값 생각) 3을 곱해줘서 333, 303030의 형태로 만들어 줌.
    # 그런 다음 정렬해주면 333, 303030순서로 정렬(내림차순)되어서 3이 30보다 앞에 나오게 됨.
    numbers.sort(key=lambda x:x*3, reverse=True) 
    answer = str(int(''.join(numbers)))
    
    return answer