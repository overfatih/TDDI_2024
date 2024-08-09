# my_mlp_model.py

from sklearn.neural_network import MLPClassifier

class TddiMlpModel:
    def __init__(self, hidden_layer_sizes=(100,), max_iter=200, random_state=None):
    	import pickle
    	model_path = 'profplay_tddi_model.pkl' 
    	with open(model_path, 'rb') as file:
    	        self.model = pickle.load(file)
             
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def score(self, X_test, y_test):
        return self.model.score(X_test, y_test)