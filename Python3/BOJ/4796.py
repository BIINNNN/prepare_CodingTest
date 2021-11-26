#케이스 순서 저장 변수
case = 1

while True:
  l, p, v = map(int, input().split())
  result = 0
  
  #l+p+v가 0일경우 종료
  if l+p+v == 0:
    break
  
  result = l*(v//p) + min((v%p), l)
  print("Case {}: {}".format(case, result))
  case += 1