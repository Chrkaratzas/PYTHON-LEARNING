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
