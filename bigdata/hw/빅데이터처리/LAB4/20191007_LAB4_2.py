#LAB4_2
def BMI(height, weight):
  bmi = weight / height ** 2
  print("당신의 체지방지수는 {:.2f} 입니다".format(bmi))
  return bmi
def result_print(result):
  if result < 18.5:
    print("당신은 저체중입니다")
  elif result <= 22.9:
    print("당신은 정상입니다.")
  elif 23 <= result <= 24.9:
    print("당신은 과체중입니다.")
  elif 25 <= result <= 29.9:
    print("당신은 경도비만입니다.")
  else:
    print("당신은 고도비만입니다.")

h = float(input('키를 m단위로 입력: '))
w = float(input('몸무게를 kg 단위로 입력: '))
result = BMI(h,w)
result_print(result)