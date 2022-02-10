n = int(input())
result = 0

# 배수의 개념으로 풀어야 함.
for i in range(1, n+1):
    result += (n//i)*i #1~n까지 수의 약수를 구하는과정에서 i가 약수로 몇 번 나오는지를 이용

print(result)

# 약수 이용하면 시간초과 뜸....

# def get_divisor_sum(n):
#     divisors_front = []
#     divisors_back = []
#     divisors = []
#     div_sum = 0

#     for i in range(1, int(n**(1/2))+1):
#         if(n%i == 0): #나누어 떨어지면 약수
#             divisors_front.append(i)
#             if (i != n//i): #중복되는 값으로 나오는 약수가 아니면 (ex.25 = 5*5에서 5)
#                 divisors_back.append(n//i)
#     divisors = divisors_front+divisors_back[::-1]

#     for i in range(len(divisors)):
#         div_sum += divisors[i]

#     return div_sum

# for i in range(1, n+1):
#     result += get_divisor_sum(i)

# print(result)