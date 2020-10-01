num= int(input('enter no'))
result=0

for i in range(1,num):
    if (num%i)==0:
        result=result+i

if result==num:
    print(num,'perfect')
else:
    print(num,'not perfect')

