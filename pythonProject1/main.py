from tkinter import*
def btnEqualsInput():
    global operator
    sum = str(eval(operator))
    text_input.set(sum)
    operator=""

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")


cal=Tk()
cal.title("calculator")
cal.config(bg="#949284")
operator=""
text_input=StringVar()
txtDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_input,bd=2,insertwidth=4,
                           bg="#949284" ,justify="right").grid(columnspan=4)
btn7=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="7",bg="#949284",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="8",bg="#949284",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="9",bg="#949284",command=lambda:btnClick(9)).grid(row=1,column=2)
Addition=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="+",bg="#E40D6F",command=lambda:btnClick("+")).grid(row=1,column=3)
#=====================================================================================
btn4=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="4",bg="#949284",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="5",bg="#949284",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="6",bg="#949284",command=lambda:btnClick(6)).grid(row=2,column=2)
Subtraction=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="-",bg="#E40D3E",command=lambda:btnClick("-")).grid(row=2,column=3)
btn1=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="1",bg="#949284",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="2",bg="#949284",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="3",bg="#949284",command=lambda:btnClick(3)).grid(row=3,column=2)
multiply=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="x",bg="#949284",command=lambda:btnClick("*")).grid(row=3,column=3)
ex=Button(cal,padx=55,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="^",bg="#949284",command=lambda:btnClick("**")).grid(row=4,column=1,columnspan=2)
btn0=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="0",bg="#949284",command=lambda:btnClick(0)).grid(row=4,column=0)
btnclear=Button(cal,padx=16,pady=16,bd=1,fg="black",font=('arial',20,'bold'),
            text="c",bg="pink",command=btnClearDisplay).grid(row=5,column=2)

division=Button(cal,padx=16,pady=55,bd=1,fg="black",font=('arial',20,'bold'),
            text="/",bg="#F4D618",command=lambda:btnClick("/")).grid(row=4,column=3,rowspan=2)

btnEquals=Button(cal,width=2,padx=53,pady=15,bd=1,fg="black",font=('arial',20,'bold'),
            text="=",bg="#18F440",command=btnEqualsInput).grid(row=5,column=0,columnspan=2)


cal.mainloop()