import perdiction
class main:

	def __init__(self,filename):
		self.d = perdiction.perdiction()
		self.filename  = filename
		self.string = self.load_file(filename)
		print self.string
		self.words = self.load_words()
		self.change_words()
		print self.string

	def load_file(self,filename):
		F = open(filename,'r') 
		string = ""
		for line in F:
			string = string + line
		F.close()

		string = string.split()
		for i in range(len(string)):
			string[i] = string[i].rstrip('?:!.,;')

		return string


	def load_words(self):
		F = open("word_list.txt",'r')
		words = []
		for line in F:
			words.append(line.strip())
		return words

	def change_words(self):
		# d.perdict(text)
		for x in range(len(self.string)):
			z =0
			for w in range(len(self.words)):
				if self.string[x].lower() == self.words[w]: #the word is spelled correctly
					#print self.string[x]
					z =1
				elif len(self.string[x])==1:
					s = list(self.string[x])
					# print type(s[0])
					# print type(chr(ord(s[0])+2))
					if not chr(ord(s[0])+2).isalpha():
						z=1
				
			if z == 1:
				print self.string[x]
			else:

				# perdict word and change word in file
				self.string[x]  = self.d.perdict(self.string[x]).lower()











text = raw_input("enter a file name: ")
d = main(text)


