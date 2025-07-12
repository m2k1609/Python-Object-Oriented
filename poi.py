# class cat: 
#     cat_color="white"
#     age=1
#     eye_color="black"

#     def __init__(self,name,breed,age,eye_color):
#         self.name=name
#         self.breed=breed
#         self.age=age
#         self.eye_color=eye_color

#     def sleep(self):
#         return ("cat is sleeping")
    
#     def meow(self):
#         return f"hi i am {self.name} and I am meowing"
    
#     def food(self):
#         return f"hi I want food"
    
# seek = cat("seek","american",1,"black")

# print(seek.meow())
# print(seek.sleep())



# class DaBank:
#     bank_name="how to get rich 101"
#     location = "here"
#     money = 250000


#     def __init__(self,name,location,money):
#         self.name=name
#         self.location=location
#         self.money=money

#     def getmoney(self):
#         return f"How much money would you like to withdraw from your account?"
    
#     def inputmoney(self):
#         x = input("how much input")
#         return f"we have withdrawed ${x} from your account"
    
# iamrobbingdabank = DaBank("Robin","here",250000)
# print(iamrobbingdabank.inputmoney())

# print(iamrobbingdabank.location)
# print(iamrobbingdabank.name)
   



# class account:
#     bank_name = "bank of america"
    
    
#     def __init__(self,name,number,type,balance):
#         self.name=name
#         self.number=number
#         self.type=type
#         self.balance=balance

#     def typeofaccounts(self):
#         y = input("what type of account do you have")
#         return f"You have a {y} account"
    
#     def numbers(self):
#         z = int(input("what is your account number?"))
#         return f"We are now accessing {z} account"
    
#     def withdraw(self):
#         a = int(input("How much would you like to withdraw")) 
#         if a>self.balance:
#             print("Your broke bruh")
#         else:
#             return f"we are withdrawing ${a} from your account"

#     def deposit(self):
#         b = int(input("How much would you like to deposit"))
#         return f"we have deposited ${b} into your account"
    
# moneythingy = account("bank of america",123,"checking",100)

# print(moneythingy.bank_name)
# print(moneythingy.withdraw())
# print(moneythingy.deposit())
# print(moneythingy.numbers())
# print(moneythingy.typeofaccounts())







# class School:
#     school_name = "howtoberich"
    
#     def __init__(self, name, number, type, students):
#         self.name = name
#         self.number = number
#         self.type = type
#         self.students = students

#     def get_students(self):
      
#         return f"This school has {self.students} number of students"
    
#     def get_school_type(self):
        
#         return f"This is a {self.type} school"
    
#     def get_school_number(self):
#         a = int(input("What is the school number? "))
#         return f"We are now accessing school number {a}"
    
#     def add_student(self):
#         b = int(input("How many students would you like to add? "))
#         self.students=b + self.students
#         if b <= 0:
#             print("You can't add zero or negative students!")
#         else:
#             return f"We are adding {b} students to the school"
    
#     def remove_student(self):
#         c = int(input("How many students are leaving? "))
#         self.students=self.students - c
#         if c > self.students:
#             print("You can't remove more students than you have!")
#         else:
#             return f"We are removing {c} students from the school"

# # Create a school instance
# my_school = School("howtoberich", 123, "high school", 5000)

# print(my_school.school_name)
# print(my_school.get_students())
# print(my_school.add_student())
# print(my_school.get_students())
# print(my_school.remove_student())
# print(my_school.get_students())

# print(my_school.get_school_type())
# print(my_school.get_school_number())



class Student:
    school_name = "Purdue University"
    
    def __init__(self, name, student_id, major, grade):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.grade = grade
    
    def get_major(self):
        
        return f"You are studying {self.major}"
    
    def get_student_id(self):
      
        return f"We are now accessing student ID {self.student_id}"
    
    def add_grade(self):
        grade = int(input("What grade did you receive? "))
        self.grade = self.grade + grade
        if self.grade < 0 or self.grade > 100:
            print("Invalid grade! Grade must be between 0 and 100")
        else:
            return f"Adding grade {grade} to your record"
    
    def check_grade(self):
        
        if self.grade < 60:
            print("You're failing, study harder!")
        else:
            return f"Your current grade is {self.grade}"
    
    def enroll_course(self):
        course = input("What course would you like to enroll in? ")
        return f"You have enrolled in {course}"


student1 = Student("Mohammad Khan", 12345, "Computer Science", 0)

print(student1.school_name)
print(student1.get_major())
print(student1.get_student_id())
print(student1.add_grade())
print(student1.check_grade())
print(student1.enroll_course())







# class gpa please help