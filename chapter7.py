a='' #empty string
b="spam's"
c='s\np\ta\x00m'
d="""şofdlfdiıdfpl
işldksjlşskdfj
ds.sdkjl.dsjk"""


d=r'tolga \gülcan\n'
d=u'sp\u00e4m'

z="Benim adım %s'dır." %"tolga gülcan"  # Format Strings
z="Yaşım {0}'dür".format(34) #format strings
rnerde=z.find('Y') #find first occurence of text, return -1 if not found

"tolga    \n\ta".rstrip() #strip whitepace
"tolga    \n\ta".lstrip()
"tolga    \n\ta".strip()
k="1,2,3".split(",")  #split on delimeter and return a list

k="15".isdigit() #string text sadece rakamlardan oluşuyor
k="TOLGA".lower() #Change case
k="TOLGA".upper()

k="Tolga".endswith("ga") #text ends with a string

k='-'.join(["t","a"]) #t-o-l-g-a Join list to string

for x in "tolga":
    print(x*3,end=' ')


print(" " in "tolga") #true or false
print([x for x in map(ord,"tolga")])
print(u'eggs\u0020spam')
t='tolga','gulcan'
print (t)
print("tolga"[5:-1:-1])

t="a43a"

s=[x for x in t if x in "0123456789f."]



chr(65)
ord('a')

y="tolga".replace("ko","ko")
print(dir(str))







