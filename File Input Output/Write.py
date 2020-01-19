with open('test.txt', 'r') as rf:
	with open('testCOPY.txt', 'w') as wf:

		for line in rf:
			wf.write(line)

# with open('cat.jpg', 'rb') as rf:
# 	with open('cat_copy.jpg', 'wb') as wf:

# 		for line in rf:
# 			wf.write(line)

#>>PIP