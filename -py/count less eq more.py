print('--- Part 1 ---')
n=input('Number (10-99): ')
a=int(n[0])
b=int(n[1])
print('a = %d and b = %d'%(a,b))
print('\n---- Part 2 ---')
cnt1=cnt2=cnt3=0
if a<5:
    cnt1+=1
if b<5:
    cnt1+=1
if a==5:
    cnt2+=1
if b==5:
    cnt2+=1
if a>5:
    cnt3+=1
if b>5:
    cnt3+=1
print('Less than 5 = %d\nEqual to 5 = %d\nMore than 5 = %d'%(cnt1,cnt2,cnt3))
    
