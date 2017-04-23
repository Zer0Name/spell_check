f = open('text.txt','r')
F = open('newwords.txt','a') 

for line in f:
	x = line.strip().upper()
	if x[0] == "$":
		word = x[1:] 
		word1 = x[1]
		wordlast = x[len(x)-1]
		print word1
		print wordlast
		F.write(x+'\n')
	else:
		if x[0] == word1  and x[len(x)-1] == wordlast and len(x)>4:
			F.write(x+'\n')

