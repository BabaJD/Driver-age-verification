
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    office_address = "Cape Town"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

#  Add another method in the Course class that prints the head office location: Cape Town
    def head_office_location(self):
        print(f"The head office location of HyperionDev is: {self.office_address}")

# Create a subclass of the Course class named OOPCourse
class OOPCourse(Course):
    course_id = "#12345"

# Create a constructor that initialises the description and trainer attributes 
# and assign their values
    def __init__(self, description = "OOP Fundamentals", trainer = "Mr Anon A. Mouse"):
        self.description = description
        self.trainer = trainer

# Create a method in the subclass named "trainer_details" that prints what the 
#  course is about and the name of the trainer    
    def trainer_details(self):
        print(f"The name of this course is {self.description} and the name of the trainer is {self.trainer}")

# Create a method in the subclass named "show_course_id" that prints the ID number of the course
    def show_course_id(self):
        print(f"The course id is {self.course_id}")

#Create an object of the subclass called course_1 and call the methods created
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
