import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]


num=random.randrange(0,len(words),1)

def res():
   global words,answers,num
   num=random.randrange(0,len(words),1)
   lbl.config(text=words[num])
   e1.delete(0,END)

def default():
    global words,answers,num
    lbl.config(text=words[num])

def checkans():
    global words,answers,num
    var=e1.get()
    if var==answers[num]:
        messagebox.showinfo("Success","This is Correct Answer")
        res()
    else:
        messagebox.showerror("error","This is Wrong Answer")
        e1.delete(0,END)





root=tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Jumbled")
root.configure(background="#000000")

lbl=Label(
    root,
    text="Text here",
    font=("verdana",18),
    bg="#000000",
    fg="#ffffff",
)
lbl.pack(pady=30,ipadx=10,ipady=10)



ans1=StringVar()
e1=Entry(
    root,
    font=("verdana",16),
    textvariable=ans1,
)
e1.pack(ipady=5,ipadx=5)

btn1=Button(
    root,
    text="Check",
    font=("Comic sans ms",16),
    width=16,
    bg="#4C4B4B",
    fg="#6ab04c",
    relief= GROOVE,
    command=checkans,


)
btn1.pack(pady=40)

btn2=Button(
    root,
    text="Reset",
    font=("Comic sans ms",16),
    width=16,
    bg="#4C4B4B",
    fg="#EA425C",
    relief= GROOVE,
    command=res


)
btn2.pack()

default()

root.mainloop()
