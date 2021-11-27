import numpy as np
import pickle
import tensorflow as tf 

stocks = ["BSESN","INFY","NSEI","RELIANCE","SBI","TATASTEEL","TCS","TTM"]

def run3():
	for stock in stocks:
		X_train = pickle.load(open("X_train/"+stock+".pickle","rb"))
		y_train = pickle.load(open("y_train/"+stock+".pickle","rb"))

		X_train = np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1))
		model = tf.keras.models.Sequential()

		model.add(tf.keras.layers.LSTM(50,return_sequences=True,input_shape=(X_train.shape[1],1)))
		model.add(tf.keras.layers.LSTM(50,return_sequences=False))
		model.add(tf.keras.layers.Dense(25))
		model.add(tf.keras.layers.Dense(1))

		model.compile(optimizer='adam',loss='mean_squared_error')

		model.fit(X_train,y_train,batch_size=1,epochs=1)

		model.save("models\\"+stock+".model")