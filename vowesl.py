#!/usr/bin/python

#names = ["vivek","apple","owl","ink","samba"]
#vowel_words = []
#for name in names:
#	if name[0] in "aeiou":
#		vowel_words.append(name)
#print vowel_words
empty = []
def print_vowels(names):
	for i in names:
		if i[0] in "aeiou":
			 empty.append(i)
	return empty
names = ["vivek","apple","owl","ink","samba","also"]
a = print_vowels(names)
print a
