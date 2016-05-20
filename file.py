f = open("names.txt","r")
string = []
for name in f:
	name = name.strip()
	string.append(name)
f.close()
print string
print (len(string))

for some in string:
	if some[0] == "T":
		print some
			
