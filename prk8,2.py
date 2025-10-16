import random
n=int(input("введіть кількість рядків: "))
for i in range(n):
    l=input("введіть рядок: ")
    if len(l)%3!=0:
        print("помилка")
    l1=len(l)//3
    p=[l[:l1], l[l1:2*l1], l[2*l1:]]
    random.shuffle(p)
    P=''.join(p)
    print('',P)
