t = int(input())

cases = [int(input()) for _ in range(t)]

maxnum = max(cases)

dp = [1, 2, 4] 

for i in range(3, maxnum+1):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])
    
for case in cases:
    print(dp[case-1])