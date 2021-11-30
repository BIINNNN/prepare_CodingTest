test_case = int(input()) 

for _ in range(test_case):
    n , m = list(map(int,input().split(' ')))
    queue = list(map(int,input().split(' ')))
    idx_queue = list(range(len(queue)))
    count = 0 
    
    while True:
        if queue[0] == max(queue):
            count += 1
            
            if idx_queue[0] == m:
                print(count)
                break
            else:
                queue.pop(0)
                idx_queue.pop(0)
        else:
            queue.append(queue.pop(0))
            idx_queue.append(idx_queue.pop(0))