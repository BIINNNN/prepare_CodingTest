begin = "hit"

word_list = [begin]
print(word_list)
for wl in word_list:
    i = 1
    for idx in range(0,len(begin)):
        print(idx)
        print(wl[idx])