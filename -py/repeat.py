print('--- Part 1 ---')
n=input('Enter 1000-9999: ')
a=int(n[0])
b=int(n[1])
c=int(n[2])
d=int(n[3])
print('a = %d, b = %d, c = %d, d = %d'%(a,b,c,d))
print('\n---- Part 2 ---')
if a==b or a==c or a==d:
    print('Repeat Number is %d'%(a))
if b==c or b==d:
    if not a==b:
        print('Repeat Number is %d'%(b))
if c==d:
    if not b==c:
        print('Repeat Number is %d'%(c))
if not (a==b or a==c or a==d or b==c or b==d or c==d):
    print('All numbers are different')
        
        
    


    
    
    
        
    