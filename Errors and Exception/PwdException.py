import time
import re
class ShortPwdException(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

class LongPwdException(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

class UppercaseException(Exception):
	def __init__(self, uppercase):
		self.uppercase = uppercase

class LowercaseException(Exception):
	def __init__(self, lowercase):
		self.lowercase = lowercase

class NumberException(Exception):
	def __init__(self, number):
		self.number = number

uppers = 0
upperlist = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()

lowers = 0
lowerlist = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

numbers = 0
numberslist = "1 2 3 4 5 6 7 8 9 0".split()
try :
	text = input("Enter your password: ")
	if len(text) < 8:
		raise ShortPwdException(len(text), 8)

	if len(text) > 72:
		raise LongPwdException(len(text), 72)

	if not re.search(r"[A-Z]+", text):
		raise UppercaseException()

	for char in text:
		if char in upperlist:
			uppers += 1
		raise UppercaseException(upperlist)

	for char in text:
		if char in lowerlist:
			lowers += 1
		raise LowercaseException(lowerlist)

	for char in text:
		if char in numberslist:
			numbers += 1
		raise NumberException(numberslist)

except ShortPwdException as ex:
	print("ShortPwdException: Your entered password was too short. Should be minimum {}".format(ex.atleast))

except LongPwdException as ex:
	print("LongPwdException: Your entered password was too long. It should be maximum {}".format(ex.atleast))

except UppercaseException as ex:
	print("UppercaseException: Your entered password should include at least one uppercase character")

except LowercaseException as ex:
	print("LowercaseException: Your entered password should include at least one lowercase character")

except NumberException as ex:
	print("NumberException: Your entered password should include at least one number")
time.sleep(5)
input("Press any key to exit...")