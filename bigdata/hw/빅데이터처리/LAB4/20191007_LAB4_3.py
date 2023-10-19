#LAB4_3
def average(*args):
  sum = 0
  print('매개변수로 전달된 값 : ', end=' ')
  for i in range(len(args)):
    print(args[i], end=' ')
    sum += args[i]
  average = sum / len(args)
  print()
  return average
print("평균: ", average(1, 2, 3, 4, 5))
print("-" * 40)
print("평균: ", average(30, 10, 20))