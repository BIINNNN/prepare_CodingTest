def solution(genres, plays):
    answer = []
    songs = len(genres)  #주어진 곡의 개수
    total = {}  #genres와 plays를 저장할 딕셔너리

    for i in range(songs):  #곡의 개수만큼 각 인덱스에 접근
        #total의 key에 genre가 없는 경우
        if genres[i] not in total.keys():
            total[genres[i]] = {'total': plays[i], i: plays[i]}
        #genre가 key로 존재하는 경우
        else:
            total[genres[i]]['total'] += plays[i]
            total[genres[i]][i] = plays[i]  #곡 번호에 plays[i] 입력

    sorted_genres = sorted(total.items(), key=lambda x: x[1]['total'], reverse=True)  #각 genre의 하위 딕셔너리의 total key를 기준으로 내림차순 정렬

    for j in range(len(sorted_genres)):
        genre_dict = sorted_genres[j][1]  #각 장르의 딕셔너리 가져옴
        sorted_songs = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)  #value 기준 내림차순 정렬

        k = 1
        while k <= 2:
            answer.append(sorted_songs[k][0])
            if (len(sorted_songs) < 3):
                break
            k += 1
    return answer