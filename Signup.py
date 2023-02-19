from tkinter import *
import customtkinter
import messagebox
import pymysql
from PIL import ImageTk

customtkinter.set_default_color_theme("Design.json")
customtkinter.set_appearance_mode("light")
#customtkinter.set_appearance_mode("dark")


signup_window = customtkinter.CTk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
signup_window.geometry('500x550+300+200')

def signup_user():
    if entry_1.get() == '' or entry_2.get()=='' or entry_3.get()=='':
        messagebox.showerror('Error', 'All fields are required')
    elif entry_2.get() != entry_3.get():
        messagebox.showerror('Error', 'Password and confirm Password does not match' )
    elif checkbox_1.get()==0:
        messagebox.showerror('Error','Please accept Terms and Conditions')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','DataBase connectivity Issue, please Try Again')
            return
        try:
            query = "CREATE DATABASE userdata"
            mycursor.execute(query)
            query = "USE userdata"
            mycursor.execute(query)
            query = "CREATE TABLE data(UserName varchar(50) primary key not null, Password varchar(20))"
            mycursor.execute(query)
        except:
            mycursor.execute("use userdata")

        query = "SELECT * FROM `data` WHERE UserName=%s"
        mycursor.execute(query, (entry_1.get()))

        row = mycursor.fetchone()
        if row != None:
                 messagebox.showerror('Error', 'Username already exist')
                 clear()
        else:
              query = "INSERT INTO `data`(`UserName`, `Password`) VALUES (%s,%s )"
              mycursor.execute(query, (entry_1.get(), entry_2.get()))
              con.commit()
              con.close()
              messagebox.showinfo('Success', 'Registration is Successful!')
              clear()
              signup_window.destroy()
              import login

def login():
        import main

#def password_Validate():
   # if entry_2.get

def clear():
    entry_1.delete(0,20)
    entry_2.delete(0,20)
    entry_3.delete(0,20)

def hide1():
    openeye.config(file='closed.png')
    entry_2.configure(show='*')
    eyeButton1.config(command=show1)

def hide2():
    openeye2.config(file='closed.png')
    entry_3.configure(show='*')
    eyeButton2.config(command=show2)

def show1():
    openeye.config(file='openeye.png')
    entry_2.configure(show='')
    eyeButton1.config(command=hide1)

def show2():
    openeye2.config(file='openeye.png')
    entry_3.configure(show='')
    eyeButton2.config(command=hide2)

frame = customtkinter.CTkFrame(master=signup_window,corner_radius=10)
frame.place(x=55,y=30)

label_topic = customtkinter.CTkLabel(master=frame,text="Create an Account",width=120,font=("Arial" , 30, 'bold'))
label_topic.grid(row=0, column=1, padx=(30,20), pady=8)


entry_1 = customtkinter.CTkEntry(frame, placeholder_text="Enter User Name: " ,height=40)
entry_1.grid(row=3, column=1, padx=(20, 20), pady=(20, 10), sticky="nsew")

entry_2 = customtkinter.CTkEntry(frame, placeholder_text="Enter Password: " ,height=40)
entry_2.grid(row=6, column=1, padx=(20, 20), pady=(20, 10), sticky="nsew")

openeye = PhotoImage(file='openeye.png')
eyeButton1 = Button(frame,image=openeye,bd=0, bg='#E8E8E8',cursor='hand2',command=hide1)
eyeButton1.grid(row=6,column=2, pady=0,padx=(0,10))

entry_3 = customtkinter.CTkEntry(frame, placeholder_text="Confirm Password : " ,height=40)
entry_3.grid(row=9, column=1, padx=(20, 20), pady=(20, 10), sticky="nsew")

openeye2 = PhotoImage(file='openeye.png')
eyeButton2 = Button(frame,image=openeye2,bd=0, bg='#E8E8E8',cursor='hand2', command=hide2)
eyeButton2.grid(row=9,column=2, pady=0, padx=(0,10))

checkbox_1 = customtkinter.CTkCheckBox(master=frame, text="I agree to the terms and conditions")
checkbox_1.grid(row=12, column=1, pady=(20, 10), padx=10, sticky="n")

main_button_1 = customtkinter.CTkButton(master=frame, fg_color="#68aced", border_width=0, font=('Arial', 20, 'bold') ,text_color=("white") , height=40, text="Sign Up", command=signup_user)
main_button_1.grid(row=15, column=1, padx=(20, 20), pady=(20, 10), sticky="nsew")

sub_frame = customtkinter.CTkFrame(master=frame, fg_color="transparent")
sub_frame.grid(row=17, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

label_topic = customtkinter.CTkLabel(master=sub_frame, text="If you have an Account?",width=100,font=("Arial" , 12), text_color="black")
label_topic.grid(row=17, column=1, padx=(20,20), pady=(10, 20))

main_button_2= customtkinter.CTkButton(master=sub_frame, fg_color="transparent", text_color="blue", text="Login", font=("Arial" , 12, 'underline'), hover_color="#E8E8E8", command=login)
main_button_2.grid(row=17, column=2, padx=(20, 20), pady=(10, 20), sticky="nsew")

signup_window.mainloop()