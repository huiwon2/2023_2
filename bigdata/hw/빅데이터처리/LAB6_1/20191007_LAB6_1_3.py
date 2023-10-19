#LAB6_1_3
items ={'커피':7, '펜':3, '종이컵':2, '우유':1, '콜라':4, '책':5}
print("-----재고관리-----")
print("1. 모든 상품 재고수량 관리")
print("2. 특정 상품 재고수량 관리")
print("3. 상품 판매")
print("4. 상품 입고")
print("5. 종료")
print()

while True:
  print('-'*15)
  menu = int(input('메뉴 입력 : '))
  if menu == 1:
    for k, v in zip(items.keys(), items.values()):
      print('{} : {}개'.format(k, v))
  elif menu == 2:
    name = input('상품명 입력 : ')
    print('재고 수량: {}'.format(items.get(name, '상품명 입력 오류')))
  elif menu == 3:
    sell_name = input('판매 상품명 입력 : ')
    sell_num = int(input('판매 수량 입력 : '))
    if sell_num > items.get(sell_name):
      print('상품이 부족합니다.')
    else:
      items[sell_name] = items.get(sell_name, 0) - sell_num
  elif menu == 4:
    sale_name = input('입고 상품명 입력 : ')
    sale_num = int(input('입고 수량 입력 : '))
    items[sale_name] = items.get(sale_name, 0) + sale_num
  else:
    break