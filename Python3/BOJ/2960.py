n, k = map(int, input().split()) #2~n까지의 정수, k번째에 지워진 수를 구하는 것이 문제

cnt = 0

nums = [False]*(n+1) #숫자를 제거했는지 확인하기 위한 리스트

for i in range(2, len(nums)+1):
    for j in range(i, n+1, i):
        if nums[j] == False:
            nums[j] = True #제거했으면 True로 변경
            cnt += 1
            if cnt == k: #k번째가 되면 
                print(j) #결과 출력
                break

