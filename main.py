import perdiction
import re
class main:

	def __init__(self,filename):
		self.d = perdiction.perdiction()
		self.filename  = filename
		self.string = self.load_file(filename)
		#print self.string
		self.words = self.load_words()
		self.change_words()
		#print self.string
		self.string = self.recomple()
		print self.string

	def load_file(self,filename):
		F = open(filename,'r') 
		string = ""
		for line in F:
			string = string + line
		F.close()
		string = re.findall(r"[\w']+|[.,!?;]", string)
		# for i in range(len(string)):
		# 	string[i] = string[i].rstrip('?:!.,;')
		#print "got to here"
		 
		#print string
		return string


	def load_words(self):
		F = open("word_list.txt",'r')
		words = []
		for line in F:
			words.append(line.strip().lower())
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
					if not chr(ord(s[0])+2).isalpha():
						z=1
				
			if  not z == 1:
				if self.string[x].isalpha():
					print self.string[x]
					print self.d.perdict(self.string[x]).lower()
					self.string[x]  = self.d.perdict(self.string[x]).lower()


	def recomple(self):
		#self.string=join(self.string)
		for x in range(len(self.string)-1):
			if not(len(self.string[x+1])==1) or (len(self.string[x+1])==1 and chr(ord(self.string[x+1])+2).isalpha()):
				#if here... next "word" is NOT punctuation
				if not self.string[x+1] == "?":

					self.string[x] = self.string[x]+" "

		# does not work for dialouge
		for y in range(len(self.string)):
			if y==0:
				r= list(self.string[y])
				r[0] = r[0].upper()
				self.string[y]=''.join(r)
			elif self.string[y-2] == '.' or self.string[y-2] == '?' or self.string[y-2] == '!':
				w= list(self.string[y])
				w[0] = w[0].upper()
				self.string[y]=''.join(w)
		self.string = ''.join(self.string)
		return self.string




text = raw_input("enter a file name: ")
d = main(text)


