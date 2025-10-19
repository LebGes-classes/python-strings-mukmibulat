text = input('Введите текст: ')
ntt=''
nt = ''
st = ''
word=''
for j in range(len(text)-1, -1, -1):
    if text[j]==' ':
        ntt+=word+' '
        word=''
    else:
        word=text[j]+word
    if j==0:
        ntt+=word
        word=''
print(ntt)

for i in range(len(text)):
    if text[i] != ' ':
        nt += text[i]
    else:
        for j in range(len(nt)):
            st += nt[-j - 1]
        st += ' '
        nt = ''

    if i == len(text) - 1:
        for j in range(len(nt)):
            st += nt[-j - 1]
print(st)