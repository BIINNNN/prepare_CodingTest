n = int(input())
students = []
for i in range(n):
    students.append(input().split())
    
# 국어(students의 두 번째 원소) : 내림차순 (감소)
# 영어(students의 세 번째 원소) : 오름차순 (증가)
# 수학(students의 네 번째 원소) : 내림차순 (감소)
# 이름(students의 첫 번째 원소) : 오름차순 (증가)

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0]) # 이름만 출력