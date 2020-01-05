# def - define

# def scope_test():
# 	def do_local():
# 		spam = "local spam"

# 	def do_nonlocal():
# 		nonlocal spam
# 		spam = "nonlocal spam"

# 	def do_global():
# 		global spam
# 		spam = "global spam"

# 	spam = "test spam"
# 	do_local()
# 	print("After local assignment:", spam)
# 	do_nonlocal()
# 	print("After nonlocal assignment:", spam)
# 	do_global()
# 	print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

# def say_hello():
# 	print('Hello World')

# say_hello()

# def say_hello():
# 	print('Hey Python')

# say_hello()

a = input('Please enter A Value:')
b = input('Please enter B value:')

def print_max(a, b):
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a, 'is equal to ', b)
	else:
		print(b, ' is maximum')
print_max(a, b)
# print_max()




# print_max(3, 4)
# x = 8
# y = 10
# print_max(x, y)



# print(20 > 10)
# print(20 == 10)
# print(20 < 10)
# print(bool("Hello World"))
# print(bool(20))



# Python Conditions

# Equals 						-> x == y
# Not Equals					-> x != y
# less than 					-> x < y
# less than or equal to 		-> x <= y
# greater than 				-> x > y
# greater than or equal to 	-> x >= y

def func(x):
	print('x is ', x)
	x = 2
	print('Changed local x to ', x)

x = 10
func(x)
print('x is still ', x)

------------------------------------
#eg

def func(y):
	print('y is ', y)
	y = 50
	print('Changed local y to ', y)

def funx(y):
	print('y is ', y)
	y = x + y
	print('Y is changed x + y', y)

x = 40
y = 20
func(y)
funx(y)
print('y is still ', y)

---------------------------------------

#Global Statement

def func(x):
	global x

	print('x is ', x)
	x = 2
	print('Changed global x to ', x)

x = 50
func(x)
print('Value of x is: ',x)

-------------------------------------------

#eg

def func():
	global y
	print('y is ', y)

	y = 100
	print('Value of y is: ', y)

y = 50
func()

print('Value of y: ',y)
-----------------------------------------
#eg
def do_global():
	global spam
	spam = 'global spam'

spam = 'test spam'
do_global()
print('After global assignment: ', spam)
-------------------------------------------
#eg.

# def func():
# 	nonlocal x
# 	print('x is ', x)
# 	x=5
# 	print('Value of x is:',x)

# x = 10
# func()
# print("Real Value of x is:",x)

def do_nonlocal():
	global spam
	spam = "global spam"

	nonlocal spam
	spam = "nonlocal spam"

spam = "test spam"
do_nonlocal()
print("After nonlocal assignment: ",spam)

def scope_test():
    def do_local():
            spam = "local spam"
    def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"
    spam = "test spam"
    do_local()
    print("After local assignment:",spam)
    do_nonlocal()
    print("After nonlocal assignment:",spam)

 scope_test()