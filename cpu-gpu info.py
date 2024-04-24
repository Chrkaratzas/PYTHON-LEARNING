"""
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
                result //= number
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


from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image viewer")

image1 = ImageTk.PhotoImage(Image.open('cold.png'))
image2 = ImageTk.PhotoImage(Image.open('current_frame.jpg'))
image3 = ImageTk.PhotoImage(Image.open('leaf.jpg'))

images = [image1,image2,image3]

myLabel = Label(image = images[0])

myLabel.grid(row = 0, column = 0, columnspan = 3)


def forward(image_number):
    global button_for
    global button_back
    global myLabel
    myLabel.grid_forget()
    if image_number == 2:
        myLabel = Label(image=images[2])
        button_for = Button(root, text=">>", state=DISABLED)
        button_back = Button(root, text="<<", command=lambda: backword())
    else:
        myLabel = Label(image=images[image_number + 1])
        button_for = Button(root, text=">>", command=lambda: forward())
        if image_number == 0:
            button_back = Button(root, text="<<", command=lambda: backword())
        else:
            button_back = Button(root, text="<<", command=lambda: backword())

    myLabel.grid(row=0, column=0, rowspan=3)
    button_for.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


def backword(image_number):
    global button_for
    global button_back
    global myLabel

    myLabel.grid_forget()
    if image_number == 0:
        myLabel = Label(image=images[0])
        button_back = Button(root, text="<<", state=DISABLED)
        button_for = Button(root, text=">>", command=lambda: forward())
    else:
        myLabel = Label(image=images[image_number])
        button_for = Button(root, text=">>", command=lambda: forward())
        button_back = Button(root, text="<<", command=lambda: backword())

    myLabel.grid(row=0, column=0, rowspan=3)
    button_for.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


button_for = Button(root, text=">>", command=lambda : forward())
button_back = Button(root, text="<<", command=lambda : backword())
button_quit = Button(root, text="Exit programm", command= root.quit)

button_for.grid(row = 1, column = 2)
button_back.grid(row = 1, column =0)
button_quit.grid(row = 1, column =1)

root.mainloop()


from tkinter import *
root = Tk()
def command():
    myLabel = Label(root, text="YOU HAVE CREATED A NEW FILE ON YOUR DESKTOP")
    myLabel.pack()
def Copy():
    myLabel = Label(root, text="YOU HAVE COPIED A MESSAGE")
    myLabel.pack()

def Paste():
    myLabel = Label(root, text="YOU HAVE PASTED A MESSAGE")
    myLabel.pack()


my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command = command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command = Copy)
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=Paste)
root.mainloop()
"""
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import psutil
import GPUtil
import time
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk






root = Tk()
root.title("CPU & GPU INFO")
myLabel = Label(root,text="Enter number of seconds you want to get data from you CPU and GPU",bg='yellow',fg='blue')
myLabel.pack()
e = Entry(root, width=100, borderwidth=5)
e.pack()
def get_secs():
    global message
    message = e.get()
    my_img = ImageTk.PhotoImage(Image.open("waiting_image.jpg"))
    img_label = Label(root, image=my_img)
    img_label.pack()
    root.update()

    try:
        message = int(message)
        if message > 60:
            response = messagebox.askquestion("Are you sure?", f"{message} are quite a few seconds, are you sure?")
            if response:
                img_label.destroy()

            if response.lower() == 'yes':
                # Time interval in seconds between readings
                interval = 1
                # Duration to monitor in seconds
                monitor_duration = message

                # Lists to hold usage data
                times = []
                cpu_usages = []
                gpu_usages = []

                # Monitoring loop
                start_time = time.time()
                while time.time() - start_time < monitor_duration:
                    # Get CPU usage
                    cpu_usage = psutil.cpu_percent()
                    cpu_usages.append(cpu_usage)

                    # Get GPU usage
                    gpus = GPUtil.getGPUs()
                    if gpus:
                        gpu_usage = gpus[0].load * 100
                    else:
                        gpu_usage = 0  # In case there are no NVIDIA GPUs available
                    gpu_usages.append(gpu_usage)

                    # Append current time
                    current_time = time.time() - start_time
                    times.append(current_time)

                    # Sleep for the specified interval
                    time.sleep(interval)

                img_label.destroy()
                # Plotting
                plt.figure(figsize=(10, 5))
                plt.plot(times, cpu_usages, label='CPU Usage (%)')
                plt.plot(times, gpu_usages, label='GPU Usage (%)', linestyle='--')
                plt.xlabel('Time (seconds)')
                plt.ylabel('Usage (%)')
                plt.title('CPU and GPU Usage Over Time')
                plt.legend()
                plt.grid(True)
                plt.show()
            else:
                messagebox.showinfo("Alright", f"{message} are quite a few seconds, choose another number!!")
        else:
            # Time interval in seconds between readings
            interval = 1
            # Duration to monitor in seconds
            monitor_duration = message

            # Lists to hold usage data
            times = []
            cpu_usages = []
            gpu_usages = []

            # Monitoring loop
            start_time = time.time()
            while time.time() - start_time < monitor_duration:
                # Get CPU usage
                cpu_usage = psutil.cpu_percent()
                cpu_usages.append(cpu_usage)

                # Get GPU usage
                gpus = GPUtil.getGPUs()
                if gpus:
                    gpu_usage = gpus[0].load * 100
                else:
                    gpu_usage = 0  # In case there are no NVIDIA GPUs available
                gpu_usages.append(gpu_usage)

                # Append current time
                current_time = time.time() - start_time
                times.append(current_time)

                # Sleep for the specified interval
                time.sleep(interval)

            img_label.destroy()
            # Plotting
            plt.figure(figsize=(10, 5))
            plt.plot(times, cpu_usages, label='CPU Usage (%)')
            plt.plot(times, gpu_usages, label='GPU Usage (%)', linestyle='--')
            plt.xlabel('Time (seconds)')
            plt.ylabel('Usage (%)')
            plt.title('CPU and GPU Usage Over Time')
            plt.legend()
            plt.grid(True)
            plt.show()

    except ValueError:
        response = messagebox.showerror("Wrong input", "You must only enter numbers")
        if response:
            img_label.destroy()

button = Button(root, text="Click me to get your info", command=get_secs)
button.pack()
button = Button(root, text="Exit", command=root.destroy)
button.pack()

root.mainloop()