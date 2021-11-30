cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in cro:
    word = word.replace(i, '*') #cro에 있는 알파벳 찾아서 word에서 바꿈 
    
print(len(word))