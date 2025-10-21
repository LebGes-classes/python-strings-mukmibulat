text = input('Введите текст: ')

line_reversed=''
words_repository = ''
symbols_reversed = ''
word=''

for j in range(len(text)-1, -1, -1):
    if text[j]==' ':
        line_reversed+=word+' '
        word=''
    else:
        word=text[j]+word

    if j==0:
        line_reversed+=word
        word=''

print(line_reversed)

for i in range(len(text)):
    if text[i] != ' ':
        words_repository += text[i]
    else:
        for j in range(len(words_repository)):
            symbols_reversed += words_repository[-j - 1]
        symbols_reversed += ' '
        words_repository = ''

    if i == len(text) - 1:
        for j in range(len(words_repository)):
            symbols_reversed += words_repository[-j - 1]

print(symbols_reversed)