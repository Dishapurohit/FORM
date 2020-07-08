'''
Author : Disha Purohit
date : 6 July
purpose : Cloud Stack Task
'''


import pipreqs
import tkinter as tk
import sqlite3
from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk
from functools import partial

def validateSignUp(FirstName, LastName, Email, Password, ConfirmPassword):
    print("First Name entered :", FirstName.get())
    print("Last Name entered :", LastName.get())
    print("Email entered :", Email.get())
    print("Password entered :", Password.get())
    print("Password Confirm entered :", ConfirmPassword.get())
    return

def validateLogin(Email, Password, ConfirmPassword):
    print("Email entered :", Email.get())
    print("Password entered :", Password.get())
    print("Password Confirm entered :", ConfirmPassword.get())
    return

root = Tk()
root.geometry('1500x1500')
root.title('Cloud Stack Group')

image = Image.open("C:/Users/DIsha Purohit/Downloads/0.png")
Photo = ImageTk.PhotoImage(image)

lab=Label(image=Photo)
lab.pack()

def database():
    FirstName = FirstName1.get()
    LastName = LastName1.get()
    Email = Email1.get()
    Password = Password1.get()
    ConfirmPassword = ConfirmPassword1.get()

    connect = sqlite3.connect('Form.db')
    print("The database has created in DB-browser")
    with connect:
        cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS CandidateInfo(First Name TEXT, Last Name TEXT, Email TEXT, Password TEXT, Password Confirm TEXT )")
    cursor.execute("INSERT INTO CandidateInfo VALUES(First Name, Last Name, Email, Password, ConfirmPassword ) "
               "VALUES(?, ?, ?, ?, ?, ?)",(FirstName1, LastName1, Email1, Password1, ConfirmPassword1))
    connect.commit()

    tkinter.messagebox.showinfo("Welcome",'user is successfully Signed up !!')
    tkinter.messagebox.showinfo("Welcome",'user is successfully  Loged in !!')

FirstName1 = StringVar()
LastName1 = StringVar()
Email1 = StringVar()
Password1 = StringVar()
ConfirmPassword1 = StringVar()

def exit1():
    exit()

menuBar=Menu()
root.config(menu=menuBar)

submenu1=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="Quit",command=quit)

def second_root():
    root = Tk()
    root.geometry('400x250')
    root.title('Cloud Stack Group')

    image = Image.open("C:/Users/DIsha Purohit/Downloads/0.png")
    Photo = ImageTk.PhotoImage(image)

    label1_02=Label(root, text = "SignUp completed", relief = "solid", font = ('arial',16,'bold'))
    label1_02.place(x = 50, y = 50)
    button_1 = Button(root, text = "Done", width = 12, fg = "blue", bg = "red", command = exit1)
    button_1.place(x = 100, y = 100)

def fourth_root():
    root = Tk()
    root.geometry('400x250')
    root.title('Cloud Stack Group')

    image = Image.open("C:/Users/DIsha Purohit/Downloads/0.png")
    Photo = ImageTk.PhotoImage(image)

    label1_02 = Label(root, text="Login completed", relief="solid", font=('arial', 16, 'bold'))
    label1_02.place(x=50, y=50)
    button_1 = Button(root, text="Done", width=12, fg="blue", bg="red", command=exit1)
    button_1.place(x=100, y=100)

label = Label(root,text = "Welcome To Cloud Stack Group", fg = "blue", bg = "Black", font = ("arial",30,"bold"))
label.place(x = 400, y = 180)

FirstNamelabel = Label(root,text = "First Name  ", fg = "blue", bg = "white", font = ("arial",10,"bold"))
FirstNamelabel.place(x = 550, y = 250)
FirstName = StringVar()
FirstNameentry = Entry(root, textvar = FirstName)
FirstNameentry.place(x = 750, y = 250)

LastNamelable = Label(root, text = "Last Name  ", fg = "blue", bg = "white", font = ("arial",10,"bold"))
LastNamelable.place(x = 550, y = 300)
LastName = StringVar()
LastNameentry = Entry(root, textvar = LastName)
LastNameentry.place(x = 750, y = 300)

Emaillabel = Label(root, text = "Email  ", fg = "blue", bg = "white", font = ("arial",10,"bold"))
Emaillabel.place(x = 550,y = 350)
Email = StringVar()
Emailentry = Entry(root, textvar = Email)
Emailentry.place(x = 750, y = 350)

Passwordlabel = Label(root, text = "Password  ", fg = "blue", bg = "white", font = ("arial",10,"bold"))
Passwordlabel.place(x = 550,y = 400)
Password = StringVar()
Passwordentry = Entry(root, textvar = Password, show='*')
Passwordentry.place(x = 750, y = 400)

ConfirmPasswordlabel = Label(root, text = "Password Confirm  ", fg = "blue", bg = "white", font = ("arial",10,"bold"))
ConfirmPasswordlabel.place(x = 550,y = 450)
ConfirmPassword = StringVar()
ConfirmPasswordentry = Entry(root, textvar = ConfirmPassword, show='*')
ConfirmPasswordentry.place(x = 750, y = 450)


validateSignUp = partial(validateSignUp,FirstName,LastName,Email,Password,ConfirmPassword )

SignUpButton = Button(root, text="SignUp", width=12, fg="blue", bg="red",command=database)
SignUpButton.place(x = 550, y = 500)
root.bind("<Return>",database)

Quitbutton=Button(root, text = "Quit", width = 12, fg = "blue", bg = "red", command = exit1)
Quitbutton.place(x = 750, y = 500)

label = Label(root,text = "If you have already an account", fg = "blue", bg = "orange", font = ("arial",10,"bold"))
label.place(x = 545, y = 550)

validateLogin = partial(validateLogin, Email, Password, ConfirmPassword)

Loginbutton = Button(root, text="Login", width=12, fg="blue", bg="red", command=database)
Loginbutton.place(x=755, y=550)
root.bind("<Return>",database)

def validateLogin():
    root = Tk()
    root.geometry('400x250')
    root.title('Cloud Stack Group')

    image = Image.open("C:/Users/DIsha Purohit/Downloads/0.png")
    Photo = ImageTk.PhotoImage(image)

    Loginbutton = Button(root, text="Login", width=12, fg="blue", bg="red", command=database)
    Loginbutton.place(x=755, y=550)

    Emaillabel = Label(root, text="Email  ", fg="blue", bg="white", font=("arial", 10, "bold"))
    Emaillabel.place(x=550, y=350)
    Email = StringVar()
    Emailentry = Entry(root, textvar=Email)
    Emailentry.place(x=750, y=350)

    Passwordlabel = Label(root, text="Password  ", fg="blue", bg="white", font=("arial", 10, "bold"))
    Passwordlabel.place(x=550, y=400)
    Password = StringVar()
    Passwordentry = Entry(root, textvar=Password, show='*')
    Passwordentry.place(x=750, y=400)

    ConfirmPasswordlabel = Label(root, text="Password Confirm  ", fg="blue", bg="white", font=("arial", 10, "bold"))
    ConfirmPasswordlabel.place(x=550, y=450)
    ConfirmPassword = StringVar()
    ConfirmPasswordentry = Entry(root, textvar=ConfirmPassword, show='*')
    ConfirmPasswordentry.place(x=750, y=450)

root.mainloop()