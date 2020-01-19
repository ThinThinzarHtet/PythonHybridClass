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

# uppercase = text.isupper()
try :
	text = input("Enter your password: ")
	if len(text) < 8:
		raise ShortPwdException(len(text), 8)

	if len(text) > 72:
		raise LongPwdException(len(text), 72)

	if not re.findall("[A-Z]", uppercase):
		raise UppercaseException("[A-Z]", text)
except ShortPwdException as ex:
	print("ShortPwdException: Your entered password was too short. Should be minimum {}".format(ex.atleast))

except LongPwdException as ex:
	print("LongPwdException: Your entered password was too long. It should be maximum {}".format(ex.atleast))

except UppercaseException as ex:
	print("UppercaseException: Your enetered password should include at least one uppercase character")
time.sleep(5)
input("Press any key to exit...")