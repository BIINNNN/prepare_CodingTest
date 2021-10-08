begin = "hit"
target = "cog"
words=["hot","dot","dog","lot","log","cog"]

def solution(begin, target, words):
    answer = 0
    word_list = [begin]
    dif_list = list()
    if target not in words:
        return 0
    
    while(1):
        for wl in word_list:
            dif_list.clear()
            for word in words: #words안의 글자수 만큼 반복하며 words 모두 훑음
                dif = 0 #차이나는 글자 수(한 글자 차이나는 단어와 교환하기 위해)
                for idx in range(0, len(begin)): #모든 단어의 길이가 같으므로 begin의 단어 길이만큼 잘라서 차이나는 글자수 비교
                    if wl[idx] != word[idx]:
                        dif += 1
                    if dif > 1: #한 개의 알파벳만 바꿀 수 있으므로 2자리가 다르면 반복 멈춤
                        break
                if dif == 1:
                    dif_list.append(word)
                    words.remove(word)

        answer += 1     
        if target in dif_list:
            return answer
        else: 
            word_list = dif_list
                        
result = solution(begin, target, words)
print(result)