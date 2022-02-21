n, m, k = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort() #작은수부터 오름차순 정렬

first = numbers[n-1] #가장 큰 수 
second = numbers[n-2] #두 번째로 큰수
result = 0
    
count = int(m/(k+1))*k
count += m%(k+1) #가장 큰 수가 계산되는 횟수

#가장 큰 수와 두번째로 큰 수가 계산되는 횟수를 곱해주어서 결과값 도출
result += count*first
result += (m-count)*second 

print(result)