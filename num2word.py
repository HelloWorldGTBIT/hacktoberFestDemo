"""
    This Library is Created by Dev.
    Funtion in This Library:
        num2word(int)
            pass 1 to 13 digit number and it will return Its Word Value.
"""
def num2word(number):
    numbers = {10:"Ten",20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
    tens = {100:'Hundred',1000:'Thousand',10000:'Ten Thousand',100000:'One Lakh',1000000:'Ten Lakh'}
    onetotwenty = {0:'zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eightteen',19:'Nineteen',20:'Twenty'}
    def twodigit(num):
        a = str(num)
        if num in onetotwenty:
            return onetotwenty[num]
        elif num in numbers:
            return numbers[num]
        else: 
            return numbers[num-int(a[1])]+" "+onetotwenty[int(a[1])]
    def threedigit(num):
        a = str(num)
        if num in tens:
            return onetotwenty[int(a[0])]+" "+tens[num]
        elif num in onetotwenty:
            return onetotwenty[num]
        elif int(a[1:]) == 00 and len(a)==3: 
            return onetotwenty[int(a[0])]+" Hundred "
        else:
            return onetotwenty[int(a[0])]+" Hundred "+twodigit(int(a[1:]))
    def fourdigit(num):
        a = str(num)   
        if a[1:]=='000':
            return onetotwenty[int(a[0])]+' Thousand '
        else:
            return onetotwenty[int(a[0])]+' Thousand '+threedigit(int(a[1:]))
    def fivedigit(num):
        a = str(num)   
        if a[1:]=='0000':
            return numbers[int(a[0:2])]+' Thousand '
        elif a[2:]=='000':
            return twodigit(int(a[:2]))+' Thousand '
        else:
            return twodigit(int(a[:2]))+' Thousand '+threedigit(int(a[2:]))
    def sixdigit(num):
        a = str(num)   
        if a[1:]=='00000':
            return threedigit(int(a[0:3]))+'Thousand '
        else:
            return threedigit(int(a[0:3]))+" Thousand "+threedigit(int(a[3:]))

    def sevendigit(num):
        a = str(num)   
        if a[1:]=='000000':
            return onetotwenty[int(a[0])]+' Million '
        else:
            return onetotwenty[int(a[0])]+' Million '+sixdigit(int(a[1:]))
    def eightdigit(num):
        a = str(num)
        if a[1:]=="0000000":
            return numbers[int(a[0])]+' Million'
        else:
            return twodigit(int(a[:2]))+' Million '+sixdigit(int(a[2:]))

    def ninedigit(num):
        a = str(num)
        if a[1:]=="00000000":
            return threedigit(int(a[:3]))+'Million'
        else:
            return threedigit(int(a[:3]))+' Million '+sixdigit(int(a[3:]))

    def tendigit(num):
        a = str(num)
        if a[1:]=="000000000":
            return onetotwenty[int(a[0])]+' Billion'
        else:

            return onetotwenty[int(a[0])]+' Billion '+ninedigit(int(a[1:]))
            
    def elevendigit(num):
        a = str(num)
        if a[1:]=="000000000":
            return numbers[int(a[0])]+' Billion'
        else:
            return twodigit(int(a[:2]))+' Billion '+ninedigit(int(a[2:]))
    def twelvedigit(num):
        a = str(num)
        if a[1:]=="0000000000":
            return twodigit(int(a[0]))+' Billion'
        else:
            return threedigit(int(a[:2]))+' Billion '+ninedigit(int(a[3:]))
    def thirteendigit(num):
        a = str(num)
        if a[1:]=="000000000000":
            return twodigit(int(a[0]))+' Trillion'
        else:
            return threedigit(int(a[:2]))+' Triillion '+elevendigit(int(a[2:]))

    if len(str(number))==1 or len(str(number))==2:
        num2wor = str(number)+' : '+twodigit(number)
        return num2wor
    elif len(str(number))==3:
        num2wor = str(number)+' : '+threedigit(number)
        return num2wor
    elif len(str(number))==4:
        num2wor = str(number)+' : '+fourdigit(number)
        return num2wor
    elif len(str(number))==5:
        num2wor =str(number)+' : '+fivedigit(number)
        return num2wor
    elif len(str(number))==6:
        num2wor = str(number)+' : '+sixdigit(number)
        return num2wor
    elif len(str(number))==7:
        num2wor =str(number)+' : '+sevendigit(number)
        return num2wor
    elif len(str(number))==8:
        num2wor =str(number)+' : '+eightdigit(number)
        return num2wor
    elif len(str(number))==9:
        num2wor = str(number)+' : '+ninedigit(number)
        return num2wor
    elif len(str(number))==10:
        num2wor = str(number)+' : '+tendigit(number)
        return num2wor
    elif len(str(number))==11:
        num2wor = str(number)+' : '+elevendigit(number)
        return num2wor
    elif len(str(number))==12:
        num2wor = str(number)+' : '+twelvedigit(number)
        return num2wor
    elif len(str(number))==13:
        num2wor =str(number)+' : '+thirteendigit(number)
        return num2wor
