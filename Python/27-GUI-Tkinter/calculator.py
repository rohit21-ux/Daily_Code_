from tkinter import *

root = Tk()

root.title("Simple calculator")

Label1 = Label(root, text = "Enter first Number:")
Label1.grid(row= 0, column= 0 )

Label2 = Label(root, text = "Enter second Number:")
Label2.grid(row = 1, column = 0)

result = Label(root , text='')
result.grid(row= 3 , column= 0 , columnspan=4)

Entry1 = Entry(root)
Entry1.grid(row= 0, column=1)

Entry2 = Entry(root)
Entry2.grid(row = 1 , column=1)

def add():
    n1 = int(Entry1.get())
    n2 = int(Entry2.get())
    n3 = n1 + n2
    result.config(text= 'Result = '+str(n3))

def subtract():
    n1 = int(Entry1.get())
    n2 = int(Entry2.get())
    n3 = n1 - n2
    result.config(text = 'Result = ' + str(n3))

def Multiply():
    n1 = int(Entry1.get())
    n2 = int(Entry2.get())
    n3 = n1 * n2
    result.config(text = 'Result = ' + str(n3))

def Divide():
    n1 = int(Entry1.get())
    n2 = int(Entry2.get())
    n3 = n1 / n2
    result.config(text = 'Result = ' + str(n3))

B1 =Button(root , text='Add',command=add)
B1.grid(row=2,column=0)

B2 = Button(root,text='Subtract',command=subtract)
B2.grid(row=2,column=1)

B3 = Button(root,text = 'Multiply',command=Multiply)
B3.grid(row = 2 , column= 2)

B4 = Button(root,text = 'Divide',command=Divide)
B4.grid(row = 2 , column= 3)


B5 = Button(root, text='Exit', command=root.destroy)
B5.grid(row=2, column=4)

root.mainloop()

