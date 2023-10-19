#LAB6_1_1
english_dict = {}

english = ['one', 'two', 'three', 'four', 'five']
korean = ['하나', '둘', '셋', '넷', '다섯']
for k, v in zip(english, korean):
  english_dict[k] = v
print('three의 뜻은 {}이다.'.format(english_dict.get('three')))