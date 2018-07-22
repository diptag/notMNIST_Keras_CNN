# notMNIST_Keras_CNN
My first Keras model trained on notMNIST_large dataset with tensorflow backend.
The model gives 97.14% accuracy on notMNIST_small dataset.

The dataset "notMNIST_large" can be downloaded from [here.](http://yaroslavvb.com/upload/notMNIST/notMNIST_large.tar.gz)

## notMNIST_small.pickle
Pickle file for normalized notMNIST_small dataset.
File contains a tuple with dataset and labels.
(X_test, Y_test_labels)

The original dataset "notMNIST_small" can be downloaded from [here.](http://yaroslavvb.com/upload/notMNIST/notMNIST_small.tar.gz)

All the Labels are in interger form with 0 for A and 9 for J.

## notMNIST_model.h5
Keras model trained on nonMNIST_large dataset.

## evaluate.py
Python script to evaluate the model on nonMNIST_small dataset.
