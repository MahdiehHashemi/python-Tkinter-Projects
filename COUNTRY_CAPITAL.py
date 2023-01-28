from tkinter import Tk,simpledialog,messagebox
root=Tk()
root.withdraw()
from random import *

a= open("C:/Users/Mahdieh/Desktop/python/read and write/country.txt","r")
b= open("C:/Users/Mahdieh/Desktop/python/read and write/capital.txt","r")
b=b.read()
b = b.split("\n")
print(b[randint(0,8)])
a=a.read()
a = a.split("\n")
print(a[randint(0,8)])
query=simpledialog.askstring('country','type the name of a country')
query=query.capitalize()
if query in a:
    ans=b[a.index(query)]
    messagebox.showinfo('Answer','capital city of '+ query +' is '+ ans)
else:
    a= open("C:/Users/Mahdieh/Desktop/python/read and write/country.txt","a")
    a.write("\n"+query)
    b= open("C:/Users/Mahdieh/Desktop/python/read and write/capital.txt","a")
    c=simpledialog.askstring('teach me','teach me what is the capital city of '+ query)
    b.write("\n"+c)