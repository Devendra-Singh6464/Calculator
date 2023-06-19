import tkinter
from tkinter import*
from tkinter import messagebox

d = tkinter.Tk()
a = StringVar()
b = StringVar()
c = StringVar()

# def tkin():
    # messagebox.showinfo("message",t.get())

d.geometry("500x400")
d.config(bg="#B3C51B")
d.title("My Calculator")

def getAdd():
    ad=int(a.get())+int(b.get())
    c.set(ad)

def getSub():
    ad=int(a.get())-int(b.get())
    c.set(ad)

def getMul():
    ad=int(a.get())*int(b.get())
    c.set(ad)

def getDiv():
    ad=int(a.get())/int(b.get())
    c.set(ad)


l1 = Label(text="CLCULATOR",bg="Aqua",fg="red",font="lucida 14 bold",border=4,relief=SUNKEN).place(x=180,y=20)

l1 = Label(text="Enter First Number").place(x=40,y=80)
t1 = Entry(textvariable=a).place(x=210, y=80)

l2 = Label(text="Enter Second Number").place(x=40,y=120)
t2 = Entry(textvariable=b).place(x=210, y=120)

l3 = Label(text="Result").place(x=40,y=160)
t3 = Entry(textvariable=c).place(x=210, y=160)

b1=Button(text="Add",fg="red",bg="Aqua",font="lucida 12 bold",command=getAdd).place(x=40,y=200)
b2=Button(text="Sub",fg="red",bg="Aqua",font="lucida 12 bold",command=getSub).place(x=130,y=200)
b3=Button(text="Mul",fg="red",bg="Aqua",font="lucida 12 bold",command=getMul).place(x=210,y=200)
b4=Button(text="Div",fg="red",bg="Aqua",font="lucida 12 bold",command=getDiv).place(x=300,y=200)


d.mainloop()
