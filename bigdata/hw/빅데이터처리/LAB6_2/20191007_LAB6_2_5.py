# LAB6_2_5
list_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f_odd = lambda x:x % 2 == 1
f_even = lambda x:x % 2 == 0
list_odd = list(filter(f_odd, list_original))
list_even = list(filter(f_even, list_original))

print('원래 리스트 : {}'.format(list_original))
print('짝수 리스트 : {}'.format(list_even))
print('홀수 리스트 : {}'.format(list_odd))