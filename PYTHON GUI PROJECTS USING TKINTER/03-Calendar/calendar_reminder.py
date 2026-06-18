from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import calendar
from datetime import datetime

reminders = {}
today = datetime.today()
year = today.year
month = today.month

def show_reminders(day):
    key = f"{year}-{month}-{day}"

    if key in reminders:

        messagebox.showinfo("Reminders", f"{day} {calendar.month_name[month]}:\n" + "\n".join(reminders[key]))

    else:

        messagebox.showinfo("Reminders", f"No reminders for {day} {calendar.month_name[month]}")

def add_reminder(day):

    note = simpledialog.askstring("Add Reminder", f"Reminder for {day} {calendar.month_name[month]}:")

    if note:

        key = f"{year}-{month}-{day}"

        reminders.setdefault(key, []).append(note)

        messagebox.showinfo("Saved", "Reminder added!")

def delete_reminders(day):
    key = f"{year}-{month}-{day}"

    if key in reminders:

        del reminders[key]

        messagebox.showinfo("Deleted", "All reminders removed.")
    else:

        messagebox.showinfo("Info", "No reminders to delete.")

def day_options(day):

    top = Toplevel(root_window)

    top.title(f"Day: {day}")

    Label(top, text=f"{day} {calendar.month_name[month]}", font=("Arial", 12)).pack(pady=10)

    Button(top, text="View Reminders", command=lambda: show_reminders(day), bg="lightblue").pack(pady=5)
    Button(top, text="Add Reminder", command=lambda: add_reminder(day), bg="lightgreen").pack(pady=5)
    Button(top, text="Delete Reminders", command=lambda: delete_reminders(day), bg="lightcoral").pack(pady=5)

def draw_calendar():
    cal = calendar.monthcalendar(year, month)

    Label(root_window, text=f"{calendar.month_name[month]} {year}", font=("Arial", 14)).grid(row=0, column=0, columnspan=7, pady=10)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for i, day_name in enumerate(days):

        Label(root_window, text=day_name, font=("Arial", 10, "bold")).grid(row=1, column=i)

    for row_index, week in enumerate(cal, start=2):

        for col_index, day in enumerate(week):
            
            if day != 0:
                
                Button(
                   
                   
                    root_window, text=str(day), width=4,
                    command=lambda d=day: day_options(d),
                    bg="lightyellow"
                ).grid(row=row_index, column=col_index, padx=2, pady=2)

root_window = Tk()
root_window.title("Calendar Reminder App")
root_window.configure(bg="white")
root_window.geometry("500x400")

draw_calendar()
root_window.mainloop()
