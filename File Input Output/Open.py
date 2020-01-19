# "r" - Read

# "a" - Append

# "w" - Write

# "x" - Create

# "t" - Text

# "b" - Binary

# open & Read File

# filename = ["test.txt","test1.txt"]
# 	open('filename', 'r')
# 	for f in filename:
# 		print(f.name)
# 		f.close()

# f = open('test.txt', 'r') and #R - Read
# print(f.name)
# f.close()



# with open('test1.txt', 'a') as g:

# 	g.write('This is line number '+"\n")

# 	print(g,end='')


with open('test.txt', 'r') as f:

	# f_text = f.readline()
	# print(f_text,end='')

	# f_text = f.readline()
	# print(f_text,end='')

	# for x in f:
	# 	print(x,end='')

# 	f_text = f.readline()
# 	print(f_text,end='')

# 	for f_text in f:
# 		print(f_text,end='')

	# f_text = f.read(60)
	# print(f_text,end='')

	size_to_read = 100
	f_text = f.read(size_to_read)

	while len(f_text) > 0:
		print(f_text,end='')