numbers = set(range(1, 10000))
remove = set()  #생성자가 있는 숫자 set

for num in numbers :
    for i in str(num):
        num += int(i)
    remove.add(num)  #add: 집합에 요소를 추가할 때

self_numbers = numbers - remove  #set의 '-' 연산자로 차집합을 구함

for self_num in sorted(self_numbers):  #sorted 함수로 정렬
    print(self_num)