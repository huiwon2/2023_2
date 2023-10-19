#LAB5_2
img = input("이미지 이름 입력 : ")
list1 = img.split('.')
if list1[1] == 'jpg':
  print('jpg 형식의 이미지 파일입니다.')
else:
  print('jpg 형식의 이미지 파일이 아닙니다.')