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



class DaBank:
    bank_name="how to get rich 101"
    location = "here"
    money = 250000


    def __init__(self,name,location,money):
        self.name=name
        self.location=location
        self.money=money

    def getmoney(self):
        return f"How much money would you like to withdraw from your account?"
    
    def inputmoney(self):
        x = input("how much input")
        return f"we have withdrawed ${x} from your account"
    
iamrobbingdabank = DaBank("Robin","here",250000)
print(iamrobbingdabank.inputmoney())

print(iamrobbingdabank.location)
print(iamrobbingdabank.name)
   



# class account: