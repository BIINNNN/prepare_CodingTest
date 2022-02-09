while True:
    #입력 탈출 조건이 따로 명시되어 있지 않음
    # 따라서 try catch문으로 테스트 케이스가 끝나는 경우 실행을 멈출 수 있도록 조건을 걸어줘야 함
    try:
        n = int(input())
    except EOFError:
        break
    
    num = 0
    i = 1 #자리수 카운트
    while True:
        num = 10*num + 1
        num %= n 
        if num == 0:
            print(i)
            break
        i+=1 