


a=open("a.txt").readlines()
size=len(a)


with open('b2.txt', mode='w', encoding='utf-8') as b2:
    with open('b1.txt', mode='w', encoding='utf-8') as b1:
        
        for i in range(0, size):
            if(i%2==0):
                b2.write(a[i].lower())
            else:
                b1.write(a[i].upper())