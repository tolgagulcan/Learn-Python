t=list("tolga")
k=t.reverse()
t.pop(2) # remove with index
t.remove("a") # remove with value

t=list("tolga")
del t[2:3]
t[2:]=[]
t[4:10]=[1,2,3,4,5,6]

k=list(range(5))
s=[a**2 for a in range(10)]

print(s)
print(['Ni!']*4)
print(3 in [1,2,3])



k=[x for x in [1,2,3,4,5] if x in [2,3,4,5] if x in [3,4,5] if x>5]
print(range(0,5))

def kare(x,a=5):return x*x
k=[1,2,3,4,5]
k[0:-1]=["a","b","c"]
k.extend(["b"])

print(k)


k=[1,2,3,4,5]

for x in reversed(k):
    print(x)
    k.append("a")

k={"ad":"tolga","soyad":"gulcan"}
a={"ad":"tolga","soyad":"ahmet"}

print(k.viewkeys())
      
