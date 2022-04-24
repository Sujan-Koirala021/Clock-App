"""
Sujan Koirala, Institute of Engineering, Pulchowk

Clock App
# This is a simple clock app that shows the standard time of your current timezone 
"""

from tkinter import *
import time

root = Tk()
root.title('Clock')
root.iconbitmap('clock_icon.ico')


def updateDisplay():

    hour = time.strftime("%I")          # %I -> 12 hour clock while %H -> 24 hour clock
    minute = time.strftime("%M")        # Minute
    second = time.strftime("%S")        # Second
    am_pm = time.strftime("%p")         # AM or PM
    week_name = time.strftime("%a")     # Abbreviated week name
    day_decimal = time.strftime("%d")   # Day in decimal like 1 - 30
    month = time.strftime("%B")         # Full month name
    timezone = time.strftime("%Z")      # Time zone

    myLabel1.config(text=f'{hour}:{minute}:{second} {am_pm}')
    myLabel1.after(1000, updateDisplay)     # Update after every 1 second and is recursion

    myLabel2.config(text=f'{week_name}, {day_decimal} {month} \n{timezone}')


# Display Labels
myLabel1 = Label(text='',  font=('Helvetica', 42), bg="black", fg="green")
myLabel1.pack()

myLabel2 = Label(text='',  font=('Helvetica', 24), bg="black", fg="green")
myLabel2.pack(ipadx=11)

updateDisplay()

root.mainloop()
