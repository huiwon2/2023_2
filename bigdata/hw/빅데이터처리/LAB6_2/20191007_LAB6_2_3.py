# LAB6_2_3
price = [5000, 3000, 10000, 8000, 2000]
discount = [float(i*0.2) for i in price]
for i in discount:
  print('{:.1f}'.format(i))