F = open('information_check.txt','r') 

def add_to_database(incorrect_spell,correct_spell):
	incorrect_spell = incorrect_spell.upper()
	correct_spell = correct_spell.upper()
	f = open('data.txt','r')
	y =0
	# for line in f:
	# 	x = line.strip().upper()
	# 	if str(x) == str(incorrect_spell):
	# 		y = 1
	# 		print "error: word already installed"
	# f.close()
	if y == 0:
		f = open('data.txt','a') 
		f.write(str(correct_spell + '\n').upper())
		f.write(str(incorrect_spell + '\n').upper())
		f.close()


words = []
for line in F:
	words.append(line.strip().upper())
F.close()

while True:
	F = open('information_check.txt','r') 
	words = []
	for line in F:
		words.append(line.strip().upper())
	F.close()
	print words[0]
	print words[1]
	choice = raw_input("y/n: ")
	if choice == "y":
		add_to_database(words[1],words[0])
		F = open('information_check.txt','w') 
		for x in range (2,len(words)):
			F.write(str( words[x] + '\n').upper())
		F.close()
	else:
		F = open('information_check.txt','w') 
		for x in range (2,len(words)):
			F.write(str( words[x] + '\n').upper())
		F.close()
