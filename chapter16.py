import random
ls=[]
for i in range(49):
    ls.append(i+1)


print("*"*10)
for i in range(8):
    t=[]
    for s in range(6):
        a=random.randint(0,len(ls)-1)
        t.append(ls[a])
        ls.pop(a)
    print(i+1,". Kolon: ",sorted(t))
    print("\n")
print("Kalan sayı:",ls)
print("*"*20)


