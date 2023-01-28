from tkinter import *

w = Tk()
hh = StringVar()
ww = StringVar()

w.configure(width = 500 ,height = 500)
h = Label(text="Enter your height in meter ",font=("Monotype Corsiva",15)).place(x=50, y=50)
w = Label(text="Enter your weight in kilograms ",font=("Monotype Corsiva",15)).place(x=50, y=80)

getheight = Entry(text = hh).place(x=245,y=60)
getweight = Entry(text = ww).place(x=274,y=85)

def calculate():

    hhh = float(hh.get()) **2
    BMI = float(ww.get()) / hhh

    if BMI <= 18.5:
        a = Label(text = "Your BMI is "+ str(BMI)+"\n You are Underweight !",font=("b titr",10)).place(x=200,y=200)
    elif BMI > 18.5 and BMI <= 25:
        a = Label(text = "Your BMI is "+ str(BMI)+"\n You are Normal !",font=("b titr",10)).place(x=200,y=200)
    elif BMI > 25 and BMI <= 30:
        a = Label(text = "Your BMI is "+ str(BMI)+"\n You are Overweight !",font=("b titr",10)).place(x=200,y=200)
    elif BMI > 30 and BMI <= 35:
        a = Label(text = "Your BMI is "+ str(BMI)+"\n You are Obese !",font=("b titr",10)).place(x=200,y=200)
    elif BMI >= 35:
        a = Label(text = "Your BMI is "+ str(BMI)+"\n You are Extremely Obese !",font=("b titr",10)).place(x=200,y=200)

Button(text="calculate !",font=("b titr",13),command=calculate).place(x=100,y=150)
mainloop()
