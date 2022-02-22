#만들 수 없는 금액
n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for i in coin:
    # 다음 코인을 더해서 타겟값을 갱신
    # 이 때, 코인이 타겟보다 크면 중간이 비면서 만들지 못하는 금액이 생기게 되는 것.
    if target < i:
        break
    target += i

print(target)