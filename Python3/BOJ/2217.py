n = int(input())
weight = []

for i in range(n):
    weight.append(int(input()))

weight.sort(reverse=True) #로프들의 최대 중량부터 차례로 정렬해서 로프가 1개인 경우부터 차례로 최대중량을 구할 수 있도록 함

result = []
for i in range(n):
    result.append(weight[i]*(i+1)) #로프 1~n개 사용할 때 각각의 중량을 구하는 반복문

#여러 경우 중 최대 중량 출력
print(max(result))