print('--- Part 1 ---')
n=input('Integer (100-999): ')
a=int(n[0])
b=int(n[1])
c=int(n[2])
print('a = %d, b = %d and c = %d'%(a,b,c))
print('\n---- Part 2 ---')
print('Maximum number of %d, %d and %d is %d.'%(a,b,c,max(a,b,c)))
if (max(a,b,c)%2)==0:
    print('Number %d is an even number.'%(max(a,b,c)))
else:
    print('Number %d is an odd number.'%(max(a,b,c)))
print('Sum of %d, %d and %d is %d.'%(a,b,c,(a+b+c)))
    