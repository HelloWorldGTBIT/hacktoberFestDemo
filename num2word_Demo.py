from tkinter import *
from num2word import *
from tkinter import messagebox
window  = Tk()
window.geometry("500x150")
window.title("Number2Word")
head = Label(window,text="Number2Word",font=('Times',20))
head.pack()
text1 = Label(window,text="Enter A Number",font=('Times',15))
text1.place(x=20,y=60)
number = IntVar()
numberinput = Entry(window,textvariable=number,font=('Times',15),width=25)
numberinput.place(x=200,y=60)

def numfun(num1):
    messagebox.showerror("Number2Word","{}".format(num2word(int(num1))))
def reset():
    number.set(0)
check = Button(window,text="Check",font=('Times',15),command=lambda:numfun(numberinput.get()))
check.place(x=300,y=100)
reset = Button(window,text="Reset",font=('Times',15),padx=5,command=reset)
reset.place(x=100,y=100)

window.mainloop()

