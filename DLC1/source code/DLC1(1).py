import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

#Here First i imported the data
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#This is the dataset taken
dataset = pd.read_csv("diabetes.csv", header=None).values

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:8], dataset[:,8],
                                                    test_size=0.23, random_state=86)
np.random.seed(155)
# used to create model
my_first_nn = Sequential() 
 #This is the hidden layer
my_first_nn.add(Dense(30, input_dim=8, activation='relu'))
my_first_nn.add(Dense(30, activation='relu'))
 # This is the output layer
my_first_nn.add(Dense(1, activation='sigmoid'))
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
#Here i print the accuracy 
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test))
