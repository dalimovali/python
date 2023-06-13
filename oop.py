# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def info(self):
#         print(f"My name is {self.name}, I am {self.age} yesars old")

# person = Person("gansterskiye", 20)
# person.info()
# person2 = Person("ali", 19)
# person2.info()



# import math

# class Mathh:
#     def __init__(self, a):
#         self.a = a

#     def perimetr(self):
#         return self.a * 4
    
#     def squear(self):
#         return self.a ** 2 
#     def dioganal(self):
#         res = (self.a ** 2 + self.a ** 2)
#         res2 = math.sqrt(res)
#         return res2
    
# mathh = Mathh(5)

# print(mathh.dioganal())
# print(mathh.perimetr())
# print(mathh.squear())


# class Regtangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def get_area(self):
#         area = self.width * self.height
#         return f"Площадь прямоугольника {area}"

# regtangle = Regtangle(3, 4)
# print(regtangle.get_area())



# class Car():
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def get_info(self):
#         return f"Марках автомобиля:{self.brand},модель:{self.model} "
# car = Car("TOYOTA", "SUPRA")
# print(car.get_info())
# car2 = Car("AUDI", "S8")
# print(car2.get_info())



# class Circle():
    
#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_circumference(self):
#         C = 2 * 3.14 * self.radius
#         return C
    
#     def get_area(self):
#         A = 3.14 * self.radius ** 2
#         return A
# circle = Circle(3)
# print(circle.get_circumference())
# print(circle.get_area())




# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.baa = []

#     def student_baa(self, num):
#         self.baa.append(num)

#     def student_info(self):
#         if len(self.baa) > 0:
#             return sum(self.baa) / len(self.baa)
#         else:
#             return 0

# student = Student("ali")
# student.student_baa(5)      
# student.student_baa(5)    
# student.student_baa(5) 
# student.student_baa(5) 
# student.student_baa(5) 
# print(student.student_info()) 


# class Car(Bus):
#     def hunk(self):
#         print("Deep, dep!")

# car = Car ("toyota")
# car.driving()
# car.hunk()



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary

#     def display_info(self):
#         print(f"name - {self.name}")
#         print(f"salary - {self.name}")

# class Manager(Employee):
#     def __init__(self, name, salary, departament):
#         super().__init__(name, salary)
#         self.departament = departament

#     def display_info(self):
#         super().display_info()    
#         print(f"Departament - {self.departament}")

# emp =Employee("jony", 4000)
# manager = Manager("jack",5000,"sale")
# emp.display_info()
# print("------------------")
# manager.display_info()


# class Animal:
#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self):
#         print("мяу мяу")

# class Dog(Animal):
#     def make_sound(self):
#         print("гаф гаф")

# def make_sound(animal):
#     animal.make_sound()

# dog = Dog()
# cat = Cat()

# make_sound(dog)
# make_sound(cat)



# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Cat(Animal):
#     def speak(self):
#         return "мяу мяу"

# class Dog(Animal):
#     def speak(self):
#         return "гав гав"

# dog = Dog("Бека")
# cat = Cat("Муря")

# print(dog.name, dog.speak())
# print(cat.name, cat.speak())



# class Horse():
#     isHorse = True

# class Donkey():
#     isDonkey = True

# class Mule(Horse, Donkey):
#     pass

# mule = Mule()
# print(mule.isHorse)
# print(mule.isDonkey)



from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def str(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())