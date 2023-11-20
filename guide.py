age = 22  # int بنعرف متغير نوعه
name = "Youssef"  # string بنعرف
print(f"my name is {name} and age is {age}")  # formatted string بنطبع
print("my name is {} and age is {}".format(
    name, age))  # نفس اللى فوق بطريقة تانية
# escape sequences كمان استخدمنا concatenation الطباعة عن طريق
print("my name is\n \"" + name + "\" and age is " + str(age))
# بتنزل سطر تلقائيا فهنا حددنا ان النهاية تكون مسافة بدل سطر جديد printال
print("hello", end=" ")
print("world")  # hello هتطبع بعد مسافة من
g = '''sjskhka assad
sjdksjda bsjnds
klsa
'''  # بتسمح انى اكتب على اكتر من سطر '''
print(g*2)  # مرتين g بكرر ال
print(name.replace("o", "a"))  # a ل o بغير ال
txt = "The good place"  # عادى string عرفت
# indx 2 هنا بطبع indx 3 فبالتالى بيطبع ليست ب txt قسمت ال
print(txt.split()[2])
print(len(name))  # stringطول ال
print(len(g))  # stringطول ال
print(len(txt))  # stringطول ال
# syntax of slicing->string[start:end]
print(name[0])  # array of characters على انه stringبيعامل الindexingال
print(txt[:])  # slicing showing all string
print(txt[:9])  # slicing from range(beginning char to indx 9)
print(txt[7:])  # slicing from range(indx 7 to last char)
print(txt[7:10])  # slicing from range(indx 7 to indx 10)
print(txt[7:-3])  # slicing from range(indx 7 to indx -3 => indx 3 from last)
# pycode style => pycodestyle --first --show-source --show-pep8 --statistics -qq
x = 12
y = 1
if x > 8:
    print("x is greater than 7")  # true الشرط يتحقق لو
elif x == 12:
    print("I am 12")
else:
    print("Not true")  # false الشرط يتحقق لو
# nested if
if x == 12:
    if y == 1:
        print("Both are true")
    else:
        print("Y isn't 1")
else:
    print("X isn't 12")
# assign values to variables
num = 100
noun = "This"
pi = 22/7
isplayed = True
# perform calculations and assigning result to a new variable
n1 = 23
n2 = 15
sum = n1 + n2
# reassigning
ty = 7
print(ty)
ty = 123
print(ty)
# assign multiple variables on same line
gh, im, yu = 4, "asd", 5.9
print(yu, im, gh)
# swap var val
cv = 8
vc = 2
cv, vc = vc, cv
print("cv: ", cv)  # cv: 2
print("vc: ", vc)  # vc: 8
# type() show the data type of a variable
print(type(cv))  # output: <class 'int'>
# while loop
count = 0
while count < 6:
    # using break
    '''if (count == 3):
            continue # skip this iteration when count is 3 '''
    if (count == 5):
        break  # exit the loop when count is 5
    print("count =", count)
    count += 1
else:
    print("continue without reaching count 5")
# for loop
fruits = ["watermelon", "banana", "pear"]
for fruit in fruits:
    print("Fruit:", fruit)
    if fruit == "apple":
        print("apple found, breaking loop.")
        break
else:  # using else with for or while loops
    print("Loop completed without finding apple")
if "ABC" == "abc":
    pass  # عدى
print("true")
# range in for loop
for num in range(5):  # generates numbers from 0 to 4
    print(num)
for no in range(2, 6):  # بداية:2 و نهاية:5 من 2 ل 6
    print(no)
for odd in range(1, 10, 2):  # انشاء ارقام فردية الخطوات 2 من 1 ل 10 و 10 مش معانا
    print(odd)
for rev in range(10, 0, -1):  # print reversed numbers 10 : 1 (0 not printed)
    print(rev)
# defining a function


def greet(name):
    print("hi", name)


# calling the function
greet("Youssef")
# add function


def add(cx, cy):
    return (cx + cy)


ssum = add(2, 9)
print(ssum)  # output: 11
# no return value


def noret():
    print("no return statement")


print(noret())  # output: none
# scope of variables
glob_var = 21  # global variable can be accessed anywhere


def outer_func():
    # Enclosing scope (outer_func)
    outer_var = 20

    def inner_func():
        # Enclosing scope (inner_func)
        inner_var = 12
        print(inner_var)  # Accessible here

    inner_func()
    print(outer_var)  # Accessible here


outer_func()
print(glob_var)  # Accessible here

# print(inner_var) error -> output:
# Traceback (most recent call last):
#   File "c:/Users/Youss/python projects/guide.py", line 131, in <module>
#     print(inner_var)
#           ^^^^^^^^^
# NameError: name 'inner_var' is not defined

# Arethmatic operators:
# ---------------------
# (+) addition -> 2 + 3 = 5
# (-) subtraction -> 5 - 3 = 2
# (*) multiplication -> 2 * 4 = 8
# (/) division(float) -> 8 / 4 = 2
# (//) floor division(integer) -> 15 // 2 = 7
# (%) modulus(remainder) -> 17 % 4 = 1
# (**) exponention(power) -> 2 ** 3 = 8
# (-) unary negation(negate value) -> -num => negative
# (+) unary positive(indicate positive) -> +num => positive

# import and module
# module is a .py file that can be imported using import

# for example we have a module called mo.py
#    we can 'import mo' and then use any function in it
#    using 'mo.add(9, 3)'
#    we can also import fuction from module
#    in order not to use .
#    'from mo import add'
#    'add(9, 3)'

if __name__ == "__main__":
    import fibo  # fibo اللى اسمه module بنادى على ال
    fibo.fib(129)  # fib اللى اسمها funcبستدعى ال
    print(dir(fibo))  # module fiboبتاعة ال dir بطبع ال
lista = [1, 3, 3, 9, 27, 233]  # list of integers
lista[-1] = 243  # replace error 233 and put 243
lista.append(6561)  # add a new item to the list and be put in last index
print(lista)  # print the list
print(lista[1])  # slicing the list
listr = ["Youssef", "Name", "Play", "Done"]  # list of string
print(listr)  # print the list
listmix = [1, "name", 2.3, False]  # list of mixed data types
listmix[3] = True  # changing the value of list at index 3
listmix.insert(0, 122)  # inserting 122 at index 0 instead of 1
listmix.remove(1)  # remove index 1
# p = True and True is removed from listmix void pop()[last index]
p = listmix.pop()
print(p)  # print the last index value of the list
print(listmix)  # print the list
print(listmix.pop(0))  # print index 0 which = 122
print(listmix)  # print the list
# showing the index number of 2.3 (first appearance)
indxx = listmix.index(2.3)
print(indxx)  # printing 1 index number of 2.3
listmix.append(3)  # add 3 to last index
listmix.append(5)  # add 5 to last index
listmix.append(3)  # add 3 to last index
listmix.append(4)  # add 4 to last index
listmix.append(3)  # add 3 to last index
listmix.append(2.3)  # add 2.3 to last index
cnt = listmix.count(3)  # showing how many 3 element come in the list
cnt2 = listmix.count(2.3)  # showing how many 2.3 element come in the list
print(listmix)  # print the list
print(cnt)  # output is 3
print(cnt2)  # output is 2
lista.sort()  # arrange the list from smaller to bigger
print(lista)  # print the list
listr.sort()  # arrange the list from smaller to bigger
print(listr)  # print the list
lista.reverse()  # reverse the arrangement of the list (the last becomes first)
print(lista)  # print the list
listr.reverse()  # reversr the arrangement of the list (the last becomes first)
print(listr)  # print the list
print(len(lista))  # print the length of the list
print(len(listr))  # print the length of the list
print(len(listmix))  # print the length of the list
print(len(listmix) - 1)  # print the no. of index of the list

# List comprehension: a concise way to create lists based on existing ones:
# -------------------------------------------------------------------------
comlist = [] # here is a comprehensed list (a void list)
for i in range(12): # in this for loop we iterate from 0 to 11
    comlist.append(i) # here we append i to the comlist
print(comlist) # then printing the list and this illustrates the List comprehension
# # # # # # # # # # # # # # # Another examples # # # # # # # # # # # # # #
square = [x ** 2 for x in range(1, 6)] # iterate on x from 1 to 6 then perform x ** 2
print(square) 				 	 	   # then put the result in a list and print it here
even_nums = [x for x in square if x & 1 == 0] # if x (in square list) & 1 == 0 or x % 2 == 0
#even_nums = [x for x in square if x % 2 == 0] -> if x (in square list) & 1 == 0 or x % 2 == 0
print(even_nums)							  # print the even_nums list
# --------------------------------------------------------------------------

# using list as a stack which is a data structure that follows the
# Last-In-First_Out (LIFO) principle i.e: elements are added and removed
# from the same end of the stack:  اخر عنصر دخلته هو اول عنصر طلع
# -------------------------------
stack = []
# push elements into stack
stack.append(1)
stack.append(2)
stack.append(3)   # stack: [1, 2, 3]
#pop element from stack
popped_element = stack.pop()
print("popped:", popped_element) # output: popped: 3
# the stack now contains [1, 2]
print("stack:", stack) # output: stack: [1, 2]

#-------------------------------------------------

# using list as a queue which is a data structure that follows
# First-In-First_Out (FIFO) principle i.e: elements are added at one end
# and removed from the other end of the queue: اول عنصر بندخله هو اللى بيخرج الأول
# -------------------------------------------
queue = []
# Enqueue elements in the queue
queue.append("a")
queue.append("b")
queue.append("c") # queue: ["a", "b", "c"]
#Dequeue elements from the queue
dequeued_element =  queue.pop(0)
print("Dequeued:", dequeued_element) # output: Dequeued: a
#The queue now contains ["b", "c"]
print("Queue:", queue) # output: Queue: ["b", "c"]
# --------------------------------------------------------------------------

# Tuples:
# -------
# They are another built-in data types in python, similar to lists.
# However, there are some key differences between tuples and lists.
# Tuples (as strings) are immutable لا تتغير , ordered collections of
# items. Once created, the elements of a tuple cannot be changed, added or removed.
# creating tuples:
# ----------------
# Tuples are created by enclosing a comma-separated sequence of
# values within parantheses ()

# creating a tuple
my_tuple = (1, 3, True,"Ahmed", "Mohammed", "Youssef")
# tuple can be created without parantheses, using just commas
# my_tuple = 1, 3, True,"Ahmed", "Mohammed", "Youssef"
print(my_tuple[0]) # output: 1
print(my_tuple[2]) # output: True
print(my_tuple[3]) # output: Ahmed
print(my_tuple.count(3)) # show how many 3 in tuple (only 1 time)
print(my_tuple.index("Ahmed")) # give the index representing the value "Ahmed" (index 3)
print("==============")
# access the elements of the tuple and printing them
for i in my_tuple:
    print(i)
# Tuple packing and unpacking:
# Packing is a process of combining multiple values into single tuple.
# Unpacking is the process of extracting values from a tuple and assigning
# them to multiple variables.
# Packing values into a tuple
coordinate = 3.14, 2.71
# Unpacking values from a tuple
x, y = coordinate
print(x) # output: 3.14
print(y) # output: 2.71
# Using tuples for multiple return values:
# Tuples are often used to return multiple values from functions
def get():
    return "JOO", 22
name, age = get() # unpacking
print(name) # output: JOO
print(age) # output: 22

# Tuples are immutable
# t = (1, 3)
# t[1] = 2 will give an error

# The del statement in python is used to delete objects, variables,
# Or elements from sequences, such as lists or dictionaries
# Deleting variables
x = 10
del x
#Deleting elements from lists
numbers = [1, 2, 3, 4, 5]
del numbers[3] # removes the element at index 3 (value 4)
# Deleting slices from lists:
del numbers[1:3] # remove elements at indices 1 and 2 (value 2 and 3)
print(numbers)
# data structures: set and dictionary
# set: a built-in data type useful when you want to store a
# collection of items where each item appears only once and
# the order of theitems doesn't matter
# creating a set: you can create a set by enclosing a comma-separated
# list of elements within curly braces
my_set = {4, 5, 6, "Joo", False}
print(my_set)
# we can create a set from a list using the set() constructor
m_list = [22, 34, 12, "AAA"]
set2 = set(m_list) # create a set from a list
my_set.add(900) # adding 900 to the set 3 times
my_set.add(900) # but it will appear only once
my_set.add(900) # so my_set = {False, 4, 5, 6, 900, 'Joo'}
print(my_set)
my_set.remove(4) # remove element not index
print(my_set)
print(my_set.pop()) # show any element
my_set.clear() # clears the set
print(my_set)
s3 = set2.copy() # copy set2 in s3
print(s3)
ssa = {'a', 2, 5, 6}
ssb = {'b', 3, 6, 5}
ssc = ssa | ssb # | is union or union(other_set)
print(ssc)
ssd = ssa & ssb # & is intersection or intersection(other_set)
print(ssd)
sse = ssa - ssb # - is difference or difference(other_set)
# the difference occurs for first set only
print(sse)
ssf = ssa ^ ssb # ^ is the symmetric_difference or
# symmetric_difference(other_set) the difference occurs for first and second
# set
print(ssf)
# we can iterate through sets
for i in ssf:
    print(i, end=" ")
# Dictionary: it is a built_in data structure that stores a collection
# of key-value pairs. Each key in a dictionary is unique and maps to a
# specific value.
# Dictionaries are useful when you want to associate data with specific
# labels (keys) for efficient and quick access
# Creating a dictionary: you can create a dictionary by enclosing a
# comma-separated list of key-value pairs within curly brace {}
print()
my_dict = {"Name" : "Joo", "age" : 22, "Color" : "Red"}
# we can also use dict() constructor to make a dictionary
print(my_dict)
# access the value of a specific key
print(my_dict["Name"])
# modifying the value of a specific key
my_dict["Color"] = "Blue"
print(my_dict["Color"])
# adding a new item mto dictionary
my_dict["City"] = "Cairo"
print(my_dict)
# removing an item using pop which prints the deleted item
# or del which remove the item without printing it
print(my_dict.pop("Color"))
print(my_dict)
del my_dict["City"]
print(my_dict)
# checking for a key if it presents in a dictionary
if 'Name' in my_dict:
    print("Yes it exists")
else:
    print("Not found")
# iterate through keys
for key in my_dict:
    print(key)
# iterate through values
for value in my_dict.values():
    print(value)
# iterate through both key and value
for key, value in my_dict.items():
    print(key, value)
# A lambda function in python is a small, anonymous, and inline function
# that can have any number of arguments, but have one expression.
# It is sometimes referred to as an "anonymous function" because
# it doesn't require a named function definition using the def keyword
addd = lambda yx, yy: yx + yy
nateg = addd(3, 12)
print(nateg) # output: 15
# equal to
def adsd(aa, bb):
    return aa + bb
ress = adsd(3, 12)
print(ress) # output: 15
# A map(function, sequence): The map() function applies a given
# function to each element in a sequence (such as a list) and return
# a new sequence containing the results
numms = [1, 2, 3, 4, 5, 6]
squared = map(lambda Ux: Ux ** 2, numms)
squared_list = list(squared)
print(squared_list)
print(numms)
# A filter(function, sequence): The filter() function filters elements
# from a sequence based on whether they satisfy a given function
# (predicate). It returns a new sequence containing only the element
# that pass the filter
print(list(filter(lambda ni: ni % 2 == 0, numms)))
# A reduce(function, sequence): The reduce function , previously part
# of the functools module (in python 3.0+), succesively applies a given
# function to the elements of a sequence, reducing it to a single
# accumulated result.
from functools import reduce
print(reduce(lambda vu, bu:vu * bu, numms))
# Python exception
try:
    result = 1 / 0 # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("ERROR: Division by zero")

try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please Enter a valid number")
except KeyboardInterrupt:
    print("User interrupted the input")

try:
    ctv = 92 / 0
except (ZeroDivisionError, KeyboardInterrupt):
    print("Zero division error and keyboard")

try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    qout = numerator / denominator
except ValueError:
    print("Invalid input. You should enter integer values")
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("Result: ", qout)
finally:
    print("Exception handling completed")

# You can raise built-in exceptions using raise statements
def divide(aa, bb):
    if bb == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return aa / bb
# print(divide(12, 0))

def process_file(file_path):
    if not file_path.endswith(".txt"):
        raise ValueError("Invalid file format. only .txt are allowed")
# print(process_file("guide.py"))

# try...except to open a file
try:
    file = open("data.txt", "r")
except FileNotFoundError as error:
    print("File not found!", error)
finally:
    file.close()

#
#



