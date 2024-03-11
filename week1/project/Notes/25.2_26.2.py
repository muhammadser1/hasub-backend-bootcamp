print("\n\n25.2\n\n")
# Why Functions?:?
# making the code easier to understand, maintain, and debug.
# Encapsulation This improves the maintainability and readability of the code.
################################################################
# Functions are “first class citizens” in python:
# Functions Can Be Assigned to Variables
# Functions Can Be Passed as Arguments to Other Functions:
# Functions Can Be Returned by Other Functions:
print("\n1. Functions are “first class citizens” in python:\n")


def greet():
    print("hello")


hello_function = greet
hello_function()  # Output: Hello!
print("\n2. Create a function that takes a list and returns a new list with duplicate values:\n")


def dup_rec(lst, mode="init"):
    new_list = [None] * len(lst) if mode != "init" else [None] * len(lst) * 2
    for index, item in enumerate(lst):
        new_list[index] = item
        if isinstance(item, list):
            item = dup_rec(item, "nested")
        if mode == "init":
            new_list[index + len(lst)] = item
    return new_list


lst1 = dup_rec([1, 2, [3]])
print(lst1)
lst1[2].append(4)
print(lst1)
print("\n3. Recursions\n")
# Readability: Recursive solutions can be easier to read and understand, especially for problems that naturally lend themselves to recursive thinking.
# Versatility: Recursion is a powerful tool that can be used to solve a wide range of problems in various domains, including mathematics, computer science, and artificial intelligence.
# Debugging Complexity: Recursive solutions can be more challenging to debug and analyze compared to iterative solutions, especially for complex recursive functions with multiple recursive calls and base cases.
print("\n4. args - is you dont know how many params\n")


def args(*hobbies):
    for hobby in hobbies:
        print(hobby)


args("reading", "playing", "bowling")
print("\n5. lambda:\n")
double = lambda x: x * 2
print(double(5))
# using lambda - list comprehension
doubles = [x * 2 for x in range(10)]
print(doubles)

# show odds
odds = [x for x in range(20) if x % 2 != 0]
print(odds)

print("5. closure")


# can be returned (high order functions) - with closure
def custom_greet_factory(greet):
    def greet_fn(name):
        print(greet, name)

    return greet_fn


greet_ar = custom_greet_factory("marhaba")
greet_ar("yishai")

print("\n\n26.2\n\n")

print("\n6.multiple inheritance:\n")
# OOP:
# Organizing code!
# Managing our code in a logical way.
# IMPORTANT:
# Connecting many types of data together in a logical way.
# Reliability of code - little duplication.
# 1. Encapsulation: Putting data and methods that are related logically in one place.
# 2. Inheritance: it allows a new class to inherit properties and behavior from an existing class
# 3. Abstraction: Hiding the details from the user. (private)
# 4. Polymorphism: Overwriting methods while still keeping the methods you need
# Define the base classes
# Define the base classes
class Animal:
    def __init__(self, species):
        self.species = species
    def speak(self):
        print(f"The {self.species} speaks")
class Flyable:
    def __init__(self, speed):
        self.speed = speed
    def fly(self):
        print(f"Flying at speed {self.speed}...")
class Bird(Animal, Flyable):
    def __init__(self, species, speed):
        Animal.__init__(self, species)
        Flyable.__init__(self, speed)

bird = Bird("sparrow", 10)
bird.speak()
bird.fly()
print("\n7. composition over inheritance\n")
