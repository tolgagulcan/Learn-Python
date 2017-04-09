a=open(__file__,"r")

try:
    while True:
        print(next(a),end='')
except:
    pass

s=[1,2,3,4]
h=s.__iter__()
print(h)
try:
    while True:
        print(h.__next__())
except:
    pass


print([x+str(y) for x in "tolga" for y in [1,2,3,4] if y<3 if x in "tol"])
#print(len(k))
    
print(__name__)


a=[1,2,3,4]

z=map(lambda x:x*x,a)

#print(list(z))
 
a[0]=5


print(list(z))


a=[4,8,9,9,"fdjhfdkfdfd"]

def k():
    global a

    try:
        value=a[0]
    except:
        value=None
    a=a[1:]
    return value
   
h=iter(k,None)



for d in h:
    print(d)


for j in iter([7,8,9,10]):
    print(j)

