text = input('Введите текст: ')

up_letters='ABCDEFGHIJKLMNOPGRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
down_letters='abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

low_text=''
for s in text:
    for i in range(52):
        if s == up_letters[i]:
            low_text+=down_letters[i]
            break
    else:
        low_text+=s

splited_text=[]
word=''
for i in range(len(low_text)):
    if low_text[i]==' ':
        if word!='':
            splited_text.append(word)
            word=''
    else:
        word+=low_text[i]
if word!='':
    splited_text.append(word)

list=[]
for word in splited_text:
    word_count = [word, splited_text.count(word)]
    if word_count not in list:
        list.append(word_count)

length_of_list = len(list)

for i in range(len(list)):
    for j in range(0, len(list)-i-1):
        if list[j][1] == list[j+1][1]:
            if len(list[j][0]) < len(list[j+1][0]):
                list[j], list[j+1] = list[j+1], list[j]
        elif list[j][1] < list[j+1][1]:
            list[j], list[j+1] = list[j+1], list[j]


print(list)

print('Топ самых встречающихся слов: ')

if length_of_list < 5:
    for i in range(length_of_list):
        print(f'{i+1}:', 'Слово:', list[i][0], ' | ', 'Количество повторений:', list[i][1])
else:
    for i in range(5):
        print(f'{i+1}:','Слово:', list[i][0], ' | ', 'Количество повторений:', list[i][1])