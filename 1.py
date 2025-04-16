import random
s,k=0,0
a=['left','right','center']
while True:
    n=input('Tanlovni kiriting(left,right,center,stop)')
    m=random.choice(a)
    if n=='stop':
        break
    if n==m:
        s+=1
        print(f"Siz {n} tomonga tepdingiz va darvozabon ham {m} tomonga sakradi; top qaytarildi❌")
    elif n!=m and n in a:
        k+=1
        s+=1
        print(f"Siz {n} tomonga tepdingiz darvozabon {m} tomonga sakradi gol bo'ldi⚽✔")
    else:
        print('Faqat [left,right,center] tomonlarga tepishingiz yoki stop tugmasi orqali to\'xtatishimgiz mumkin')
    if s==10:
        break
print(' ')
print(f'{k} ta gol urdingiz⚽✔ va {s-k} ta urolmadingiz❌')
