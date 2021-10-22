def solution(phone_book):
    answer = True

    # 오름차순 정렬하면 번호가 중복으로 시작하는 경우 길이가 짧은 단어가 앞으로 옴
    # ex) 1235, 123, 12348, 012 => 012, 123, 12348, 1235
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
            return False

    return answer