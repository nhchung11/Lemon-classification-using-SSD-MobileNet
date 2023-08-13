import tkinter as tk
import subprocess

process = None

def run_file1():
    global process
    process = subprocess.Popen(['python', '/home/nhomrobot/Desktop/arm_control/Lemon.py'])

def run_file2():
    global process
    process = subprocess.Popen(['python', '/home/nhomrobot/Desktop/arm_control/test.py'])

def stop_file():
    global process
    if process is not None:
        process.kill()
        process = None

root = tk.Tk()
root.title("Button Example")
root.geometry("200x200")  # Set window size

button1 = tk.Button(root, text="Run Lemon", command=run_file1)
button1.pack()

button2 = tk.Button(root, text="Run Control", command=run_file2)
button2.pack()

button3 = tk.Button(root, text="Stop Running File", command=stop_file)
button3.pack()

root.mainloop()