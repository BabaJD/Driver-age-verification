# create variables for the user to input
user_name = input("Enter your name here: ")
user_age = int(input("Enter your age here: "))
user_hair_colour = input("What is the colour of your hair? ")
user_eye_colour = input("What is the colour of your eye? ")

# Create an Adult class
class Adult():
    # Contructor method
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    # method that prints if the person is over 18
    def can_drive(self):
        print(f"{self.name} is old enough to drive")


# create a subclass of Adult called Child, that will print if the age of
# the user is less than 18
class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is not old enough to drive")


# contruct logic that will be used to choose which method to execute based on the age of the user

# use an if-else function to create an object that will utilize the appropriate method based on the age of the user
if user_age < 18:      
    person = Child(user_name, user_age, user_eye_colour, user_hair_colour)  
else:      
    person = Adult(user_name, user_age, user_eye_colour, user_hair_colour)


person.can_drive()
 

