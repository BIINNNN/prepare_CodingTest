def solution(brown, yellow):
    answer = []
    
    total = brown + yellow #전체 타일 수
    for y in range(1, total+1):
        if (total%y) == 0:
            x = total/y #total = x*y
            if x >= y: #조건 필터링
                #yellow = (x-2)(y-2)
                #yellow + brown = (x-2)(y-2) + brown = xy
                #(xy-(xy+2x+2y-4)) = brown
                if 2*(x+y-2) == brown: 
                    return[x,y]
        
    return answer