from keras.models import load_model
from keras.utils import to_categorical, plot_model
import pickle

# Load data from pickle file
with open("notMNIST_small.pickle", "rb") as f:
    (X_test, labels) = pickle.load(f)

# Convert labels to one-hot-encoding
Y_test = to_categorical(labels, num_classes = 10)
print ("Number of examples:", X_test.shape[0])

# Load Model
model = load_model("notMNIST_model.h5")

# Evaluate Model
scores = model.evaluate(X_test, Y_test)
print ("Loss:", scores[0])
print("%% Accuracy: %4.2f%%" % (scores[1] * 100))

