#LAB6_1_4
String = input('문자열을 입력하세요 : ')
List = list(String)
count_list = []
dic = dict()
for i in List:
  count_list.append(List.count(i))
for k, v in zip(List, count_list):
  dic[k] = v
print(dic)