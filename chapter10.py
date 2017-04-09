while True:
    k=input("input a number to find square root:")
    if k=='stop':
        break
    try:
        num=int(k)
        print(num**(0.5))
    except:
        print("Sayı gir dedik!!!")
print("Hoşçakal")
        
        
