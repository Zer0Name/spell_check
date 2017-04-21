from keras.callbacks import ModelCheckpoint
import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import LSTM
from keras.utils import np_utils
from keras.preprocessing.sequence import pad_sequences
import os

class perdiction:
	def __init__(self):
		#remove all output
		os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
		self.data = "data.txt"
		self.alphabet = [] 
		self.char_to_int = []
		self.int_to_char = []
		self.length =self.load_data(self.alphabet,self.char_to_int,self.int_to_char,self.data)
		self.model = self.load_model()


	def load_data(self, alphabet, char_to_int, int_to_char,data):

		letters = """0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ `~!@#$%^&*()-_=+[]\{}|;':",./<>?  """
		for letter in range (len(letters)):
			self.alphabet.append(letters[letter])
			
		F = open(data,'r') 
		for line in F:
			x = line.strip().upper()
			if x[:1] == '$':
				# print "doing nothing"
				self.alphabet.append(x[1:])
			else:
				self.alphabet.append(x)
		F.close()
		
		# create mapping of characters to integers (0-25) and the reverse
		self.char_to_int = dict((c, i) for i, c in enumerate(self.alphabet))
		self.int_to_char = dict((i, c) for i, c in enumerate(self.alphabet))

		dataX = []
		dataY = []
		F = open(data,'r') 
		for line in F:
		    #print line.strip()
		    x = line.strip().upper()
		    if x[:1] == '$':
		    	word = x
		    else:       #([char_to_int[char] for char in sequence_in]) 
				dataX.append([self.char_to_int[char] for char in x]) 
				dataY.append(self.char_to_int[word[1:]])  
		F.close()

		max_len = 15
		X = pad_sequences(dataX, maxlen=max_len, dtype='float32')
		# X = pad_sequences(dataX, maxlen=max_len, dtype='float32')
		# reshape X to be [samples, time steps, features]
		X = numpy.reshape(X, (X.shape[0], max_len, 1))

		X = X / float(len(self.alphabet))
		# one hot encode the output variable
		y = np_utils.to_categorical(dataY)
		return y.shape[1]


	def load_model(self):
		F = open('last_state_name.txt','r')
		for line in F:
			name = line.strip()
		F.close()

		model = Sequential()
		model.add(LSTM(256, input_shape=(15, 1), return_sequences=True , name = "first_layer"))
		model.add(LSTM(256,return_sequences=True , name = "second_layer"))
		model.add(LSTM(256, name = "third_layer"))
		model.add(Dense(self.length, activation='softmax',name = name ) )
		model.load_weights("weights.hdf5", by_name=True) 

		return model



	def perdict(self,filename):
		filename = filename.upper()

		data = []
		data.append([self.char_to_int[char] for char in filename]) 
		max_len = 15
		pattern = pad_sequences(data, maxlen=max_len, dtype='float32')
		X = numpy.reshape(pattern, (pattern.shape[0], max_len, 1))
		X = X / float(len(self.alphabet))
		prediction = self.model.predict(X, verbose=0)
		index = numpy.argmax(prediction)
		result = self.int_to_char[index]
		return (result)

d = perdiction()
while True:
	text = raw_input("enter a word: ")
	print d.perdict(text)


