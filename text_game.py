from __future__ import print_function
import random
import time

F = open('top6000.txt','r') 
alphabet = []
for line in F:

	x = line.strip().upper()
	if x[:1] == '$':
		# print "doing nothing"
		alphabet.append(x[1:])
    	#do nothing
F.close()

while True:
	p = random.randint(1,len(alphabet)-1)

	word = alphabet[p]
	print("\r" + word, end="     ")
	filename= raw_input('').upper() 

	if filename == "END GAME":
		break

	if filename !='':

		f = open('game_information.txt','a') 
		f.write('\n')
		f.write(str('$' + word + '\n').upper())
		f.write(str(filename ).upper())
		f.close()


F = open('game_information.txt','r') 
words = []
for line in F:
 	words.append(line.strip())
# print words
F.close()

y = 0
while  y < len(words):
	if words[y] == '' or words[y] == ' ':
		words.pop(y)
		f = open('game_information.txt','w') 
		for x in range (len(words)):
			f.write(str( words[x] + '\n').upper())
		f.close()
		y =0
	else:
		f = open('game_information.txt','w') 
		for x in range (len(words)):
			f.write(str( words[x] + '\n').upper())
		f.close()
		y = y+1

