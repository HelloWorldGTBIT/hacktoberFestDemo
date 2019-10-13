
print("All Armstrong Numbers from 1 to 500 are:- ")
for i in range(1,501):
    num2=i
    rem=0
    check=0
    while(i>0):
        rem=i%10
        check+=rem**len(str(num2))
        i//=10
        if(check==num2):
                print(num2)
