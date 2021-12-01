n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
index = 0

print("<", end='')

while len(arr) > 1:
    index += k
    if index > len(arr):
        index = index % len(arr)
        if index == 0:
            index += len(arr)
    
    index -= 1
    print(str(arr.pop(index)), end=", ")
    
print("{}>".format(str(arr.pop())))