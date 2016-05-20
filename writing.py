f = open("scores.txt","w")

while True:
	
	participant = raw_input("Participant name >")
	if participant == "quit":
		print("Quitting ...")
		break
	scores = raw_input("Participant Score >")
	f.write(participant + "," + scores + "\n")

f.close()
