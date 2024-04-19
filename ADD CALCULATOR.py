from tkinter import *
root = Tk()
root.title("Simple Calculator")

e = Entry(root,width = 15, borderwidth=5)
e.grid(row = 0,column = 0, columnspan = 3, padx = 30 , pady = 10)

numbers = []
def add(number):
   current = e.get()
   e.delete(0, END)
   e.insert(0,str(current)+str(number))

def plus():
    number1 = e.get()
    numbers.append(int(number1))
    e.delete(0, END)

def equal():
    number = e.get()
    e.delete(0, END)
    numbers.append(int(number))
    # Initialize a variable to store the sum
    total_sum = 0
    # Loop through each number in the list
    for number in numbers:
        total_sum = total_sum + number  # Add each number to the total sum
    e.insert(0, total_sum)
    numbers.clear()

def clear():
    e.delete(0,END)
    numbers.clear()

button_0 = Button(root,text = "0", padx=40, pady=40, command= lambda : add(0))
button_1 = Button(root,text = "1", padx=40, pady=40, command=lambda : add(1))
button_2 = Button(root,text = "2", padx=40, pady=40, command=lambda : add(2))
button_3 = Button(root,text = "3", padx=40, pady=40, command=lambda : add(3))
button_4 = Button(root,text = "4", padx=40, pady=40, command=lambda : add(4))
button_5 = Button(root,text = "5", padx=40, pady=40, command=lambda : add(5))
button_6 = Button(root,text = "6", padx=40, pady=40, command = lambda : add(6))
button_7 = Button(root,text = "7", padx=40, pady=40, command=lambda :add(7))
button_8 = Button(root,text = "8", padx=40, pady=40, command= lambda: add(8))
button_9 = Button(root,text = "9", padx=40, pady=40, command=lambda : add(9))
button_add = Button(root,text = "+" , padx=79, pady=40, command=lambda : plus())
button_equals = Button(root,text = "=", padx=91, pady=40, command=lambda : equal())
button_clear = Button(root,text = "Clear", padx=40, pady=40, command=lambda : clear())



button_0.grid(row=3, column=0)
button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)

button_3.grid(row=2, column=0)
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)

button_6.grid(row=1, column=0)
button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)

button_9.grid(row=4, column=0)
button_add.grid(row=4,column = 1, columnspan = 2)

button_clear.grid(row=5, column=0)
button_equals.grid(row=5,column = 1, columnspan = 2)

root.mainloop()







































