from keras.callbacks import ModelCheckpoint
import numpy
import numpy as np
import pandas as pd
from keras.models import Model
from keras.models import Sequential
from keras.layers import Input, Dense, Dropout
from keras.layers import LSTM
from keras.utils import np_utils
from keras.preprocessing.sequence import pad_sequences
import random
# fix random seed for reproducibility
numpy.random.seed(7)
alphabet = []
# define the raw dataset
letters = """0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ `~!@#$%^&*()-_=+[]\{}|;':",./<>?  """
for letter in range (len(letters)):
	alphabet.append(letters[letter])


choice = raw_input("Do you want to add program yes/no : ")




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
	# 		break
	# f.close()
	if y == 0:
		f = open('data.txt','a') 
		f.write('\n')
		f.write(str('$' + correct_spell + '\n').upper())
		f.write(str(incorrect_spell + '\n').upper())
		f.close()
	else:
		exit()



if choice == "y":

	correct_spell = raw_input("please input corrent spelling of word: ")
	incorrect_spell = raw_input("please input incorrent spelling of word: ")

	add_to_database(incorrect_spell,correct_spell)





F = open('data.txt','r') 
for line in F:

	x = line.strip().upper()
	if x[:1] == '$':
		# print "doing nothing"
		print x[1:]
		alphabet.append(x[1:])
	else:
		alphabet.append(x)
		print x
    	#do nothing
F.close()




# create mappng of characters to words (0-25) and the reverse
char_to_int = dict((c, i) for i, c in enumerate(alphabet))
int_to_char = dict((i, c) for i, c in enumerate(alphabet))

# print (char_to_int)
# print "-----------------"
# print (int_to_char)


dataX = []
dataY = []
counter = 0
F = open('data.txt','r') 
for line in F:
    #print line.strip()
    x = line.strip().upper()
    if x[:1] == '$':
    	word = x
    	counter = counter +1
    else:       #([char_to_int[char] for char in sequence_in]) 
		dataX.append([char_to_int[char] for char in x]) 
		dataY.append(char_to_int[word[1:]])  

print "Number of words in the database: " + str(counter)
F.close()


# print dataX
# print dataY




max_len = 15
X = pad_sequences(dataX, maxlen=max_len, dtype='float32')
# X = pad_sequences(dataX, maxlen=max_len, dtype='float32')
# reshape X to be [samples, time steps, features]
X = numpy.reshape(X, (X.shape[0], max_len, 1))

X = X / float(len(alphabet))
print X.shape
# one hot encode the output variable
y = np_utils.to_categorical(dataY)

# print X
# print len(dataY)
# print len(y[0])

p = random.randint(1,1000000000000)

name = str(str(p) + "test")


if choice == "hash":

	F = open('last_state_name_layer2.txt','w')
	F.write(name)
	F.close()
else:
	if choice != "y":

		F = open('last_state_name_layer2.txt','r')
		for line in F:
			name = line.strip()
		F.close()

	else:

		F = open('last_state_name_layer2.txt','w')
		F.write(name)
		F.close()





print "Updating System....."

batch_size = 1

model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True , name = "first_layer"))
model.add(LSTM(256, name = "second_layer"))
model.add(Dense(y.shape[1], activation='softmax',name = name ) )
try:
	model.load_weights("weights_layer2.hdf5", by_name=True) 
except:
	print "file not there"
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

filepath="weights_layer2.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

model.fit(X, y, epochs=40, batch_size=batch_size, verbose=2,validation_split=0.001, callbacks=callbacks_list, shuffle= True)
#validation_split=0.001
#, batch_size=batch_size
# print (model.summary())

print "Finish Updating System"

# Evaluate
loss, accuracy = model.evaluate(X, y, verbose=1, batch_size=batch_size)
print('loss: ', loss)
print('accuracy: ', accuracy *100)








