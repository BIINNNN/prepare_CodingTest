#성적이 낮은 순서로 학생 출력하기
import sys
sys.stdin = open("D:\input.txt", "rt", encoding='UTF8')

n = int(input())

arr = []
for i in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))
    
arr = sorted(arr, key = lambda student: student[1])

for student in arr:
    print(student[0], end=' ')