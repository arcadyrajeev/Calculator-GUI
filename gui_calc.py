from tkinter import *

root = Tk()
root.configure(background="#a0a0a0")
root.title("Simple Calculator")
root.resizable(False,False)

e = Entry(root, width=28, borderwidth=10, font=('Arial', 20))
e.grid(row=0, column=0, columnspan=3)


def button_click(number):
    cur = e.get()
    e.delete(0, END)
    e.insert(0, str(cur) + str(number))

def add(number):
    global action
    action = 'add'
    cur = e.get()
    e.delete(0, END)
    e.insert(0, str(cur) + str(number))

def sub(number):
    global action
    action = 'sub'
    cur = e.get()
    e.delete(0, END)
    e.insert(0, str(cur) + str(number))

def multiply(number):
    global action
    action = 'multiply'
    cur = e.get()
    e.delete(0, END)
    e.insert(0, str(cur) + str(number))

def divide(number):
    global action
    action = 'divide'
    cur = e.get()
    e.delete(0, END)
    e.insert(0, str(cur) + str(number))

def back():
    y = len(e.get())
    e.delete(y-1, END)

def clear():
    e.delete(0, END)

def equal():
    x= e.get()
    if action == 'add':
        w=0
        y = str(x).split("+")
        for i in range(len(y)):
            j = y[i]
            w += int(j)
        e.delete(0, END)
        e.insert(0, w)

    if action == 'multiply':
        w=1
        y = str(x).split("x")
        for i in range(len(y)):
            j = y[i]
            w *= int(j)
        e.delete(0, END)
        e.insert(0, w)

    if action == 'divide':
        y = str(x).split("/")
        for i in range(len(y)):
            j = y[0]
            k= y[len(y)-1]
            w = int(j)/int(k)
        e.delete(0, END)
        e.insert(0, w)

    if action == 'sub':
        w=0
        y = str(x).split("-")
        for i in range(len(y)):
            if w==0:
                j = y[-i]
                w += int(j)
            else:
                j = y[-i]
                w -= int(j)
        e.delete(0, END)
        e.insert(0, w)


# buttons load
button_1 = Button(root, text="1", font=('Arial', 25), padx=50, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", font=('Arial', 25), padx=50, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", font=('Arial', 25), padx=50, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", font=('Arial', 25), padx=50, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", font=('Arial', 25), padx=50, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", font=('Arial', 25), padx=50, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", font=('Arial', 25), padx=50, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", font=('Arial', 25), padx=50, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", font=('Arial', 25), padx=50, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", font=('Arial', 25), padx=50, pady=10, command=lambda: button_click(0))
button_add = Button(root, text="+", font=('Arial', 25), padx=49, pady=10, command=lambda: add("+"))
button_sub = Button(root, text="-", font=('Arial', 25), padx=53, pady=10, command=lambda: sub("-"))
button_multiply = Button(root, text="x", font=('Arial', 25), padx=50, pady=10, command=lambda: multiply("x"))
button_divide = Button(root, text="/ ", font=('Arial', 25), padx=49, pady=10, command=lambda: divide("/"))
button_equal = Button(root, text="  =  ", font=('Arial', 25), padx=185, pady=10, command=equal)
button_clear = Button(root, text="Clear", font=('Arial', 25), padx= 96 , pady=10, command=clear)
button_delete = Button(root, text="Backspace", font=('Arial', 25), padx= 56, pady=10, command=back)



# button draw
button_7.grid(row=1, column=0, padx= 0)
button_8.grid(row=1, column=1, padx= 0)
button_9.grid(row=1, column=2, padx= 0)

button_4.grid(row=2, column=0, padx= 0)
button_5.grid(row=2, column=1, padx= 0)
button_6.grid(row=2, column=2, padx= 0)

button_1.grid(row=3, column=0, padx= 0)
button_2.grid(row=3, column=1, padx= 0)
button_3.grid(row=3, column=2, padx= 0)

button_0.grid(row=4, column=0, padx= 0)
button_add.grid(row=4, column=1, padx= 0)
button_sub.grid(row=4, column=2, padx= 0)

button_multiply.grid(row=5, column=0, padx= 0)
button_divide.grid(row=6, column=0, padx= 0)
button_delete.grid(row=5, column=1, columnspan=2, padx= 0)
button_clear.grid(row=6, column=1, columnspan=2, padx= 0)
button_equal.grid(row=7, column=0, columnspan=3, padx= 0)


root.mainloop()