#Sum of given number until 0 is pressed
print("Sum of Given Number(Till 0 is pressed)")
sum = 0
i=1
num = None
while(num!=0):
    num = int(input("Enter {0} number\n".format(i)))
    sum+=num
    i+=1
print("Sum is",sum)

