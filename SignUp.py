from tkinter import *
import pymysql
from tkinter import messagebox
from PIL import ImageTk,Image
import time
import ast

root=Tk()
root.geometry('925x500+300+200')
root.title("SignUp")
root.configure(bg='#fff')
root.resizable(False,False)
root.iconbitmap('2.ico')

def clear():
    user.delete(0,'end')
    code.delete(0,'end')
    conform_code.delete(0,'end')
    
def signup():
    if (user.get()=='') or (code.get()=='') or (conform_code.get()==''):
        messagebox.showerror('ERROR','All Fields Are Required')
    elif code.get()!= conform_code.get():
        messagebox.showerror('ERROR','Password Mismatch')
    else:
        try:        
            con=pymysql.connect(host='localhost',user='root',password='Admin@123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue TRY AGAIN')
            return
    try:
        query='create database Pasupathy'
        mycursor.execute(query)
        query='use hospitall'
        mycursor.execute(query)
        query='create table datas(Id int auto_increment primary key not null,Username varchar(100),Password varchar(50))'
        mycursor.execute(query)
    except:
        mycursor.execute('use hospitall')

    query='select * from datas where username=%s'
    mycursor.execute(query,(user.get()))

    row=mycursor.fetchone()

    if row !=None:
        messagebox.showerror('Error','User name already exists')

    else:
        query='insert into datas(Username,Password)values(%s,%s)'
        mycursor.execute(query,(user.get(),code.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Account Created Successfully')
        clear()

def sign():
    root.destroy()
    import SignIn
    
#=======left======add image==========
i=PhotoImage(file='images\s3.png')
Label(root,image=i,bg='white').place(x=110,y=110)

#========right====frame set=========

frame=Frame(root,bg='white',width=350,height=390)
frame.place(x=480,y=50)

heading=Label(frame,text="Sign Up",fg='#57a1f8',bg='white',font=('microsoft yahei UI light',23,'bold'))
heading.place(x=100,y=5)

#==============user name=====================

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'username')
        
user=Entry(frame,width=25,border=0,fg="black",bg='white',font=('microsoft yahei UI light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

#=================password==============================

def on_enter(e):
    code.delete(0,'end')

def off_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
        
code = Entry(frame,width=25,border=0,fg="black",bg='white',font=('microsoft yahei UI light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

#===================conform password===============================

def on_enter(e):
    conform_code.delete(0,'end')

def on_leave(e):
    if conform_code.get()=='':
        conform_code.insert(0,'Conform Password')

conform_code = Entry(frame,width=25,border=0,font=('microsoft yahei UI light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0,'Conform Password')
conform_code.bind('<FocusIn>',on_enter)
conform_code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)

#===========sign up button============================================

signup_button=Button(frame,width=39,pady=7,text="Sign up",bg='#57a1f8',fg='white',cursor='hand2',border=0,command=signup)
signup_button.place(x=35,y=280)

label=Label(frame,text="I have an account?",fg='red',bg='white',font=('microsoft yahei UI light',9))
label.place(x=90,y=340)

signin_button=Button(frame,width=6,text="Sign in",fg='#57a1f8',bg='white',cursor='hand2',border=0,command=sign)
signin_button.place(x=200,y=340)

root.mainloop()
