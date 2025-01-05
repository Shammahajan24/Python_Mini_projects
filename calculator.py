import tkinter
from tkinter import *
from tkinter import messagebox
val=""
A=0
operator=""
def btn1_isClicked():
    global val
    val=val+"1"
    data.set(val)
def btn2_isClicked():
    global val
    val=val+"2"
    data.set(val)
def btn3_isClicked():
    global val
    val=val+"3"
    data.set(val)
def btn4_isClicked():
    global val
    val=val+"4"
    data.set(val)
def btn5_isClicked():
    global val
    val=val+"5"
    data.set(val)
def btn6_isClicked():
    global val
    val=val+"6"
    data.set(val)
def btn7_isClicked():
    global val
    val=val+"7"
    data.set(val)
def btn8_isClicked():
    global val
    val=val+"8"
    data.set(val)
def btn9_isClicked():
    global val
    val=val+"9"
    data.set(val)
def btn0_isClicked():
    global val
    val=val+"0"
    data.set(val)




def btnadd_isClicked():
    global A
    global operator
    global val
    A=int(val)
    operator="+"
    val=val + "+"
    data.set(val)
def btnminus_isClicked():
    global A
    global operator
    global val
    A=int(val)
    operator="−"
    val=val + "−"
    data.set(val)
def btnmult_isClicked():
    global A
    global operator
    global val
    A=int(val)
    operator="×"
    val=val + "×"
    data.set(val)
def btndiv_isClicked():
    global A
    global operator
    global val
    A=int(val)
    operator="÷"
    val=val + "÷"
    data.set(val)

def C_Clicked():
    global A
    global operator
    global val
    val=""
    A=0
    operator=""
    data.set(val)


def result():
    global A
    global operator
    global val
    val2=val
    if operator=="+":
        x=int((val2.split("+")[1]))
        C=A+x
        data.set(C)
        val=str(C)
    elif operator=="−":
        x=int((val2.split("−")[1]))
        C=A-x
        data.set(C)
        val=str(C) 
    elif operator=="×":
        x=int((val2.split("×")[1]))
        C=A*x
        data.set(C)
        val=str(C) 
    elif operator=="÷":
        x=int((val2.split("÷")[1]))
        if x==0:
            messagebox.showerror("Error","Division By 0 Not Suooprted")
            A=""
            val=""
            data.set(val)
        else:
            C=int(A/x)
            data.set(C)
            val=str(C)    


    











root=tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Standard")

data=StringVar()
lbl=Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana",20),
    textvariable=data,
    background="#ffffff",
    fg="#FF6C22",
)
lbl.pack(expand=True,fill="both")


btn_row1=Frame(root,bg="#000000")
btn_row1.pack(expand=True,fill="both")

btn_row2=Frame(root)
btn_row2.pack(expand=True,fill="both")

btn_row3=Frame(root)
btn_row3.pack(expand=True,fill="both")

btn_row4=Frame(root)
btn_row4.pack(expand=True,fill="both")

btn7=Button(
    btn_row1,
    text="7",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn7_isClicked,
    fg="#750E21"

)
btn7.pack(side=LEFT,expand=True,fill="both",)

btn8=Button(
    btn_row1,
    text="8",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn8_isClicked,
    fg="#750E21"

)
btn8.pack(side=LEFT,expand=True,fill="both",)

btn9=Button(
    btn_row1,
    text="9",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn9_isClicked,
    fg="#750E21"

)
btn9.pack(side=LEFT,expand=True,fill="both",)

btnmult=Button(
    btn_row1,
    text="×",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btnmult_isClicked,
    fg="#0B60B0"

)
btnmult.pack(side=LEFT,expand=True,fill="both",)



btn4=Button(
    btn_row2,
    text="4",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn4_isClicked,
    fg="#750E21"

)
btn4.pack(side=LEFT,expand=True,fill="both",)

btn5=Button(
    btn_row2,
    text="5",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn5_isClicked,
    fg="#750E21"

)
btn5.pack(side=LEFT,expand=True,fill="both",)

btn6=Button(
    btn_row2,
    text="6",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn6_isClicked,
    fg="#750E21"

)
btn6.pack(side=LEFT,expand=True,fill="both",)

btnminus=Button(
    btn_row2,
    text="−",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btnminus_isClicked,
    fg="#0B60B0"

)
btnminus.pack(side=LEFT,expand=True,fill="both",)


btn1=Button(
    btn_row3,
    text="1",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn1_isClicked,
    fg="#750E21"

)
btn1.pack(side=LEFT,expand=True,fill="both",)

btn2=Button(
    btn_row3,
    text="2",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn2_isClicked,
    fg="#750E21"

)
btn2.pack(side=LEFT,expand=True,fill="both",)

btn3=Button(
    btn_row3,
    text="3",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn3_isClicked,
    fg="#750E21"


)
btn3.pack(side=LEFT,expand=True,fill="both",)

btnadd=Button(
    btn_row3,
    text="+",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btnadd_isClicked,
    fg="#0B60B0"

)
btnadd.pack(side=LEFT,expand=True,fill="both",)

btnreset=Button(
    btn_row4,
    text="C",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=C_Clicked,
    fg="#DA0C81"

)
btnreset.pack(side=LEFT,expand=True,fill="both",)

btn0=Button(
    btn_row4,
    text="0",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn0_isClicked,
    fg="#750E21"

)
btn0.pack(side=LEFT,expand=True,fill="both",)

btndiv=Button(
    btn_row4,
    text="÷",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btndiv_isClicked,
    fg="#0B60B0"

)
btndiv.pack(side=LEFT,expand=True,fill="both",)

btnequal=Button(
    btn_row4,
    text="=",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=result,
    fg="#9FBB73"

)
btnequal.pack(side=LEFT,expand=True,fill="both",)



root.mainloop()