from tkinter import *
from datetime import datetime
from tkinter import messagebox

w= Tk()
w.configure(bg="light salmon",height=300,width=400)

de = StringVar()
me = StringVar()
ye = StringVar()

def calculate_age():
	if yeare.get():
		present = datetime.now().year
		age = present - int(yeare.get())
		messagebox.showinfo("calculator","Your age is:"+str(age))

Label(text="~AGE CALCULATOR~",font=("MV Boli",15),bg="light pink",fg="light sea green").place(x=120, y=25)
Button(text="Calculate Age!", font=("Times New Roman", 15), command=calculate_age).place(x=150,y=235)


Label(text="Enter your day of b'day: ",font=("Constantia",13),bg="cornsilk",fg="maroon").place(x=25, y=100)
daye=Entry(font=("Arial", 10))
daye.place(x=250,y=105)

Label(text="Enter your month of b'day: ",font=("Constantia",13),bg="cornsilk",fg="maroon").place(x=25, y=130)
monthe=Entry(font=("Arial", 10))
monthe.place(x=250,y=135)

Label(text="Enter your year of b'day: ",font=("Constantia",13),bg="cornsilk",fg="maroon").place(x=25, y=160)
yeare=Entry(font=("Arial", 10))
yeare.place(x=250,y=165)

mainloop()