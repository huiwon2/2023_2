import random
#LAB6_1_2
com = random.randint(1,4)
rps_dic = {1:'가위', 2:'바위', 3:'보'}
match_table={'가위':'보', '바위':'가위', '보':'바위'}

player = input('가위, 바위, 보 입력:')
print('컴퓨터 : {}'.format(rps_dic[com]))
if match_table.get(player) == rps_dic[com]:
  print('당신이 이겼다.')
elif player == rps_dic[com]:
  print('비겼습니다.')
elif match_table.get(rps_dic[com]) == player:
  print('당신이 졌습니다.')
else:
  print('에러')