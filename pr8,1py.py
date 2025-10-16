import math
s1=input("введіт список:")
suma=0
dobytok=1
dg= False
for s in s1:
    if s.isdigit():
        d = int(s)
        suma+=d
        dobytok*= d
        dg= True
if dg:
    print("Сума: ", suma)
    print("Добуток: ", dobytok)
else:
    print("немає цифр")

