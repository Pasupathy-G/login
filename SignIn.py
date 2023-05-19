from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import mysql.connector
import os
os.getcwd()

root=Tk()
root.iconbitmap('1.ico')

root.geometry('925x500+300+200')
root.title('Login')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    my=mysql.connector.connect(host='localhost',user='root',password='Admin@123',database='Pasupathy')
    mycursor=my.cursor()

    username=user.get()
    password=code.get()

    sql='select * from datas where Username=%s and Password=%s'
    mycursor.execute(sql,[(username),(password)])
    results=mycursor.fetchall()
    
    if results:
        messagebox.showinfo("login","Login success")
        print("Login success")
        root.destroy()
    else:
       messagebox.showinfo("Error","Incorrect username and password")


def signup():
    root.destroy()
    import SignUp

#===================Add Image=================================
img=PhotoImage(file='images\s1.png')
Label(root,image=img,bg='white').place(x=80,y=80)

#====================Sign in heading====================================

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('microsoft yahei UI light',23,'bold'))
heading.place(x=100,y=5)
#==============================================

def enter(e):
    user.delete(0,'end')

def leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,border=0,fg='black',bg='white',font=('microsoft yahei UI light',11))
user.place(x=30,y=80)
user.insert(0,'user_name')
user.bind("<FocusIn>",enter)
user.bind("<FocusOut>",leave)

Frame(frame,width=295,bg='black').place(x=25,y=107)

#=================================================

def on_enter(e):
    code.delete(0,"end")

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'password')

code=Entry(frame,width=25,border=0,fg='black',bg='white',font=('microsoft yahei UI light',11),show='*')
code.place(x=30,y=150)
code.insert(0,'your_password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,bg='black').place(x=25,y=177)

#==================================================

sign_in=Button(frame,border=0,width=39,pady=7,text="Sign in",bg='#57a1f8',fg='white',cursor='hand2',command=signin)
sign_in.place(x=35,y=204)

label=Label(frame,text="Dont't have an account?",fg='red',bg='white',font=('microsoft yahei UI light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup)
sign_up.place(x=215,y=270)

#======destroy the window after 5mins=========
root.after(50000,lambda:root.destroy())
#==========================================
root.mainloop()
