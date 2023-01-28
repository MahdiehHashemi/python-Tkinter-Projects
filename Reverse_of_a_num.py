from tkinter import *
from tkinter import messagebox

w= Tk()
a=StringVar()
w.configure(bg="light steel blue",height=200,width=300)

Label(text="Enter a number",font=("Segoe Print",18),bg="light steel blue",fg="midnight blue").place(x=60, y=48)
a = Entry(font=("Arial", 10))
a.place(x=75,y=95)

def rev():
    b = int(str(a.get())[::-1])

    messagebox.showinfo("reversed","Reversed number is : "+str(b))


Button(text="Reverse The Number !",font=("Comic Sans MS",11),bg="tan",command=rev).place(x=70,y=135)

mainloop()
