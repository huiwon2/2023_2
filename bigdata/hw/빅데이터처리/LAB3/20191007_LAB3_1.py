#LAB3_1
import random
print('<<덧셈 연습 게임>>')
print('-' * 20)

answer_count = 0
count = 0
while True:
  random1 = random.randint(10,100)
  random2 = random.randint(10,100)
  answer = int(input('{} + {} = '.format(random1, random2)))
  sum = random1 + random2
  if answer == sum:
    print('맞았다!')
    answer_count += 1
    count += 1
  else:
    print('틀렸다!')
    count += 1
  
  if answer_count == 5:
    break
print('시도횟수 : {}'.format(count))
