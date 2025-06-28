class cat: 
    cat_color="white"
    age=1
    eye_color="black"

    def __init__(self,name,breed,age,eye_color):
        self.name=name
        self.breed=breed
        self.age=age
        self.eye_color=eye_color

    def sleep(self):
        return ("cat is sleeping")
    
    def meow(self):
        return f"hi i am {self.name} and I am meowing"
    
    def food(self):
        return f"hi I want food"
    
seek = cat("seek","american",1,"black")

print(seek.meow())
print(seek.sleep())



class bank:
#homework


class account: