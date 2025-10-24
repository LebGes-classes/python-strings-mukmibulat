text=input('Введите текст: ')

down_letters='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
up_letters='ABCDEFGHIJKLMNOPGRSTUVWXYZABCDEFGHIJKLMNOPGRSTUVWXYZ'

word=''
code_word=''

point=0
K=0

for i in range(len(text)):
    if text[i]==',' or text[i]=='.' or text[i]==', ':
        if len(word)>K:
            K=len(word)
            code_word=word
        word=''
    else:
        word+=text[i]

transformered_string=''

if len(code_word)<=20:
    for symbol in text:
        if symbol in down_letters:
            for j in range(len(down_letters)//2):
                if down_letters[j]==symbol:
                    transformered_string+=down_letters[j+K]
        elif symbol in down_letters:
            for j in range(len(up_letters)//2):
                if [j]==symbol:
                    transformered_string+=up_letters[j+K]
        else:
            transformered_string+=symbol
    print(transformered_string,K)
else:
    print('The maximum number of characters allowed is 20! Please re-enter the text.')