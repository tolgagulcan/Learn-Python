a=[1,2,3,4]

def k():
    global a
    value=a[0:1]
    a=a[1:]
    return value
   
h=iter(k,[])



for d in h:
    print(d)


for j in iter([7,8,9,10]):
    print(j)
