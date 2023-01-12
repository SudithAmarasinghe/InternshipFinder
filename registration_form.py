import customtkinter

def slider_event(value):
    print(value)

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

customtkinter.set_default_color_theme("custom_theme.json")
customtkinter.set_appearance_mode("light")
#customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.geometry(f"{1520}x{780}+{0}+{0}")
root.title("Internship Finder")

frame0 = customtkinter.CTkFrame(master=root,corner_radius=10,height=50)
frame0.grid(row=0, column=0,padx=20, pady=(5,0), columnspan=3, sticky="new")

label_organization = customtkinter.CTkLabel(master=frame0,text="IntellWarriors", anchor="w",width=120,font=("Arial",22))
label_organization.grid(row=0, column=0, padx=20, pady=8)

label_topic = customtkinter.CTkLabel(master=frame0,text="Details Submission Form",width=120,font=("Arial",22))
label_topic.grid(row=0, column=1, padx=(417,20), pady=8)

label_username = customtkinter.CTkLabel(master=frame0,text="Nadun Hirushan",width=120,font=("Arial",22))
label_username.grid(row=0, column=2, padx=(330,20), pady=8)

logout_button = customtkinter.CTkButton(master=frame0,width=70,height=30,border_width=0, corner_radius=8,text="Sign Out",font=("Arial",17))
logout_button.grid(row=0, column=3, padx=(10,0), pady=5,sticky="e")
#---------------------------------------------------------------------------------------------------------------------------

frame1 = customtkinter.CTkFrame(master=root,corner_radius=10)
frame1.grid(row=1, column=0,padx=20, pady=(10,15))

label_profile = customtkinter.CTkLabel(master=frame1,text="Profile Details",fg_color=("#68aced","#1f538d"),width=400,height=30,corner_radius=8,font=("Arial",20))
label_profile.grid(row=0, column=0, columnspan=2, padx=10, pady=(20,5))

label_name = customtkinter.CTkLabel(master=frame1,text="Name",anchor="w",width=120,font=("Arial",17))
label_name.grid(row=1, column=0, padx=20, pady=8)
textbox_name = customtkinter.CTkTextbox(master=frame1,width=250,height=5,font=("Arial",17))
textbox_name.grid(row=1, column=1, padx=(10,20), pady=5)

label_uni_id = customtkinter.CTkLabel(master=frame1,text="University ID",anchor="w",width=120,font=("Arial",17))
label_uni_id.grid(row=2, column=0, padx=20, pady=8)
textbox_uni_id = customtkinter.CTkTextbox(master=frame1,width=250,height=5,font=("Arial",17))
textbox_uni_id.grid(row=2, column=1, padx=(10,20), pady=5)

label_gender = customtkinter.CTkLabel(master=frame1,text="Gender",anchor="w",width=120,font=("Arial",17))
label_gender.grid(row=3, column=0, padx=20, pady=8)
textbox_gender = customtkinter.CTkTextbox(master=frame1,width=250,height=5,font=("Arial",17))
textbox_gender.grid(row=3, column=1, padx=(10,20), pady=5)

label_email = customtkinter.CTkLabel(master=frame1,text="Email",anchor="w",width=120,font=("Arial",17))
label_email.grid(row=4, column=0, padx=20, pady=8)
textbox_email = customtkinter.CTkTextbox(master=frame1,width=250,height=5,font=("Arial",17))
textbox_email.grid(row=4, column=1, padx=(10,20), pady=5)

label_tel = customtkinter.CTkLabel(master=frame1,text="Telephone",anchor="w",width=120,font=("Arial",17))
label_tel.grid(row=5, column=0, padx=10, pady=8)
textbox_tel = customtkinter.CTkTextbox(master=frame1,width=250,height=5,font=("Arial",17))
textbox_tel.grid(row=5, column=1, padx=(10,20), pady=(5,15))

#--------------------------------------------------------------------------------------------------------------------------------------
frame2 = customtkinter.CTkFrame(master=root,corner_radius=10)
frame2.grid(row=2, column=0,padx=20, pady=(0,15))

label_link = customtkinter.CTkLabel(master=frame2,text="Profile Details",fg_color=("#68aced","#1f538d"),width=400,height=30,corner_radius=8,font=("Arial",20))
label_link.grid(row=0, column=0, columnspan=2, padx=10, pady=(20,5))

label_linkedin = customtkinter.CTkLabel(master=frame2,text="Linkedin",anchor="w",width=120,font=("Arial",17))
label_linkedin.grid(row=1, column=0, padx=20, pady=8)
textbox_linkedin = customtkinter.CTkTextbox(master=frame2,width=250,height=5,font=("Arial",17))
textbox_linkedin.grid(row=1, column=1, padx=(10,20), pady=5)

label_github = customtkinter.CTkLabel(master=frame2,text="GitHub",anchor="w",width=120,font=("Arial",17))
label_github.grid(row=2, column=0, padx=20, pady=8)
textbox_github = customtkinter.CTkTextbox(master=frame2,width=250,height=5,font=("Arial",17))
textbox_github.grid(row=2, column=1, padx=(10,20), pady=5)

label_other_link = customtkinter.CTkLabel(master=frame2,text="Other",anchor="w",width=120,font=("Arial",17))
label_other_link.grid(row=3, column=0, padx=10, pady=8)
textbox_other_link = customtkinter.CTkTextbox(master=frame2,width=250,height=5,font=("Arial",17))
textbox_other_link.grid(row=3, column=1, padx=(10,20), pady=(5,15))

#--------------------------------------------------------------------------------------------------------------------------------
frame3 = customtkinter.CTkFrame(master=root,corner_radius=10,height=300)
frame3.grid(row=3, column=0,padx=20, pady=(0,15),sticky="n")

label_language = customtkinter.CTkLabel(master=frame3,text="Languages",fg_color=("#68aced","#1f538d"),width=400,height=30,corner_radius=8,font=("Arial",20))
label_language.grid(row=0, column=0, columnspan=2, padx=10, pady=(20,5))

label_english = customtkinter.CTkLabel(master=frame3,text="English",anchor="w",width=120,font=("Arial",17))
label_english.grid(row=1, column=0, padx=20, pady=8)
slider_english = customtkinter.CTkSlider(master=frame3,width=250,number_of_steps=5, from_=0, to=100, command=slider_event)
slider_english.grid(row=1, column=1, padx=(10,20), pady=5)

label_sinhala = customtkinter.CTkLabel(master=frame3,text="Sinhala",anchor="w",width=120,font=("Arial",17))
label_sinhala.grid(row=2, column=0, padx=20, pady=8)
slider_sinhala = customtkinter.CTkSlider(master=frame3,width=250, number_of_steps=5, from_=0, to=100, command=slider_event)
slider_sinhala.grid(row=2, column=1, padx=(10,20), pady=5)

label_tamil = customtkinter.CTkLabel(master=frame3,text="Tamil",anchor="w",width=120,font=("Arial",17))
label_tamil.grid(row=3, column=0, padx=20, pady=8)
slider_tamil = customtkinter.CTkSlider(master=frame3,width=250, number_of_steps=5, from_=0, to=100, command=slider_event)
slider_tamil.grid(row=3, column=1, padx=(10,20), pady=5)


#-------------------------------------------------------------------------------------------------------------------------------------

frame4 = customtkinter.CTkFrame(master=root,corner_radius=10)
frame4.grid(row=1, column=1, pady=(10,20), sticky="new")

label_education = customtkinter.CTkLabel(master=frame4,text="Education Details",fg_color=("#68aced","#1f538d"),width=600,height=30,corner_radius=8,font=("Arial",20))
label_education.grid(row=0, column=0, columnspan=2, padx=10, pady=(20,5))

label_university = customtkinter.CTkLabel(master=frame4,text="University",anchor="w",width=120,font=("Arial",17))
label_university.grid(row=1, column=0, padx=20, pady=8)
university_list=["University of Colombo", "University of Peradeniya","University of Sri Jayewardenepura", "University of Kelaniya",
                 "University of Moratuwa","University of Jaffna","University of Ruhuna","The Open University of Sri Lanka",
                 "Eastern University, Sri Lanka","South Eastern University of Sri Lanka","Rajarata University of Sri Lanka",
                 "Sabaragamuwa University of Sri Lanka","Wayamba University of Sri Lanka","Uva Wellassa University of Sri Lanka",
                 "University of the Visual & Performing Arts","Gampaha Wickramarachchi University of Indigenous Medicine",
                 "University of Vavuniya"]
combobox_university = customtkinter.CTkOptionMenu(master=frame4,values=university_list,width=450,height=35,font=("Arial",17),
                                       command=optionmenu_callback)
combobox_university.grid(row=1, column=1, padx=(10,20), pady=5, ipady=1)
combobox_university.set("  --Select the University--")

label_degree = customtkinter.CTkLabel(master=frame4,text="Degree",anchor="w",width=120,font=("Arial",17))
label_degree.grid(row=2, column=0, padx=20, pady=8)
degree_list=["Bachelor of Science Honours in Computer Science", "Bachelor of Science (Surveying Science)",
             "Bachelor of Arts General Degree (BA)"]
combobox_degree = customtkinter.CTkOptionMenu(master=frame4,values=degree_list,width=450,height=35,font=("Arial",17),
                                       command=optionmenu_callback)
combobox_degree.grid(row=2, column=1, padx=(10,20), pady=5, ipady=1)
combobox_degree.set("  --Select the Degree--")

label_gpa = customtkinter.CTkLabel(master=frame4,text="Current GPA",anchor="w",width=120,font=("Arial",17))
label_gpa.grid(row=3, column=0, padx=20, pady=8)
textbox_gpa = customtkinter.CTkTextbox(master=frame4,width=450,height=5,font=("Arial",17))
textbox_gpa.grid(row=3, column=1, padx=(10,20), pady=5)

label_project = customtkinter.CTkLabel(master=frame4,text="Projects",anchor="w",width=120,font=("Arial",17))
label_project.grid(row=5, column=0, padx=20, pady=8, sticky="n")
textbox_project = customtkinter.CTkTextbox(master=frame4,width=450,height=75,font=("Arial",17))
textbox_project.grid(row=5, column=1, padx=(10,20), pady=(5,15))

#-----------------------------------------------------------------------------------------------------------------------------

frame5 = customtkinter.CTkFrame(master=root,corner_radius=10)
frame5.grid(row=2, column=1, rowspan=2,pady=(0,20), sticky="new")

label_skill = customtkinter.CTkLabel(master=frame5,text="Skills",fg_color=("#68aced","#1f538d"),width=600,height=30,corner_radius=8,font=("Arial",20))
label_skill.grid(row=0, column=0, columnspan=3, padx=20, pady=(20,5))

"""def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())"""
def checkbox_event():
    print("checkbox toggled, current value:")


checkbox1 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox1.grid(row=1, column=0,padx=20, pady=10)

checkbox2 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox2.grid(row=1, column=1,padx=20, pady=10)

checkbox3 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox3.grid(row=1, column=2,padx=20, pady=10)

checkbox4 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox4.grid(row=2, column=0,padx=20, pady=10)

checkbox5 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox5.grid(row=2, column=1,padx=20, pady=10)

checkbox6 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox6.grid(row=2, column=2,padx=20, pady=10)

checkbox7 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox7.grid(row=3, column=0,padx=20, pady=10)

checkbox8 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox8.grid(row=3, column=1,padx=20, pady=10)

checkbox9 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox9.grid(row=3, column=2,padx=20, pady=10)

checkbox10 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox10.grid(row=4, column=0,padx=20, pady=(10,13))

checkbox11 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox11.grid(row=4, column=1,padx=20, pady=(10,13))

checkbox12 = customtkinter.CTkCheckBox(master=frame5, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox12.grid(row=4, column=2,padx=20, pady=(10,13))

label_other_skill = customtkinter.CTkLabel(master=frame5,text="Other Skills",anchor="w",width=120,font=("Arial",17))
label_other_skill.grid(row=5, column=0, padx=20, pady=8, sticky="n")
textbox_other_skill = customtkinter.CTkTextbox(master=frame5,width=450,height=65,font=("Arial",17))
textbox_other_skill.grid(row=5, column=1, columnspan=2, padx=(10,20), pady=5)

label_activity = customtkinter.CTkLabel(master=frame5,text="Activities",anchor="w",width=120,font=("Arial",17))
label_activity.grid(row=6, column=0, padx=20, pady=8, sticky="n")
textbox_activity = customtkinter.CTkTextbox(master=frame5,width=450,height=65,font=("Arial",17))
textbox_activity.grid(row=6, column=1, columnspan=2, padx=(10,20), pady=(10,15))

#------------------------------------------------------------------------------------------------------------------------------
frame6 = customtkinter.CTkFrame(master=root,corner_radius=10)
frame6.grid(row=1, column=2, padx=20, pady=(10,20), rowspan=2, sticky="new")

label_skill = customtkinter.CTkLabel(master=frame6,text="Interests",fg_color=("#68aced","#1f538d"),width=320,height=30,corner_radius=8,font=("Arial",20))
label_skill.grid(row=0, column=0, columnspan=2, padx=20, pady=(20,5))

checkbox13 = customtkinter.CTkCheckBox(master=frame6, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox13.grid(row=1, column=0,padx=20, pady=10)

checkbox15 = customtkinter.CTkCheckBox(master=frame6, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox15.grid(row=1, column=1,padx=20, pady=10)

checkbox16 = customtkinter.CTkCheckBox(master=frame6, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox16.grid(row=2, column=0,padx=20, pady=10)

checkbox17 = customtkinter.CTkCheckBox(master=frame6, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox17.grid(row=2, column=1,padx=20, pady=10)

checkbox18 = customtkinter.CTkCheckBox(master=frame6, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox18.grid(row=3, column=0,padx=20, pady=10)

checkbox19 = customtkinter.CTkCheckBox(master=frame6, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox19.grid(row=3, column=1,padx=20, pady=10)

checkbox20 = customtkinter.CTkCheckBox(master=frame6, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox20.grid(row=4, column=0,padx=20, pady=10)

checkbox21 = customtkinter.CTkCheckBox(master=frame6, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox21.grid(row=4, column=1,padx=20, pady=10)

checkbox22 = customtkinter.CTkCheckBox(master=frame6, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox22.grid(row=5, column=0,padx=20, pady=10)

checkbox23 = customtkinter.CTkCheckBox(master=frame6, text="CTkCheckBox", command=checkbox_event, onvalue="on", offvalue="off")
checkbox23.grid(row=5, column=1,padx=20, pady=10)

frame7 = customtkinter.CTkFrame(master=root,corner_radius=10)
frame7.grid(row=3, column=2, padx=20, pady=20, sticky="sew")

home_button = customtkinter.CTkButton(master=frame7, width=320,height=50,border_width=0,corner_radius=8,text="Home",font=("Arial",17))
home_button.grid(row=1, column=0, padx=20, pady=10,columnspan=2)

sub_button = customtkinter.CTkButton(master=frame7,width=320,height=50,border_width=0, corner_radius=8,text="Submit",font=("Arial",17))
sub_button.grid(row=0, column=0, padx=20, pady=10,columnspan=2)


#label_name.grid(row=2, column=0, padx=1, pady=1)
#button.grid(row=12, column=0, columnspan=10, padx=20, pady=10)
#button1.grid(row=21, column=0, columnspan=10, padx=20, pady=10)
#label_name.configure(state="disabled")
#label_name1.configure(state="disabled")

#button.grid(row=0, column=0)


root.mainloop()