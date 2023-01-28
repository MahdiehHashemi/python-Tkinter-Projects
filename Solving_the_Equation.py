from tkinter import *
import sympy as sy
from tkinter import messagebox

w= Tk()
a = StringVar()
b = StringVar()
c=StringVar()

w.configure(bg="light gray",height=300,width=400)

def solve():
    x=sy.symbols("x")
    e1=sy.Eq(int(a.get()) + int(b.get())*x ,int(c.get()))
    z = sy.solve(e1,x)
    messagebox.showinfo("answer","The x is :"+str(z))




Label(text="Solving The Equation",font=("MV Boli",15),bg="lavender",fg="light sea green").place(x=110, y=25)
Button(text="Solve!", font=("Times New Roman", 15), command=solve).place(x=150,y=235)
Label(text="  A  + (B)x = C  ",font=("MV Boli",15),bg="misty rose",fg="light sea green").place(x=120, y=70)


Label(text=" A ",font=("MV Boli",15),fg="black").place(x=100, y=130)
aa=Entry(text=a,font=("Comic Sans MS",8)).place(x=150,y=135)

Label(text=" B ",font=("MV Boli",15),fg="black").place(x=100, y=165)
bb=Entry(text=b,font=("Comic Sans MS",8)).place(x=150,y=173)

Label(text=" C ",font=("MV Boli",15),fg="black").place(x=100, y=200)
cc=Entry(text=c, font=("Comic Sans MS",8)).place(x=150,y=205)




mainloop()