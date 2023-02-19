import tkinter
import customtkinter
import submition_process as sp
import mysql.connector
import re
import student
con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="internshipfinder")
cursor = con.cursor()

#--------------------------------------------------------------------------------------------------------

def signout():
    print("Signout")

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
label_username.grid(row=0, column=2, padx=(310,50), pady=8, sticky="e")

logout_button = customtkinter.CTkButton(master=frame0,width=70,height=30,border_width=0, corner_radius=8,text="Sign Out"
                                        ,command=signout,font=("Arial",17))
logout_button.grid(row=0, column=3, padx=(0,0), pady=5, sticky="e")

#---------------------------------------------------------------------------------------------------------------------------
frame1 = customtkinter.CTkFrame(master=root,corner_radius=10)
frame1.grid(row=1, column=0,padx=20, pady=(10,15))

label_profile = customtkinter.CTkLabel(master=frame1,text="PROFILE DETAILS",fg_color=("#68aced","#1f538d"),width=400,height=30,corner_radius=8,font=("Arial",20))
label_profile.grid(row=0, column=0, columnspan=2, padx=10, pady=(20,5))

label_name = customtkinter.CTkLabel(master=frame1,text="Name",anchor="w",width=120,font=("Arial",17))
label_name.grid(row=1, column=0, padx=20, pady=8)
textbox_name = customtkinter.CTkTextbox(master=frame1,width=250,height=5,font=("Arial",17))
textbox_name.grid(row=1, column=1, padx=(10,20), pady=5)

label_uni_id = customtkinter.CTkLabel(master=frame1,text="University ID",anchor="w",width=120,font=("Arial",17))
label_uni_id.grid(row=2, column=0, padx=20, pady=8)
textbox_uni_id = customtkinter.CTkTextbox(master=frame1,width=250,height=5,font=("Arial",17))
textbox_uni_id.grid(row=2, column=1, padx=(10,20), pady=5)

gender_opt = tkinter.StringVar()
label_gender = customtkinter.CTkLabel(master=frame1,text="Gender",anchor="w",width=120,font=("Arial",17))
label_gender.grid(row=3, column=0, padx=20, pady=8)
gender_list=["Male", "Female"]
combobox_gender = customtkinter.CTkOptionMenu(master=frame1,values=gender_list,width=250,height=35,font=("Arial",17),
                                              variable=gender_opt)
combobox_gender.grid(row=3, column=1, padx=(10,20), pady=5, ipady=1)
combobox_gender.set("     --Select the Gender--")

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

label_link = customtkinter.CTkLabel(master=frame2,text="PROFILE DETAILS",fg_color=("#68aced","#1f538d"),width=400,height=30,corner_radius=8,font=("Arial",20))
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

label_language = customtkinter.CTkLabel(master=frame3,text="LANGUAGES",fg_color=("#68aced","#1f538d"),width=400,height=30,corner_radius=8,font=("Arial",20))
label_language.grid(row=0, column=0, columnspan=2, padx=10, pady=(20,5))

eng_lan = tkinter.IntVar()
label_english = customtkinter.CTkLabel(master=frame3,text="English",anchor="w",width=120,font=("Arial",17))
label_english.grid(row=1, column=0, padx=20, pady=8)
slider_english = customtkinter.CTkSlider(master=frame3,width=250,number_of_steps=5, from_=0, to=100,variable=eng_lan)
slider_english.grid(row=1, column=1, padx=(10,20), pady=5)

sin_lan = tkinter.IntVar()
label_sinhala = customtkinter.CTkLabel(master=frame3,text="Sinhala",anchor="w",width=120,font=("Arial",17))
label_sinhala.grid(row=2, column=0, padx=20, pady=8)
slider_sinhala = customtkinter.CTkSlider(master=frame3,width=250, number_of_steps=5, from_=0, to=100, variable=sin_lan)
slider_sinhala.grid(row=2, column=1, padx=(10,20), pady=5)

tam_lan = tkinter.IntVar()
label_tamil = customtkinter.CTkLabel(master=frame3,text="Tamil",anchor="w",width=120,font=("Arial",17))
label_tamil.grid(row=3, column=0, padx=20, pady=8)
slider_tamil = customtkinter.CTkSlider(master=frame3,width=250, number_of_steps=5, from_=0, to=100, variable=tam_lan)
slider_tamil.grid(row=3, column=1, padx=(10,20), pady=5)


#-------------------------------------------------------------------------------------------------------------------------------------

frame4 = customtkinter.CTkFrame(master=root,corner_radius=10)
frame4.grid(row=1, column=1, pady=(10,20), sticky="new")

label_education = customtkinter.CTkLabel(master=frame4,text="EDUCATION DETAILS",fg_color=("#68aced","#1f538d"),width=600,height=30,corner_radius=8,font=("Arial",20))
label_education.grid(row=0, column=0, columnspan=2, padx=10, pady=(20,5))

uni_opt = tkinter.StringVar()
label_university = customtkinter.CTkLabel(master=frame4,text="University",anchor="w",width=120,font=("Arial",17))
label_university.grid(row=1, column=0, padx=20, pady=8)
university_list=["University of Colombo", "University of Peradeniya","University of Sri Jayewardenepura", "University of Kelaniya",
                 "University of Moratuwa","University of Jaffna","University of Ruhuna","The Open University of Sri Lanka",
                 "Eastern University, Sri Lanka","South Eastern University of Sri Lanka","Rajarata University of Sri Lanka",
                 "Sabaragamuwa University of Sri Lanka","Wayamba University of Sri Lanka","Uva Wellassa University of Sri Lanka",
                 "University of the Visual & Performing Arts","Gampaha Wickramarachchi University of Indigenous Medicine",
                 "University of Vavuniya"]
combobox_university = customtkinter.CTkOptionMenu(master=frame4,values=university_list,width=450,height=35,font=("Arial",17), variable=uni_opt)
combobox_university.grid(row=1, column=1, padx=(10,20), pady=5, ipady=1)
university_place_holder = "     --Select the University--"
combobox_university.set(university_place_holder)

degree_opt = tkinter.StringVar()
label_degree = customtkinter.CTkLabel(master=frame4,text="Degree",anchor="w",width=120,font=("Arial",17))
label_degree.grid(row=2, column=0, padx=20, pady=8)
degree_list=["Bachelor of Science Honours in Computer Science", "Bachelor of Science (Surveying Science)",
             "Bachelor of Arts General Degree (BA)"]
combobox_degree = customtkinter.CTkOptionMenu(master=frame4,values=degree_list,width=450,height=35,font=("Arial",17),
                                              variable=degree_opt)
combobox_degree.grid(row=2, column=1, padx=(10,20), pady=5, ipady=1)
degree_place_holder = "     --Select the Degree--"
combobox_degree.set(degree_place_holder)

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

label_skill = customtkinter.CTkLabel(master=frame5,text="TECHNICAL SKILLS",fg_color=("#68aced","#1f538d"),width=600,height=30,corner_radius=8,font=("Arial",20))
label_skill.grid(row=0, column=0, columnspan=3, padx=20, pady=(20,5))

apache_val = tkinter.IntVar()
xml_val = tkinter.IntVar()
angular_val = tkinter.IntVar()
javascript_val = tkinter.IntVar()
sql_val = tkinter.IntVar()
tomcat_val = tkinter.IntVar()
aws_val = tkinter.IntVar()
python_val = tkinter.IntVar()
r_val = tkinter.IntVar()
c_val = tkinter.IntVar()
c_sharp_val = tkinter.IntVar()
git_val = tkinter.IntVar()

apache = customtkinter.CTkCheckBox(master=frame5, text="Apache", variable=apache_val, onvalue=1, offvalue=0,font=("Arial",15))
apache.grid(row=1, column=0,padx=20, pady=10)

xml = customtkinter.CTkCheckBox(master=frame5, text="XML", variable=xml_val, onvalue=1, offvalue=0,font=("Arial",15))
xml.grid(row=1, column=1,padx=20, pady=10)

angular = customtkinter.CTkCheckBox(master=frame5, text="Angular", variable=angular_val, onvalue=1, offvalue=0,font=("Arial",15))
angular.grid(row=1, column=2,padx=20, pady=10)

javascript = customtkinter.CTkCheckBox(master=frame5, text="JavaScript", variable=javascript_val, onvalue=1, offvalue=0,font=("Arial",15))
javascript.grid(row=2, column=0,padx=20, pady=10)

sql = customtkinter.CTkCheckBox(master=frame5, text="SQL", variable=sql_val, onvalue=1, offvalue=0,font=("Arial",15))
sql.grid(row=2, column=1,padx=20, pady=10)

tomcat = customtkinter.CTkCheckBox(master=frame5, text="Tomcat", variable=tomcat_val, onvalue=1, offvalue=0,font=("Arial",15))
tomcat.grid(row=2, column=2,padx=20, pady=10)

aws = customtkinter.CTkCheckBox(master=frame5, text="AWS", variable=aws_val, onvalue=1, offvalue=0,font=("Arial",15))
aws.grid(row=3, column=0,padx=20, pady=10)

python = customtkinter.CTkCheckBox(master=frame5, text="Python", variable=python_val, onvalue=1, offvalue=0,font=("Arial",15))
python.grid(row=3, column=1,padx=20, pady=10)

r = customtkinter.CTkCheckBox(master=frame5, text="R", variable=r_val, onvalue=1, offvalue=0,font=("Arial",15))
r.grid(row=3, column=2,padx=20, pady=10)

c = customtkinter.CTkCheckBox(master=frame5, text="C", variable=c_val, onvalue=1, offvalue=0,font=("Arial",15))
c.grid(row=4, column=0,padx=20, pady=(10,13))

c_sharp = customtkinter.CTkCheckBox(master=frame5, text="C#", variable=c_sharp_val, onvalue=1, offvalue=0,font=("Arial",15))
c_sharp.grid(row=4, column=1,padx=20, pady=(10,13))

git = customtkinter.CTkCheckBox(master=frame5, text="Git", variable=git_val, onvalue=1, offvalue=0,font=("Arial",15))
git.grid(row=4, column=2,padx=20, pady=(10,13))

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

label_s_skill = customtkinter.CTkLabel(master=frame6,text="SOFT SKILLS",fg_color=("#68aced","#1f538d"),width=320,height=30,corner_radius=8,font=("Arial",20))
label_s_skill.grid(row=0, column=0, columnspan=2, padx=20, pady=(20,5))

attention_val = tkinter.IntVar()
creativity_val = tkinter.IntVar()
adaptability_val = tkinter.IntVar()
management_val = tkinter.IntVar()
analysis_val = tkinter.IntVar()
organization_val = tkinter.IntVar()
training_val = tkinter.IntVar()
communication_val = tkinter.IntVar()
teamwork_val = tkinter.IntVar()
leadership_val = tkinter.IntVar()

attention = customtkinter.CTkCheckBox(master=frame6, text="Attention",variable=attention_val, onvalue=1, offvalue=0,font=("Arial",15))
attention.grid(row=1, column=0,padx=(40,10), pady=10,sticky="w")

creativity = customtkinter.CTkCheckBox(master=frame6, text="Creativity", variable=creativity_val, onvalue=1, offvalue=0,font=("Arial",15))
creativity.grid(row=1, column=1,padx=30, pady=10,sticky="w")

adaptability = customtkinter.CTkCheckBox(master=frame6, text="Adaptability", variable=adaptability_val, onvalue=1, offvalue=0,font=("Arial",15))
adaptability.grid(row=2, column=0,padx=(40,10), pady=10,sticky="w")

management = customtkinter.CTkCheckBox(master=frame6, text="Management", variable=management_val, onvalue=1, offvalue=0,font=("Arial",15))
management.grid(row=2, column=1,padx=30, pady=10,sticky="w")

analysis = customtkinter.CTkCheckBox(master=frame6, text="Analysis", variable=analysis_val, onvalue=1, offvalue=0,font=("Arial",15))
analysis.grid(row=3, column=0,padx=(40,10), pady=10,sticky="w")

organization = customtkinter.CTkCheckBox(master=frame6, text="Organization", variable=organization_val, onvalue=1, offvalue=0,font=("Arial",15))
organization.grid(row=3, column=1,padx=30, pady=10,sticky="w")

training = customtkinter.CTkCheckBox(master=frame6, text="Training ", variable=training_val, onvalue=1, offvalue=0,font=("Arial",15))
training.grid(row=4, column=0,padx=(40,10), pady=10,sticky="w")

communication = customtkinter.CTkCheckBox(master=frame6, text="Communication", variable=communication_val, onvalue=1, offvalue=0,font=("Arial",15))
communication.grid(row=4, column=1,padx=30, pady=10,sticky="w")

teamwork = customtkinter.CTkCheckBox(master=frame6, text="Teamwork ", variable=teamwork_val, onvalue=1, offvalue=0,font=("Arial",15))
teamwork.grid(row=5, column=0,padx=(40,10), pady=10,sticky="w")

leadership = customtkinter.CTkCheckBox(master=frame6, text="Leadership", variable=leadership_val, onvalue=1, offvalue=0,font=("Arial",15))
leadership.grid(row=5, column=1,padx=30, pady=10,sticky="w")

#----------------------------------------------------------------------------------------------------------------------------

frame7 = customtkinter.CTkFrame(master=root,corner_radius=10)
frame7.grid(row=2, column=2, padx=20, pady=(0,10), rowspan=2, sticky="new")

label_interests = customtkinter.CTkLabel(master=frame7,text="INTERESTS",fg_color=("#68aced","#1f538d"),width=320,height=30,corner_radius=8,font=("Arial",20))
label_interests.grid(row=0, column=0, columnspan=2, padx=20, pady=(20,5))

soft_dev_val = tkinter.IntVar()
ai_eng_val = tkinter.IntVar()
data_sci_val = tkinter.IntVar()
net_admin_val = tkinter.IntVar()

soft_dev = customtkinter.CTkCheckBox(master=frame7, text="Software Developer.", variable=soft_dev_val, onvalue=1, offvalue=0,font=("Arial",15))
soft_dev.grid(row=1, column=0,padx=40, pady=10,sticky="w")

ai_eng = customtkinter.CTkCheckBox(master=frame7, text="AI Engineer.", variable=ai_eng_val,  onvalue=1, offvalue=0,font=("Arial",15))
ai_eng.grid(row=2, column=0,padx=40, pady=10,sticky="w")

data_sci = customtkinter.CTkCheckBox(master=frame7, text="Data Scientist.", variable=data_sci_val,  onvalue=1, offvalue=0,font=("Arial",15))
data_sci.grid(row=3, column=0,padx=40, pady=10,sticky="w")

net_admin = customtkinter.CTkCheckBox(master=frame7, text="Network Administrator. ", variable=net_admin_val, onvalue=1, offvalue=0,font=("Arial",15))
net_admin.grid(row=4, column=0,padx=40, pady=(10,20),sticky="w")

#-------------------------------------------------------------------------------------------------------------------------

frame8 = customtkinter.CTkFrame(master=root,corner_radius=10)
frame8.grid(row=3, column=2, padx=20, pady=20, sticky="sew")

#----------------------------------------------------------------
def assign_username(username):
    label_username.configure(text=username)

def reset_fg_color():
    textbox_name.configure(fg_color=("#ffffff", "#333333"))
    textbox_gpa.configure(fg_color=("#ffffff", "#333333"))
    textbox_tel.configure(fg_color=("#ffffff", "#333333"))
    textbox_email.configure(fg_color=("#ffffff", "#333333"))
    textbox_uni_id.configure(fg_color=("#ffffff", "#333333"))
    combobox_degree.configure(fg_color=("#3a7ebf", "#1f538d"))
    combobox_university.configure(fg_color=("#3a7ebf", "#1f538d"))
    combobox_gender.configure(fg_color=("#3a7ebf", "#1f538d"))

def validate_attributes():
    state = True
    reset_fg_color()

    name = textbox_name.get("1.0", "end")
    if len(name) == 1:
        print("Name is required!")
        textbox_name.configure(fg_color=("#f5a2a9", "#6e2d19"))
        state = False
    else:
        name_pattern = "^[a-zA-Z._ ]+$"
        name_match = re.match(name_pattern, name)
        if name_match == None:
            print("Invalide name pattern!")
            textbox_name.configure(fg_color=("#f5a2a9", "#6e2d19"))
            state = False

    if len(textbox_uni_id.get("1.0", "end")) == 1:
        print("University ID is required!")
        textbox_uni_id.configure(fg_color=("#f5a2a9", "#6e2d19"))
        state = False

    if gender_opt.get() != "Male" and gender_opt.get() != "Male":
        print("Select the gender!")
        combobox_gender.configure(fg_color=("#6e4346", "#6e2d19"))
        state = False

    email = textbox_email.get("1.0", "end")
    if len(email) == 1:
        print("Email is required!")
        textbox_email.configure(fg_color=("#f5a2a9", "#6e2d19"))
        state = False
    else:
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        email_match = re.match(email_pattern, email)
        if email_match == None:
            print("Invalide Email!")
            textbox_email.configure(fg_color=("#f5a2a9", "#6e2d19"))
            state = False

    tele = textbox_tel.get("1.0", "end")
    tele_pattern = r"^0[0-9]{2,2} [0-9]{7,7}$"
    if len(tele) == 1:
        print("Telephone number is required!")
        textbox_tel.configure(fg_color=("#f5a2a9", "#6e2d19"))
        state = False
    else:
        tele_match = re.match(tele_pattern, tele)
        if tele_match == None:
            print("Invalide Tel.No!")
            textbox_tel.configure(fg_color=("#f5a2a9", "#6e2d19"))
            state = False

    if uni_opt.get() == university_place_holder:
        combobox_university.configure(fg_color=("#6e4346", "#6e2d19"))
        state = False
        print("Select the University!")

    if degree_opt.get() == degree_place_holder:
        combobox_degree.configure(fg_color=("#6e4346", "#6e2d19"))
        state = False
        print("Select the Degree!")

    gpa = textbox_gpa.get("1.0", "end")
    if len(gpa) == 1:
        print("GPA value is required!")
        textbox_gpa.configure(fg_color=("#f5a2a9", "#6e2d19"))
        state = False
    else:
        gpa_pattern = "^[+-]?\d+(\.\d+)?$"
        gpa_match = re.match(gpa_pattern, gpa)
        if gpa_match == None:
            print("Invalide GPA value!")
            textbox_gpa.configure(fg_color=("#f5a2a9", "#6e2d19"))
            state = False
    return state


def submit_details():
    if(validate_attributes()):
        stu = student.Student()
        stu.id = "AS3000"
        stu.name = textbox_name.get("0.0", "end")
        stu.uni_id = textbox_uni_id.get("0.0", "end")
        stu.gender = gender_opt.get()
        stu.email = textbox_email.get("0.0", "end")
        stu.tel = textbox_tel.get("0.0", "end")
        stu.linkedin = textbox_linkedin.get("0.0", "end")
        stu.github = textbox_github.get("0.0", "end")
        stu.other = textbox_other_link.get("0.0", "end")

        stu.english = eng_lan.get()
        stu.sinhala = sin_lan.get()
        stu.tamil = tam_lan.get()

        stu.university = uni_opt.get()
        stu.degree = degree_opt.get()
        stu.gpa = int(textbox_gpa.get("0.0", "end"))
        stu.project = textbox_project.get("0.0", "end")

        stu.other_skill = textbox_other_skill.get("0.0", "end")
        stu.activities = textbox_activity.get("0.0", "end")

        choice_list = []
        choice_list.append(int(apache_val.get()))
        choice_list.append(int(xml_val.get()))
        choice_list.append(int(angular_val.get()))
        choice_list.append(int(javascript_val.get()))
        choice_list.append(int(sql_val.get()))
        choice_list.append(int(tomcat_val.get()))
        choice_list.append(int(aws_val.get()))
        choice_list.append(int(python_val.get()))
        choice_list.append(int(r_val.get()))
        choice_list.append(int(c_val.get()))
        choice_list.append(int(c_sharp_val.get()))
        choice_list.append(int(git_val.get()))
        choice_list.append(int(attention_val.get()))
        choice_list.append(int(creativity_val.get()))
        choice_list.append(int(adaptability_val.get()))
        choice_list.append(int(management_val.get()))
        choice_list.append(int(analysis_val.get()))
        choice_list.append(int(organization_val.get()))
        choice_list.append(int(training_val.get()))
        choice_list.append(int(communication_val.get()))
        choice_list.append(int(teamwork_val.get()))
        choice_list.append(int(leadership_val.get()))
        choice_list.append(int(soft_dev_val.get()))
        choice_list.append(int(ai_eng_val.get()))
        choice_list.append(int(data_sci_val.get()))
        choice_list.append(int(net_admin_val.get()))

        sp.insert_values(stu,choice_list)
    else:
        print("Error")

#------------------------------------------------------------------------------------------------------------------------

sub_button = customtkinter.CTkButton(master=frame8,width=320,height=50,border_width=0, corner_radius=8,text="SUBMIT",
                                     font=("Arial",17),command=submit_details)
sub_button.grid(row=0, column=0, padx=20, pady=10,columnspan=2)
home_button = customtkinter.CTkButton(master=frame8, width=320,height=50,border_width=0,corner_radius=8,text="HOME",font=("Arial",17))
home_button.grid(row=1, column=0, padx=20, pady=10,columnspan=2)

root.mainloop()
