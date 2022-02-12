import sys
heights = []

for i in range(9):
    heights.append(int(sys.stdin.readline()))
    
total = sum(heights) # 9명의 키 총 합

one = two = 0
# 2명 씩 짝지어서 탐색하며 거짓 난쟁이 뽑아냄 
# 이 때, 거짓 난쟁이가 몇 번째에 있는지 인덱스 저장해주어야 함!
for i in range(9):
    for j in range(i+1, 9):
        if total - (heights[i]+heights[j]) == 100: #toal-100(진짜 난쟁이들 키의 합)의 결과가 같다면 i와 j번째가 가짜
            one, two = heights[i], heights[j]               
            break #안쪽 반복문 중단하고 탈출


heights.remove(one)
heights.remove(two)
            
heights.sort()

for i in heights:
    print(i)