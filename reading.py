f = open("scores.txt","r")
participant_dictionary = {}
for line in f:
	#print(line.strip().split(","))
	entry = line.strip().split(",")
	participant = entry[0]
	score = entry[1]
	#print participant
	#print score
 	participant_dictionary[participant] = score

f.close()	
print participant_dictionary
