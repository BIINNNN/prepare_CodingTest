def solution(genres, plays):
    answer = []
    temp = [] # [장르, 재생횟수, 고유번호] 형태 1차 저장 리스트
    genre_cnt = {} # 장르별로 나누어 재생 횟수를 저장히기 위한 딕셔너리 (key : 장르, value : 장르 총 재생 횟수)

    temp = [[genres[i], plays[i], i] for i in range(len(genres))] 
    # 기준 2 : 장르 내에서 많이 재생된 노래를 먼저 수록
    # 기준 3 : 장르 내에서 재생 횟수가 같으면 고유 번호가 낮은 노래 먼저 수록
    temp = sorted(temp, key = lambda x: (x[0], -x[1], x[2]))
    
    # 장르별로 딕셔너리 채우기
    for x in temp:
        if x[0] not in genre_cnt:
            genre_cnt[x[0]] = x[1]
        else:
            genre_cnt[x[0]] += x[1] # 기존 키값에 재생 횟수 추가
    
    # 기준 1 : 속한 노래가 많이 재생된 장르를 먼저 수록
    genre_cnt = sorted(genre_cnt.items(), key = lambda x : -x[1])

    # 한 장르 내에선 최대 2개씩 수록
    for i in genre_cnt:
        cnt = 0
        for j in temp:
            if i[0] == j[0]:
                cnt += 1
                if cnt <= 2:
                    answer.append(j[2])
                else:
                    break
        
    return answer