#정다면체

import sys
sys.stdin = open("D:\input.txt","rt")

n, m = map(int, input().split())

# 정 N면체가 1부터 N까지이기 때문에 아래와 같은 규칙만으로도 구현 가능
# 만약, 각 면의 숫자가 무작위로 되어있다면 합의 결과와 인덱스 번호가 같도록, 그리고 그 인덱스에 해당하는 값은 합의 결과가 나온 횟수를 갖도록 하는 리스트를 생성하고
# 해당 리스트를 돌면서 max값을 갖는 인덱스들을 출력하는 방식으로 구현해야 할 것 같음(예시답안처럼)
if n == m:
    print(n+1)
elif n < m:
    for i in range(n+1, m+2):
        print(i, end=' ')
elif m < n:
    for j in range(m+1, n+2):
        print(j, end=' ')