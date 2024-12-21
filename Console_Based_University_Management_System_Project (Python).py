from Password_Checker_Module import obj
from Secure_OTP_Authentication_System_with_SMTP_Module import mail_verify
class person:
    def __init__(self,name,roll,mobile,mail):
        self.name = name
        self.roll = roll
        self.mobile = mobile
        self.mail = mail
class student(person):
    def __init__(self,name,roll,mobile,mail,branch):
        self.branch = branch
        super().__init__(name,roll,mobile,mail)
class teacher(person):
    def __init__(self,name,roll,mobile,mail,subject):
        self.subject = subject
        super().__init__(name,roll,mobile,mail)
class college:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def display_students(self):
        print()
        for i in range(len(self.students)):
            print(f"Student {i+1} Details")
            print(f"Name: {self.students[i].name}")
            print(f"Roll Number: {self.students[i].roll}")
            print(f"Mobile Number: {self.students[i].mobile}")
            print(f"Mail-ID: {self.students[i].mail}")
            print(f"Branch: {self.students[i].branch}")
            print()
    def display_teachers(self):
        print()
        for i in range(len(self.teachers)):
            print(f"Teacher {i+1} Details")
            print(f"Name: {self.teachers[i].name}")
            print(f"Roll Number: {self.teachers[i].roll}")
            print(f"Mobile Number: {self.teachers[i].mobile}")
            print(f"Mail-ID: {self.teachers[i].mail}")
            print(f"Subject: {self.teachers[i].subject}")
            print()
    def students_data_to_file(self,cname):
        f = open('Students_Data.txt', 'a')
        f.write(f"College Name: {cname}\n")
        for i in range(len(self.students)):
            f.write(f"\nStudent {i+1} Details\n")
            f.write(f"Name: {self.students[i].name}\n")
            f.write(f"Roll: {self.students[i].roll}\n")
            f.write(f"Mobile: {self.students[i].mobile}\n")
            f.write(f"Mail-ID: {self.students[i].mail}\n")
            f.write(f"Branch: {self.students[i].branch}\n")
            f.write('\n')
        f.close()
    def teachers_data_to_file(self,cname):
        f = open('Teachers_Data.txt', 'a')
        f.write(f"College Name: {cname}\n")
        for i in range(len(self.teachers)):
            f.write(f"\nTeacher {i+1} Details\n")
            f.write(f"Name: {self.teachers[i].name}\n")
            f.write(f"Id: {self.teachers[i].roll}\n")
            f.write(f"Mobile: {self.teachers[i].mobile}\n")
            f.write(f"Mail-ID: {self.teachers[i].mail}\n")
            f.write(f"Subject: {self.teachers[i].subject}\n")
            f.write('\n')
        f.close()
    def display_colleges(self, colleges):
        f = open('College_Data.txt', 'a')
        f.write('College Names: \n')
        f.write('\n')
        for i in colleges:
            f.write(f'{i.name}\n')
        f.close()
    def display_all_students(self,students):
        f = open('All_Students_Names.txt', 'a')
        f.write('All College Students Names: \n')
        f.write('\n')
        for i in colleges:
            for j in i.students:
                f.write(f'{j.name}\n')
        f.close()
    def display_all_teachers(self,students):
        f = open('All_Teachers_Names.txt', 'a')
        f.write('All College Teachers Names: \n')
        f.write('\n')
        for i in colleges:
            for j in i.teachers:
                f.write(f'{j.name}\n')
        f.close()
colleges = []

while True:
    print("Choose your Option")
    print("1. New User?")
    print("2. Login")
    print("3. Exit")
    user = int(input("Enter your Option: "))
    if user == 1:
        obj.password()
    elif user == 2:
        u_password = input("Enter Password: ")
        check = obj.verify_password2(u_password)
        if check:
            while True:
                print("Choose your Option")
                print("1. Create College")
                print("2. Add student")
                print("3. Add Teacher")
                print("4. Display Students Details")
                print("5. Display Teachers Details")
                print("6. Display Students Details in a File")
                print("7. Display Teachers Details in a File")
                print("8. Dislay All College Names")
                print("9. Display All Students Names")
                print("10. Display All Teachers Names")
                print("11. Exit")
                x = int(input("Enter your Option: "))
                if x == 1:
                    cname = input("Enter College Name: ")
                    x = True
                    for i in colleges:
                        if i.name == cname:
                            x = False
                            break
                    if x == True:
                        c = college(cname)
                        colleges.append(c)
                        print("College Created Sucessfully")
                    else:
                        print("College Already Exists")
                elif x == 2:
                    cname = input("Enter College Name: ")
                    x = False
                    for i in colleges:
                        if i.name == cname:
                            x = True
                    if x == True:
                        ind = -1
                        for i in range(len(colleges)):
                            if colleges[i].name == cname:
                                ind = i
                        sname = input("Enter Student name: ")
                        sroll = input("Enter Roll number: ")
                        smobile = input("Enter Mobile Number: ")
                        smail = input("Enter Mail-ID: ")
                        boolean = mail_verify(smail)
                        if boolean:
                            sbranch = input("Enter Student Branch: ")
                            s1 = student(sname,sroll,smobile,smail,sbranch)
                            colleges[ind].add_student(s1)
                            print(f"Student Added to {cname} College")
                        else:
                            print("OTP Verfication Failed! Try Again")
                    else:
                        print("College Does Not Exists")
                elif x == 3:
                    cname = input("Enter College Name: ")
                    x = False
                    for i in colleges:
                        if i.name == cname:
                            x = True
                    if x == True:
                        ind = -1
                        for i in range(len(colleges)):
                            if colleges[i].name == cname:
                                ind = i
                        tname = input("Enter Teacher name: ")
                        troll = input("Enter ID: ")
                        tmobile = input("Enter Mobile Number: ")
                        tmail = input("Enter Mail-ID: ")
                        boolean = mail_verify(tmail)
                        if boolean:
                            tsubject = input("Enter Subject: ")
                            t1 = teacher(tname,troll,tmobile,tmail,tsubject)
                            colleges[ind].add_teacher(t1)
                            print(f"Teacher Added to {cname} College")
                        else:
                            print("OTP Verfication Failed! Try Again")
                    else:
                        print("College Does Not Exists")
                elif x == 4:
                    cname = input("Enter College Name: ")
                    x = False
                    for i in colleges:
                        if i.name == cname:
                            x = True
                    if x == True:
                        ind = -1
                        for i in range(len(colleges)):
                            if colleges[i].name == cname:
                                ind = i
                        colleges[ind].display_students()
                    else:
                        print("College Not Exists")
                elif x == 5:
                    cname = input("Enter College Name: ")
                    x = False
                    for i in colleges:
                        if i.name == cname:
                            x = True
                    if x == True:
                        ind = -1
                        for i in range(len(colleges)):
                            if colleges[i].name == cname:
                                ind = i
                        colleges[ind].display_teachers()
                    else:
                        print("College Not Exists")
                elif x == 6:
                    cname = input("Enter College Name: ")
                    x = False
                    for i in colleges:
                        if i.name == cname:
                            x = True
                    if x == True:
                        ind = -1
                        for i in range(len(colleges)):
                            if colleges[i].name == cname:
                                ind = i
                        colleges[ind].students_data_to_file(cname)
                    else:
                        print("College Not Exists")
                elif x == 7:
                    cname = input("Enter College Name: ")
                    x = False
                    for i in colleges:
                        if i.name == cname:
                            x = True
                    if x == True:
                        ind = -1
                        for i in range(len(colleges)):
                            if colleges[i].name == cname:
                                ind = i
                        colleges[ind].teachers_data_to_file(cname)
                    else:
                        print("College Not Exists")
                elif x == 8:
                    c.display_colleges(colleges)
                elif x == 9:
                    c.display_all_students(student)
                elif x == 10:
                    c.display_all_teachers(teacher)
                else:
                    print('Thanks For Using University Management System')
                    break
        else:
            print('Wrong Password! Please Try Again')
    else:
        print('Thank You.')
        break
    

            




