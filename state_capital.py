capitals_dict = {
'Telangana':'Hyderabad',
'Goa':'Panaji',
'Texas':'Austin',
'Maharashtra':'Mumbai',
'Virginia':'Richmond',
'Tennessee':'Nashville',
'Utah':'Salt Lake City',
'Washington':'Olympia',
}
import random
states = list(capitals_dict.keys())
for i in [1,2,3,4,5]:
	state = random.choice(states)
	capital = capitals_dict[state]
	#print state
	#print capital
	capital_guess = raw_input("What is the capital of " + state +" ? ")
	
	if capital_guess == capital:
		print("Correct! Nice Job.")
	else:
		print("Incorrect. The captial of "+ state + " is" + " capital" + ".")
print "All Done!" 
