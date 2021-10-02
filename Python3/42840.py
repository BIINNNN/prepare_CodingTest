def solution(answers):
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    
    for idx, answer in enumerate(answers):
        if answer == supo1[idx%len(supo1)]:
            score[0] += 1
        if answer == supo2[idx%len(supo2)]:
            score[1] += 1
        if answer == supo3[idx%len(supo3)]:
            score[2] += 1
            
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
            
    return result