F = open('words.txt','a') 
f = open('top6000.txt','r')
x =0
for line in f:
	# x = x+1
	# print x
	x = line
	x = x.replace("$", "")
	# x = x.replace("2", "")
	# x = x.replace("3", "")
	# x = x.replace("4", "")
	# x = x.replace("5", "")
	# x = x.replace("6", "")
	# x = x.replace("7", "")
	# x = x.replace("8", "")
	# x = x.replace("9", "")
	# x = x.replace("0", "")
	x = x.strip().upper()
	if len(x) > 4:
		print x
		F.write('\n')
		F.write(str(x ).upper())

