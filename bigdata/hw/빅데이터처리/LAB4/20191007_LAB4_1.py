#LAB4_1
def game369(num):
  if num < 10:
    if num == 3 or num == 6 or num == 9:
      return "짝"
  elif num >= 10:
    if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
      return "짝"
  return num

for i in range(1, 50):
  print(game369(i), end=' ')