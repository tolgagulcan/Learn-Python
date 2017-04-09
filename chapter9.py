#Tuple Create
a=()
b=1,2,3,"tolga"
c=("t",)
d=(1,2,3,"tolga")
e=('Tolga',("ogrt","prg"))
f=tuple("tolga")

print(a,b,c,d,e,f,sep="\n")

print(e.index(("ogrt","prg")))

print((1,2)+(3,4))

print(sorted((3,1,2)))

k=("tolga","gülcan")

a,b=k

print(a,b)
ad,soyad={"ad":"tolga","soyad":"gülcan"}.values()
print(ad,soyad)

