# LAB6_2_4
names = ['신짱구', '김철수', '맹구', '유리']
pythons = [100, 90, 60, 90]
java = [90, 98, 70, 80]
c = [97, 89, 60, 91]

scores_total = [sum(x) for x in zip(pythons, java, c)]
scores_average = [sum(x) / 3 for x in zip(pythons, java, c)]
result = ['합격' if avg >= 80 else '불합격' for avg in scores_average]

Grade = list(zip(names, scores_total, scores_average, result))
print(Grade)