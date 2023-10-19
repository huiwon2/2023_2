#LAB5_5
numlist = []
while True:
  num = int(input('수를 입력하세요(-1 입력 시 입력 끝) : '))
  if num == -1:
    break
  else:
    numlist.append(num)
key = int(input('찾고 싶은 수를 입력하세요: '))
for i in range(len(numlist)):
  if key == numlist[i]:
    print('찾는 값의 위치 : {}'.format(i))
    break
if key != numlist[len(numlist)]:
  print('찾는 값이 없습니다.')