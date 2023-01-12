import subprocess
from tkinter import END
from sqlalchemy import create_engine

import registration_form



flag_validation = True
english = registration_form.slider_english.get("1.0", END)
sinhala = registration_form.slider_sinhala.get("1.0", END)
tamil = registration_form.slider_tamil.get("1.0", END)
university = registration_form.combobox_university.get()
degree = registration_form.combobox_degree.get()
gpa = registration_form.textbox_gpa.get("1.0", END)
projects = registration_form.textbox_project.get("1.0", END)

engine = create_engine("mysql+mysqldb://userid:password@localhost/user")

query = "INSERT INTO `education` (`english` ,`sinhala` ,`tamil` ,`university` , `degree` , `gpa` , `projects`) \
         VALUES(%s,%s,%s,%s,%s,%s,%s)"
my_data = (english, sinhala, tamil, university, degree, gpa, projects)
engine.execute(query, my_data)








