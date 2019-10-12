# fibonacci series
num1 = eval(input(' Enter number of terms '))
FN = 0 ; SN = 1
print(FN)
print(SN)
for i in range(2, num1):
    TN = FN + SN
    print(TN)
    FN = SN
    SN = TN
    i += 1

