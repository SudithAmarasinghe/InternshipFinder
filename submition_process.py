import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="internshipfinder")
cursor = con.cursor()

def insert_values(stu,opt_list):
    str_profile = "INSERT INTO profile VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    user_profile = (stu.id, stu.name, stu.uni_id, stu.gender, stu.email, stu.tel, stu.linkedin, stu.github, stu.other)
    cursor.execute(str_profile, user_profile)

    str_technical_skills = "INSERT INTO technical_skills VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    user_technical_skills = (stu.id, opt_list[0], opt_list[1], opt_list[2], opt_list[3], opt_list[4], opt_list[5], opt_list[6], opt_list[7], opt_list[8],
             opt_list[9], opt_list[10], opt_list[11], stu.other_skill, stu.activities)
    cursor.execute(str_technical_skills, user_technical_skills)

    str_soft_skills = "INSERT INTO soft_skills VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    user_soft_skills = (stu.id, opt_list[12], opt_list[13], opt_list[14], opt_list[15], opt_list[16], opt_list[17], opt_list[18], opt_list[19],
    opt_list[20], opt_list[21])
    cursor.execute(str_soft_skills, user_soft_skills)

    str_lang = "INSERT INTO languages VALUES (%s, %s, %s, %s)"
    user_lang = (stu.id, stu.english, stu.sinhala, stu.tamil)
    cursor.execute(str_lang, user_lang)

    str_interest = "INSERT INTO interests VALUES (%s, %s, %s, %s, %s)"
    user_interest = (stu.id, opt_list[22], opt_list[23], opt_list[24], opt_list[25])
    cursor.execute(str_interest, user_interest)

    str_edu = "INSERT INTO education VALUES (%s, %s, %s, %s, %s)"
    user_edu = (stu.id, stu.university, stu.degree, stu.gpa, stu.project)
    cursor.execute(str_edu, user_edu)

    con.commit()
