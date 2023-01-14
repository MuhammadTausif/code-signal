#get file object
f = open("data.txt", "r")

while(True):
	#read next line
	no = f.readline()
	#if line is empty, you are done with all lines in the file
	if not no:
		break
	name = f.readline()
	#if line is empty, you are done with all lines in the file
	if not name:
		break
	#you can access the line
	print(no.strip() + "- " + name.strip())

	# create file from file names
	open(no.strip() + "- " + name.strip() + ".py", "x")

#close file
f.close