# 자물쇠와 열쇠 (꼭 다시 혼자 힘으로 풀어보기)
def rotate_matrix_by_90_degree(a):
    n = len(a) # 행 길이
    m = len(a[0]) # 열 길이
    result = [[0]*n for _ in range(m)] # 회전한 결과 담을 리슽
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
            
    return result

# 자물쇠 중간 부분이 모두 1이 되는지 확인 (열쇠로 자물쇠를 열 수 있음을 확인)
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True
            
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    # 열쇠를 올려 비교하기 편하도록 자물쇠를 기존의 3배로 변환
    # 이때, 기존 자물쇠 정보는 중앙에 오도록 함.
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    # 열쇠를 회전할 수 있는 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_matrix_by_90_degree(key) # 90도 회전
        for x in range(n*2):
            for y in range(n*2):
                # 열쇠를 자물쇠에 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                        
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                
                # 자물쇠에서 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
                
    return False