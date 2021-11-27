import pandas as pd
import sklearn.preprocessing
import numpy as np
stocks = ["BSESN","INFY","NSEI","RELIANCE","SBI","TATASTEEL","TCS","TTM"]

def run2():
	for stock in stocks:
		df = pd.read_csv('stock_list/'+stock+'.csv')
		df = df.dropna()
		df = df.reset_index(drop=True)
		
		data = df.filter(['Close'])
		dataset = data.values

		scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0,1))
		scaled_data = scaler.fit_transform(dataset)


		training_size = (len(df['Close'])) - 60
		train_data = scaled_data[0:training_size,:]

		X_train = []
		y_train = []

		for i in range(60,len(train_data)):
			X_train.append(train_data[i-60:i,0])
			y_train.append(train_data[i,0])

		X_train = np.array(X_train)
		y_train = np.array(y_train)

		import pickle 
		pickle_out = open("X_train/"+stock+".pickle","wb")
		pickle.dump(X_train,pickle_out)
		pickle_out.close()

		pickle_out = open("y_train/"+stock+".pickle","wb")
		pickle.dump(y_train,pickle_out)
		pickle_out.close()

