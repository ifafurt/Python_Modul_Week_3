"""Question1: Create a Python class called "Rectangle" that represents a rectangle.
The Rectangle class must have the following properties and methods:
Features: width (an integer) height (an integer)
Methods: area(self): A method that calculates and returns the area of the rectangle.
perimeter(self): A method that calculates and returns the perimeter of the rectangle.
Create an instance of Rectangle class, set its width to 5 and height to 7, then print its area and perimeter."""

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# rect = Rectangle(5, 7)
# print("Area:", rect.area())
# print("Perimeter:", rect.perimeter())


"""Question2: Create a "School" class in Python. This class should have the following features and functionality:
Features:
"name"
"foundation_year"
"students"
"teachers"
Methods:
add_new_student(self, student_name, class): A method used to add a new student to the school. 
It takes the student's name and class and adds it to the "students" list.
add_new_teacher(self, teacher_name, branch): A method used to add a new teacher to the school. 
It takes the teacher's name and major and adds it to the "teachers" dictionary.
view_student_list(self): A method used to display the list of students enrolled in the school. 
List student names and classes.
view_teacher_list(self): A method used to display the list of teachers working in the school. 
List teacher names and majors."""

# class School:
#     def __init__(self, name, foundation_year):
#         self.name = name
#         self.foundation_year = foundation_year
#         self.students = []
#         self.teachers = []
#
#     def add_new_student(self, student_name, class_name):
#         self.students.append((student_name, class_name))
#
#     def add_new_teacher(self, teacher_name, branch):
#         self.teachers.append((teacher_name, branch))
#
#     def view_student_list(self):
#         print(self.students)
#
#     def view_teacher_list(self):
#         print(self.teachers)
#
#
#
# school = School("Sunrise School", 2005)
# school.add_new_student("Ali", "3A")
# school.add_new_student("Ayşe", "4B")
# school.add_new_teacher("Ahmet", "Math")
# school.add_new_teacher("Elif", "Science")
#
# school.view_student_list()
# school.view_teacher_list()







"""Question4: Create a "Vehicle" class in Python. Make sure this class has the following properties:

Features:
"make" (Brand of vehicle)
"model" (Vehicle model)
"year" (Year of manufacture of the vehicle)
Create a "Vehicle" class and create two derived subclasses, "Off-Road Vehicle" (SUV) and "SportsCar" classes.

The "Off-Road Vehicle" class inherits from the "Vehicle" class and adds an additional "four_wheel drive" feature.
Let the "SportCar" class inherit from the "Vehicle" class and add a "max_speed" property.
Create an instance of each class, determine its properties, and write a program to display these properties."""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} - 4x4: {self.four_wheel_drive}")


class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def display_info(self):
        print(f"{self.year} {self.make} {self.model} - Max speed: {self.max_speed} km/h")


suv = OffRoadVehicle("Toyota", "Land Cruiser", 2022, True)
sport = SportsCar("Ferrari", "F8", 2023, 340)

suv.display_info()
sport.display_info()
