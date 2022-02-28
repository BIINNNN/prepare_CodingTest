#럭키 스트레이트
n = input() #점수 str

left = 0
right = 0
length = len(n)

for i in range(length//2):
    left += int(n[i])
    
for i in range(length//2, length):
    right += int(n[i])
    
if left == right:
    print("LUCKY")
else:
    print("READY")