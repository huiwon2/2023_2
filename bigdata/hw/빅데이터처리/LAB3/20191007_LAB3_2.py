#LAB3_2
sum = 0
for i in range(1,101):
  if i % 5 == 0:
    continue
  else:
    sum += i
print(sum)