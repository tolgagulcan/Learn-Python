"""
while True:
    a=int(input("write a number: \n"))
    if a==0:
        break
    if a>10:
        print("10 dan büyük")
    elif a<10:
        print("10 dan küçük")

"""

choice=input("what do you want to learn?")
bilgi={"ad":"tolga","soyad":"gülcan","yas":34,"job":"teacher"}
print(bilgi.get(choice,"bad choice"))


try:
    print(bilgi("ayak"))
except:
    print("bad choice")

a=5 if 3<4 else 4

print(a)

k=[0,1,2,3,4,[],[1,2],{},{1:1,3:3}]


print(list(filter(bool,k)))

print(any(k),all(k))

print(k[True],k[False])
