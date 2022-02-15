n = int(input())

n_length = len(str(n))

count = 0

for i in range(1, n_length):
    count += 9*10**(i-1)*i
    
result = count + (n-(10**(n_length-1))+1)*n_length

print(result)