from tkinter import *
root=Tk()
def add():
    a=int(num1entry.get())
    b=int(num2entry.get())
    c=a+b
    l=Label(root,texy=c)
    l.grid(row=2,column=4)

root.geometry("300x300")
root.title("Calculator")

num1=Label(root,text="Enter number 1:")
num2=Label(root,text="Enter number 2:")
num1.grid(row=0,column=2)
num2.grid(row=1,column=2)

num1entry=Entry(root,text="Enter number 1:")
num2entry=Entry(root,text="Enter number 2:")
num1entry.grid(row=0,column=3)
num2entry.grid(row=1,column=3)

b1=Button(root,command=add,text="ADD")
b1.grid(row=2,column=0)

root.mainloop()