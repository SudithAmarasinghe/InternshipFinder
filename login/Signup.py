from tkinter import *
from tkinter import messagebox
import pymysql

from PIL import ImageTk

signup_window = Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
signup_window.geometry('500x500+300+200')
signup_window.configure(bg="#fff")
#img1= ImageTk.PhotoImage(file='OIP.jpg')



frame=Frame(signup_window,width=350,height=350,bg="#fff")
frame.place(x=80,y=30)

heading = Label(frame, text="Create an Account", font=('calibri(body)',26,'bold'),bd=0, bg="white", fg="#68aced" )
heading.grid(row=0, column=0, padx=10, pady=10)

def onuser_enter(e):
    usernameEntry.delete(0, 'end')

def onuser_leave(e):
    name=usernameEntry.get()
    if name=='':
        usernameEntry.insert(0,'User Name')


usernameEntry = Entry(frame,width=42, borderwidth=1, font=('calibri(body)',11), bg="#fff" ,fg="black")
usernameEntry.grid(row=2, column=0, sticky='w', padx=10, pady=15)


usernameEntry.insert(0,'User Name')
usernameEntry.bind('<FocusIn>', onuser_enter)
usernameEntry.bind('<FocusOut>', onuser_leave)

def onpass_enter(e):
    passwordEntry.delete(0,'end')

def onpass_leave(e):
    password = passwordEntry.get()
    if password== '':
        passwordEntry.insert(0,'Password')


passwordEntry = Entry(frame,width=42, borderwidth=1, font=('calibri(body)',11), bg="#fff" ,fg="black")
passwordEntry.grid(row=4, column=0, sticky='w', padx=10, pady=15)


passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>', onpass_enter)
passwordEntry.bind('<FocusOut>', onpass_leave)

def oncpass_enter(e):
   confirmpassEntry.delete(0,'end')
def oncpass_leave(e):
  cpass=confirmpassEntry.get()
  if cpass=='':
        confirmpassEntry.insert(0,'Confirm Password')


confirmpassEntry = Entry(frame,width=42, borderwidth=1, font=('calibri(body)',11), bg="#fff" ,fg="black")
confirmpassEntry.grid(row=6, column=0, sticky='w', padx=10, pady=15)

confirmpassEntry.insert(0,'Confirm Password')
confirmpassEntry.bind('<FocusIn>', oncpass_enter)
confirmpassEntry.bind('<FocusOut>', oncpass_leave)

check = IntVar()
conditions = Checkbutton(frame, width=39, text='I agree to the terms and conditions', font=('calibri(body)',10), fg='black', cursor='hand2', variable=check)
conditions.grid(row=7,column=0, padx=10, pady=15)

def clear():
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpassEntry.delete(0,END)
    check.set(0)

def signup_user():
    if usernameEntry.get() == '' or passwordEntry.get()=='' or confirmpassEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get() != confirmpassEntry.get():
        messagebox.showerror('Error', 'Password and confirm Password does not match' )
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms and Conditions')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='', database='internship database')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','DataBase connectivity Issue, please Try Again')
            return


        query = "SELECT * FROM `login_data` WHERE UserName=%s"
        mycursor.execute(query, (usernameEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username already exist')
            clear()
        else:
            query = "INSERT INTO `login_data`(`UserName`, `Password`) VALUES (%s,%s )"
            mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is Successful!')
            signup_window.destroy()
            import login

SignupButton = Button(frame, text='Sign Up', width=17,font=('calibri(body)',15, 'bold'), bd=0, bg="#68aced" ,fg="#fff",
                      activebackground="#68aced", activeforeground="#fff", command=signup_user, cursor='hand2')
SignupButton.grid(row=8,column=0,pady=20, padx=10)

alreadyaccount = Label(frame, width=50, text="If you have an account                                                   " ,
                       font=('calibri(body)',9) ,bg="#fff", fg="black")
alreadyaccount.grid(column=0,row=10,pady=15)


loginButton = Button(frame, text='login', width=10, font=('calibri(body)',10, 'bold'),borderwidth=0, bg='#fff', fg='blue', activeforeground='blue', activebackground='#fff')
loginButton.place(x=180,y=363)



#userimage = Label(frame,image=img1)
#userimage.grid(row=2, column=0)

signup_window.mainloop()