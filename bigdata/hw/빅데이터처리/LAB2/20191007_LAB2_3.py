#LAB2_3
name = input('Enter the name : ')
age = int(input('Enter {}\'s age : '.format(name)))
if age < 10 :
  print('{}은 0대이다.'.format(name))
elif age < 20:
  print('{}은 10대이다.'.format(name))
elif age < 30:
  print('{}은 20대이다.'.format(name))
elif age < 40:
  print('{}은 30대이다.'.format(name))
elif age < 50:
  print('{}은 40대이다.'.format(name))
else:
  print('{}은 50대이다.'.format(name))