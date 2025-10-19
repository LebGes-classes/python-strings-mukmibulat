text=input()
aa=2*'abcdefghijklmnopqrstuvwxyz'
AA=2*'ABCDEFGHIJKLMNOPGRSTUVWXYZ'
w=''
code_word=''
K=0
for i in range(len(text)):
    if text[i]==',' or text[i]=='.' or text[i]==', ':
        if len(w)>K:
            K=len(w)
            code_word=w
        w=''
    else:
        w+=text[i]

nt=''
for s in text:
    if s in aa:
        for j in range(len(aa)//2):
            if aa[j]==s:
                nt+=aa[j+K]
    elif s in aa:
        for j in range(len(AA)//2):
            if AA[j]==s:
                nt+=AA[j+K]
    else:
        nt+=s
print(nt,K)