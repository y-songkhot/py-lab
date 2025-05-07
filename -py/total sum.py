print('--- Part 1 ---')
n=input('Enter 1000-9999: ')
a=int(n[0])
b=int(n[1])
c=int(n[2])
d=int(n[3])
print('a = %d, b = %d, c = %d, d = %d'%(a,b,c,d))
print('\n---- Part 2 ---')
cnts=cntb=sums=sumb=0
if a<5:
    cnts+=1
    sums+=a
else:
    cntb+=1
    sumb+=a
if b<5:
    cnts+=1
    sums+=b
else:
    cntb+=1
    sumb+=b
if c<5:
    cnts+=1
    sums+=c
else:
    cntb+=1
    sumb+=c
if d<5:
    cnts+=1
    sums+=d
else:
    cntb+=1
    sumb+=d
print('Total small number : %d\nSum of small number : %d\nTotal big number : %d\nSum of big number : %d'%(cnts,sums,cntb,sumb))
    
