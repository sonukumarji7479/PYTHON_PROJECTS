import tkinter as tk
from tkinter import ttk
import calendar

# Function to generate the calendar for a month
def generate_month(year, month, frame):
    # Clear previous content
    for widget in frame.winfo_children():
        widget.destroy()
    
    month_name = calendar.month_name[month]
    tk.Label(frame, text=f"{month_name} {year}", font=("Helvetica", 16, "bold"), bg="#fdf6e3", fg="#333").pack(pady=10)

    days_frame = tk.Frame(frame, bg="#fdf6e3")
    days_frame.pack()

    # Weekdays header
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for idx, day in enumerate(weekdays):
        tk.Label(days_frame, text=day, width=5, font=("Helvetica", 12, "bold"), bg="#ffecb3", fg="#000").grid(row=0, column=idx, padx=2, pady=2)

    cal = calendar.monthcalendar(year, month)
    for r, week in enumerate(cal, start=1):
        for c, day in enumerate(week):
            if day == 0:
                tk.Label(days_frame, text="", width=5, bg="#fdf6e3").grid(row=r, column=c, padx=2, pady=2)
            else:
                bg_color = "#aed581" if c < 5 else "#ff8a65"  # Weekdays green, weekends orange
                tk.Label(days_frame, text=str(day), width=5, bg=bg_color, fg="#000").grid(row=r, column=c, padx=2, pady=2)

# Main window
root = tk.Tk()
root.title("2026 Colorful Calendar - Sonu Kumar")
root.geometry("1200x800")
root.config(bg="#fdf6e3")  # Paper-like background

# Notebook for 12 months
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

for month in range(1, 13):
    frame = tk.Frame(notebook, bg="#fdf6e3")
    notebook.add(frame, text=calendar.month_name[month])
    generate_month(2026, month, frame)

root.mainloop()
