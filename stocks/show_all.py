import pickle
import numpy as np
import pandas as pd
import sklearn.preprocessing
import tensorflow as tf 
import matplotlib.pyplot as plt 

stocks = ["BSESN","INFY","NSEI","RELIANCE","SBI","TATASTEEL","TCS","TTM"]

def run4():
	for stock in stocks:
		df = pd.read_csv('stock_list/'+stock+'.csv')
		df = df.dropna()
		df = df.reset_index(drop=True)
		data = df.filter(['Close'])
		dataset = data.values

		scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0,1))
		scaled_data = scaler.fit_transform(dataset)


		training_size = (len(df['Close'])) - 180
		train_data = scaled_data[0:training_size,:]

		test_data = scaled_data[training_size-60:,:]

		X_test = []
		y_test = dataset[training_size:,:]
		for i in range(60,len(test_data)):
			X_test.append(test_data[i-60:i,0])


		X_test = np.array(X_test)
		X_test = np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))

		model = tf.keras.models.load_model("models/"+stock+".model")

		df = pd.read_csv('stock_list/'+stock+'.csv')
		data = df.filter(['Close'])
		dataset = data.values
		scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0,1))
		scaled_data = scaler.fit_transform(dataset)


		y_ans = model.predict(X_test)
		y_ans = scaler.inverse_transform(y_ans)


		training_size = (len(df['Close'])) - 180
		train = data[:training_size]
		date = df.filter(['Date'])

		date = date.values
		TDate = date[:training_size]
		TeDate = date[training_size:]



		valid = {
			"TDate" : TDate,
			"TeDate" : TeDate,
			"train" : train,
			"Close" : data[training_size:],
			"Prediction" : y_ans
		}
		pickle_out = open("results/"+stock+".pickle","wb")
		pickle.dump(valid,pickle_out)
		pickle_out.close()