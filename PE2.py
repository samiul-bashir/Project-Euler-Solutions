a=1
b=1
c=0
sum=0
while c<4000000:        #here <for c in range(400000)>) will not work as, 
                        #for each updation of c it will agaim redo the loop for all those c values
    c=a+b
    if c%2==0:
        sum=sum+c
    a=b
    b=c
print(sum)
