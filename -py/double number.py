print('--- Part 1 ---')
n=input('Enter 1000-9999: ')
a=int(n[0:2])
b=int(n[2:4])
print('a=%d, b=%d'%(a,b))
print('\n---- Part 2 ---')
cnt=0
if (a%11)==0:
    cnt+=1
if (b%11)==0:
    cnt+=1
if cnt==0:
    print('No double number')
else:
    if cnt==1:
        print('Double number = %d'%(cnt))
        if (a%11)==0:
            print('It is %d'%(a))
        else:
            print('It is %d'%(b))
    else:
        print('Double number = %d'%(cnt))
        print('It is %d'%(a))
        print('It is %d'%(b))
    
            
        
        
    