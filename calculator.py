from tkinter import *


root = Tk()
root.geometry('294x290')
root.title('calculate')
root.resizable(0,0)
root.config(bg="black")

firstnumber = secondnumber = operator = None

def get_digit(digit):
    curnt = label_frame1["text"]
    new = curnt + str(digit)
    label_frame1.config(text=new)

def clear():
    label_frame1.config(text='')

def CE():
    label_frame1.config(text='')


def get_operator(op):
    global firstnumber,operator
    firstnumber = int(label_frame1['text'])
    operator = op
    label_frame1.config(text="")


def get_result():
    global firstnumber, secondnumber, operator

    secondnumber = int(label_frame1['text'])

    if operator == "+":
        label_frame1.config(text=str(firstnumber + secondnumber))
    elif operator == "-":
        label_frame1.config(text=str(firstnumber - secondnumber))
    elif operator == "x":
        label_frame1.config(text=str(firstnumber * secondnumber))
    elif operator == "%":
        label_frame1.config(text=int(firstnumber/100) * secondnumber)
    else:
        if secondnumber == 0:
            label_frame1.config(text='Error')
        else:
            label_frame1.config(text=str(firstnumber / secondnumber))



label_frame1 =Label(root,text="", width="21",bd="16",relief=RIDGE,bg="black",fg="white", font='arial 15 bold')
label_frame1.place(x=3.5, y=30)
label_frame1.focus()


btnclear = Button(root, text="C",fg="white", font="arial 11",width="7", bg="black",bd="4", command=lambda :clear())
btnclear.place(x=0, y=100)

btncancel = Button(root, text="CE",fg="white", font="arial 11",width="7", bg="black",bd="4", command=lambda :CE())
btncancel.place(x=72.25,y=100)

btndiv = Button(root, text="/",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda :get_operator('/'))
btndiv.place(x=144.5, y=100)

btnper = Button(root, text="%",fg="white", font="arial 11 ",width="7", bg="black",bd="4",command=lambda :get_operator('%'))
btnper.place(x=216.7, y=100)



btn7 = Button(root, text="7",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit(7))
btn7.place(x=0, y=135)

btn8 = Button(root, text="8",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit(8))
btn8.place(x=72.25,y=135)

btn9 = Button(root, text="9",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit(9))
btn9.place(x=144.50, y=135)

btnmul = Button(root, text="x",fg="white", font="arial 11 ",width="7", bg="black",bd="4",command=lambda:get_operator('x'))
btnmul.place(x=216.75, y=135)

btn4 = Button(root, text="4",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit(4))
btn4.place(x=0, y=170)

btn5 = Button(root, text="5",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit(5))
btn5.place(x=72.25,y=170)

btn6 = Button(root, text="6",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit(6))
btn6.place(x=144.50, y=170)

btnplus = Button(root, text="+",fg="white", font="arial 11 ",width="7", bg="black",bd="4",command=lambda:get_operator('+'))
btnplus.place(x=216.75, y=170)

btn1 = Button(root, text="1",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit(1))
btn1.place(x=0, y=205)

btn2 = Button(root, text="2",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit(2))
btn2.place(x=72.25,y=205)

btn3 = Button(root, text="3",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit(3))
btn3.place(x=144.50, y=205)

btnmin = Button(root, text="-",fg="white",font="arial 11 ",width="7", bg="black",bd="4",command=lambda:get_operator('-'))
btnmin.place(x=216.75, y=205)

btn00 = Button(root, text="00",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit('00'))
btn00.place(x=0, y=240)

btn0 = Button(root, text="0",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit(0))
btn0.place(x=72.25, y=240)

btnpoint = Button(root, text=".",fg="white", font="arial 11",width="7", bg="black",bd="4",command=lambda:get_digit('.'))
btnpoint.place(x=144.50,y=240)

btneql = Button(root, text="=",fg="white",font="arial 11 ",width="7", bg="black",bd="4", command=lambda :get_result())
btneql.place(x=216.75, y=240)



root.mainloop()