from itertools import permutations

def prime_number(x):
    if x<2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False #소수 아님
    return True #소수임

def solution(numbers):
    answer = 0
    array = [] #숫자 조합 저장할 배열
    
    #숫자 이용해서 가능한 숫자 순열 만들기 위해 permutation 사용
    for i in range(1, len(numbers)+1): #1자리 숫자 조합 부터 number 개수의 자리만큼 숫자 조합
        temp = permutations(numbers, i) #튜플 조합으로 출력됨
        for n in temp:
            #튜플을 문자열로 합침
            temp_str = "".join(n)
            #문자열을 int형으로 변환
            array.append(int(temp_str))
    #중복 제거
    array = list(set(array))
    
    #중복 제거된 숫자 조합에서 소수 판별
    for number in array:
        if prime_number(number):
            answer +=1
        else:
            continue
            
    return answer