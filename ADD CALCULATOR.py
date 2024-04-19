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

def plus(sign):
    number1 = e.get()
    numbers.append(int(number1))
    numbers.append(sign)
    e.delete(0, END)

def equal():
    a = e.get()
    numbers.append(int(a))
    e.delete(0, END)
    result = numbers[0]  # Start with the first number in the list

    i = 1  # Start index for the loop
    while i < len(numbers):
        operator = numbers[i]  # Get the operator
        number = numbers[i + 1]  # Get the number following the operator

        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
        elif operator == '*':
            result *= number
        elif operator == '/':
            try:
                result /= number
            except ZeroDivisionError:
                e.insert(0, "You cannot divide by zero")
                clear()
        else:
            raise ValueError("Unsupported operator")

        i += 2  # Move to the next operator
    numbers.clear()
    e.insert(0,result)


def clear():
    e.delete(0,END)
    numbers.clear()

button_0 = Button(root,text = "0", padx=40, pady=40, command= lambda : add(0),bg='green')
button_1 = Button(root,text = "1", padx=40, pady=40, command=lambda : add(1),bg='green')
button_2 = Button(root,text = "2", padx=40, pady=40, command=lambda : add(2),bg='green')
button_3 = Button(root,text = "3", padx=40, pady=40, command=lambda : add(3),bg='green')
button_4 = Button(root,text = "4", padx=40, pady=40, command=lambda : add(4),bg='green')
button_5 = Button(root,text = "5", padx=40, pady=40, command=lambda : add(5),bg='green')
button_6 = Button(root,text = "6", padx=40, pady=40, command = lambda : add(6),bg='green')
button_7 = Button(root,text = "7", padx=40, pady=40, command=lambda :add(7),bg='green')
button_8 = Button(root,text = "8", padx=40, pady=40, command= lambda: add(8),bg='green')
button_9 = Button(root,text = "9", padx=40, pady=40, command=lambda : add(9),bg='green')
button_add = Button(root,text = "+" , padx=79, pady=40, command=lambda : plus('+'),bg='grey')
button_minus = Button(root,text = "-" , padx=79, pady=40, command=lambda : plus('-'),bg='grey')
button_times = Button(root,text = "*" , padx=79, pady=40, command=lambda : plus('*'),bg='grey')
button_divide = Button(root,text = "/" , padx=79, pady=40, command=lambda : plus('/'),bg='grey')
button_equals = Button(root,text = "=", padx=91, pady=40, command=lambda : equal(),bg='yellow')
button_clear = Button(root,text = "Clear", padx=40, pady=40, command=lambda : clear(),bg='red')



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

button_minus.grid(row=6,column = 1)
button_times.grid(row=6,column = 2)
button_divide.grid(row=6,column = 3)

root.mainloop()
