#LAB5_6
Str1 = 'You said some winds blow forever and I didn\'t understand'
list_str = Str1.split(' ')
list_del = ['some', 'forever']
list_str.remove('some')
list_str.remove('forever')
print('원본 문자열 : {}'.format(Str1))
print('삭제 단어들 : {}'.format(list_del))
print('삭제 후 남은 단어들 : {}'.format(list_str))