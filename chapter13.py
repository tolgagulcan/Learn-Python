

s={1:"a",2:"b",3:"c"}
print(list(s.items()))
for k in (s):
    print(k)
k=open(__file__,"r")
while True:
    a=k.read(300)
    if not a:break
    print(a)

