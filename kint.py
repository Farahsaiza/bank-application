from tkinter import*
import random
import tkinter as tk
from tkinter import ttk



    





root = Tk()
root.title("account creation")
root.geometry("500x500")

global  e1
global  e2
global  e3
global  e4
global  e5
global  e6







number=0
num = Label(root,text = "Number : ")
num.place (x=10,y=10)
number1= Label(root,text=number)
number1.place(x=100,y=10)

user = Label(root,text="user :")
user.place( x=10 , y=40)
e2= Entry(root)
e2.place(x=100,y=40,width=200)

Solde= Label(root,text="current solde :")
Solde.place( x=10 , y=70)
eurro= Label(root, text="Euro €")
eurro.place(x=300,y=70)
e3= Entry(root)
e3.place(x=100,y=70,width=200)

#choice methode

e4= tk.StringVar()
e4.set("current saving")

def choice_var():
    accout_type=e4.get()
    if  accout_type== "current":
        e5.config(state=tk.DISABLED)
        e6.config(state=tk.NORMAL)

    else:
        e5.config(state=tk.NORMAL)
        e6.config(state=tk.DISABLED)







Type = Label(root,text="Type :")
Type.place(x=10 ,y=100)
e4 = StringVar()
current = Radiobutton(root,text="current" ,variable= e4, value="current", command=choice_var )
current.place(x=90,y=100)
saving = Radiobutton(root,text="saving",variable= e4, value="saving", command=choice_var)
saving.place(x=170,y=100)






Taux = Label(root,text="Taux Interet :")
Taux.place( x=10 , y=140)
e5= Entry(root)
e5.place(x=100,y=140,width=200)
pourc=  Label(root,  text="%")
pourc.place(x=300 , y=140)

 
M = Label(root,text="M.Decouvert :")
M.place( x=10 , y=170)
e6= Entry(root)
e6.place(x=100,y=170,width=200)
 

#click= tk.StringVar




table = ttk.Treeview(root, columns=('number','user' , 'solde'  , 'type'  , 'taux', 'montant')  , show='headings')
table.heading('number' , text=  ' number')
table.heading('user' , text= ' user')
table.heading('solde' , text= ' solde initial')
table.heading('type' , text= ' type')
table.heading('taux' , text= ' Taux Interet')
table.heading('montant' , text= ' montant decouvert')
table.pack(padx=100 , pady=230)


def add():
    global number
    number=number+1
    number1.config(text=number)

    user=e2.get()
    solde=e3.get()
    type=e4.get()
    t=e5.get()
    md=e6.get()
    table.insert("",'end', values=( number, user , solde, type , t, md))


b=Button( root, text="account creation" , command=add)
b.place (x=100, y=200)







root.mainloop()

