#print(k) # error not declared variable

ad="tolga"
ad,soyad="tolga","gülcan" #tuble assignment


[ad,soyad]=["ahmet","aslan"] #list assignment
print(ad,soyad)

a,b,c,d,e="tolga" #iterable assignment 1

print(a,b,c,d,e)
a,b,c=["tolga","gülcan","teacher"] #iterable assignment 2
print(a,b,c)

t,*z=[1,2,3,4,5] #sequence unpacking

print(t,z)


a=b=c=0#multple assignment to a vriable

print(a,b,c)

ad="tolga"
ad+=" gülcan"

print(ad)

a,*b="tolga gülcan"

print(a,"".join(b))


ad,soyad="tolga","gülcan"
ad,soyad=soyad,ad #swap values

print(ad,soyad)

h="masa"
a,b,*c="masa"
print(a,b,c)
a,b,c=h[0],h[1],h[2:]
print(a,b,c,sep="*")

((a,b),c)=((15,20),25) #nestep tuple assignment

print(a,b,c)

for a,b,c in ((1,2,3),(4,5,6)): #tuble assignment in for
    print (a,b,c)


red,green,blue=range(3)

print(red,green,blue)


L=[1,2,3,4]
print(*L)

while L:
    print(L[0],L[1:])
    L=L[1:]

a=b=c="spam"
a="tolga"

print(a,b,c)

x=5
print()


print("çksjdskjds",file=open("s.txt","w"))






