import csv # подключение библиотеки cvs
with open('magical.csv') as f:
    wr = csv.DictReader(f, delimiter=';')
    data = list(wr)
herbs = {}
for i in data:# получение списка всех трав
    herbs[i['magic_herbs_1']] = 0
    herbs[i['magic_herbs_2']] = 0
    herbs[i['magic_herbs_3']] = 0
for i in data:# подсчет колличества нужных трав
    if i['count'] == '-1':
        herbs[i['magic_herbs_1']] += 1
        herbs[i['magic_herbs_2']] += 1
        herbs[i['magic_herbs_3']] += 1
x = []
for i in herbs:# удаление ненужных трав
    res = {}
    if herbs[i] != 0:
        res['magic_herbs'] = i
        res['count_herbs'] = herbs[i]
        x.append(res)

with open('magicaPotions.csv ', 'w') as f:#создание фалй для записи результата
    wr = csv.DictWriter(f, fieldnames=x[0].keys())
    wr.writeheader()
    for i in x:
        wr.writerow(i)






