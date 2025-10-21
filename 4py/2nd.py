text=input('Введите текст: ')

down_letters=2*'abcdefghijklmnopqrstuvwxyz'
up_letters=2*'ABCDEFGHIJKLMNOPGRSTUVWXYZ'

word=''
code_word=''

point=0
K=0

for i in range(len(text)):
    if text[i]=='.':
        point+=1
    if text[i]==',' or text[i]=='.' or text[i]==', ':
        if len(word)>K:
            K=len(word)
            code_word=word
        word=''
    else:
        word+=text[i]

transformered_string=''

if point==0:
    print('This text does not contain a period! You must rewrite the text, adding only a single period at the end.')
elif point==2:
    print('This text contains more than two periods! You must rewrite the text, adding only a single period at the end.')
elif len(code_word)<=20:
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
            transformered_string+=s
    print(transformered_string,K)
else:
    print('The maximum number of characters allowed is 20! Please re-enter the text.')