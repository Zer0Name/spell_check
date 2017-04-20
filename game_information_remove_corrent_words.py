F = open('game_information.txt','r') 
words = []
for line in F:
 	words.append(line.strip())
# print words

x = 0
while (x < len(words)-1):
	print "x"
	print x
	if len(words) == x:
		break
	correct = words[x]
	print correct[1:]
	
	typed = words[x+1]
	print typed

	x = x +2

	if correct[1:] == typed.upper():
		words.pop(x-2)
		words.pop(x-2)
		print "got to here"
		x = 0
		print x
	print "here"



print words
f = open('information_check.txt','a') 
for x in range (len(words)):
	f.write(str( words[x] + '\n').upper())
f.close()

F = open('information_check.txt','r') 
words = []
for line in F:
 	words.append(line.strip())
# print words
F.close()

if words[0] == '':
	words.pop(0)
	f = open('information_check.txt','w') 
	for x in range (len(words)):
		f.write(str( words[x] + '\n').upper())
	f.close()
else:
	f = open('information_check.txt','w') 
	for x in range (len(words)):
		f.write(str( words[x] + '\n').upper())
	f.close()


F.close()
F = open('game_information.txt','w')
F.close() 