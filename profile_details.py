import subprocess
from tkinter import END
from sqlalchemy import create_engine

import registration_form


flag_validation = True
name = registration_form.textbox_name.get("1.0", END)
uni_id = registration_form.textbox_uni_id.get("1.0", END)
gender = registration_form.textbox_gender.get("1.0", END)
email = registration_form.textbox_email.get("1.0", END)
phone = registration_form.textbox_tel.get("1.0", END)
linkedin = registration_form.textbox_linkedin.get("1.0", END)
github = registration_form.textbox_github.get("1.0", END)
other = registration_form.textbox_other_link.get("1.0", END)

engine = create_engine("mysql+mysqldb://userid:password@localhost/user")

query = "INSERT INTO `profile` (`name` ,`uni_id` ,`gender` ,`email` , `phone` , `linkedin` , `github` , `other`) \
         VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
my_data = (name, uni_id, gender, email, phone, linkedin, github, other)
engine.execute(query, my_data)








