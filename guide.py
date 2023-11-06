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
list = [1, 3, 3, 9, 27, 233]  # list of integers
list[-1] = 243  # replace error 233 and put 243
list.append(6561)  # add a new item to the list and be put in last index
print(list)  # print the list
print(list[1])  # slicing the list
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
list.sort()  # arrange the list from smaller to bigger
print(list)  # print the list
listr.sort()  # arrange the list from smaller to bigger
print(listr)  # print the list
list.reverse()  # reverse the arrangement of the list (the last becomes first)
print(list)  # print the list
listr.reverse()  # reversr the arrangement of the list (the last becomes first)
print(listr)  # print the list
print(len(list))  # print the length of the list
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
#
#
#