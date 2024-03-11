# Why Python:?
# simple, easy to use, Popularity,Runs Everywhere(linux,windows...),Versatility.
# Slow , Memory hungry, Bad client side support
################################################################
# Loops?
# Dont repeat YourSelf.
################################################################
# What is imperative?
# Imperative is when you describe the exact technical steps needed for the solution. for i in range(len(array)):
# What is declarative?
# Declarative is when you describe the goal, or the general steps, and leave the details of the technical implementation to the computer. for num in nums
print("1.declarative")
arr = [1, 2, 3, 4, 5]
for index, val in enumerate(arr):
    print("Index:", index, "Value:", val)
print("\n2.iterator")


################################################################
# iterable objects:
# They help us iterate over a chain of objects, without the need to load them all at once. - they save us memory.
class OddNumbers:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1  # Start from the first odd number

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_num:
            raise StopIteration
        else:
            odd = self.current
            self.current += 2  # Move to the next odd number
            return odd


odd_iterator = OddNumbers(10)  # Generate odd numbers up to 10
for num in odd_iterator:
    print(num)
print("\n3.generate")


# Generator Function:
# Easy to read, understand
def generate_odd_numbers(max_num):
    current = 1
    while current <= max_num:
        yield current
        current += 2


odd_generator = generate_odd_numbers(10)
for num in odd_generator:
    print(num)
print("\n4.Lists vs Dictionaries vs Sets vs Tuples")
# Lists vs Dictionaries vs Sets vs Tuples
# Lists: Storing data in sequence.
# Dicts: Ordering data by logical keys. Fetching data quickly. Inserting data quickly.
# Sets : Storing unique values. When order of the values is not important. When the values are immutable(string,int.... not list[])
# Tuples: When you want to store values that cannot be changed. Store values in order.
################################################################################################################################
# my_list = [1, 2, 3, 4, 5]
# print(my_list[2])#3
# my_list.append(6)#add 6
# my_list.insert(2, 7)  # Insert 7 at index 2
# my_list.remove(3)  # Removes the first occurrence of 3
# popped_element = my_list.pop(2)  # Removes and returns element at index 2
# my_list.extend([8, 9, 10])
# length = len(my_list)
################################################################################################################################
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['a'])  # Output: 1
my_dict['d'] = 4  # Adding a new key-value pair
my_dict['a'] = 10  # Updating the value of an existing key
del my_dict['b']  # Removes the key-value pair with key 'b'
for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)
my_dict.clear()  # Removes all key-value pairs from the dictionary
new_dict = my_dict.copy()  # Creates a shallow copy of the dictionary.
length = len(my_dict)
################################################################################################################################
# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# my_set.remove(3)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1.union(set2)
# intersection_set = set1.intersection(set2)
# difference_set = set1 - set2
# for element in my_set:
#     print(element)
################################################################################################################################
# print("\n5. Mutable (by value) vs Immutable (by ref)")
# #string int float Boolean  NoneType
# x="1"
# y=x
# y+="2"
# print("x is ",x +" y is "+ y+"       x doesnot changed!")
# x=[1]
# y=x
# y.append(2)
# print("x is [1], y is [1,2]  x change")
################################################################################################################################
print("\n6. shallow_copy vs Deep copy")
# Shallow copy: nested mutable values are still passed by ref
# Deep copy: nested mutable values are passed by value.
import copy
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list)
print("Original list:", original_list)
original_list[0][0] = 100
print("original_list[0][0] = 100")
print("Shallow copied list:", shallow_copied_list)
print("Deep copied list:", deep_copied_list)
################################################################################################################################