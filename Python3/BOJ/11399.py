n = int(input()) #사람의 수
pi = list(map(int, input().split())) #각 사람이 인출하는 데 걸리는 시간

#(본인이 중간즈음 있다고 가정 할 때) 앞 사람이 빨리 인출할수록 내 대기시간 짧아짐
# 따라서 돈을 뽑는 시간이 짧은 사람부터 앞에 오도록 하면 평균 대기 시간이 단출 됨
pi.sort()

time = 0
result = 0
#wait_list = []
for i in range(n):
    time += pi[i]
    result += time #대기시간 계속해서 더해줌

print(result)