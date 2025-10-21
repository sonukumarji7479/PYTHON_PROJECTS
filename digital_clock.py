import tkinter as tk
from tkinter import Label
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.configure(bg="black")

# Function to update time
def time():
    string = strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    date_string = strftime("%d-%m-%Y")  # Day-Month-Year
    time_label.config(text=string)
    date_label.config(text=date_string)
    time_label.after(1000, time)  # update every second

# Date label
date_label = Label(root, font=("Helvetica", 20), bg="black", fg="cyan")
date_label.pack(pady=10)

# Time label
time_label = Label(root, font=("Helvetica", 50, "bold"), bg="black", fg="lime")
time_label.pack(pady=10)

# Call the time function
time()

root.mainloop()
