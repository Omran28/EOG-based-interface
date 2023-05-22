import os
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle


def logistic_reg(x_train, y_train, x_test, y_test, feature_name):
    # Create a logistic regression model
    logreg = LogisticRegression()

    # Fit the model to the data
    logreg.fit(x_train, y_train)

    # Make predictions on the training data
    y_pred = logreg.predict(x_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)

    print('Accuracy Logistic reg using ' + feature_name + ": " + str(accuracy * 100))


def decision_tree(x_train, y_train, x_test, y_test, feature_name):
    filename = 'DT_model' + feature_name + '.pkl'
    if not os.path.exists(filename):
        # Create a decision tree model
        tree = DecisionTreeClassifier()

        # Fit the model to the data
        tree.fit(x_train, y_train)
        with open(filename, 'wb') as file:
            pickle.dump(tree, file)
        print('Model saved successfully.')
    else:
        print('Model file already exists.')

    # Load the model if the file exists
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            tree = pickle.load(file)

        # Make predictions on new data
        y_pred = tree.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        print('Accuracy DT using ' + feature_name + ": " + str(accuracy * 100))
        print('Model loaded and used for prediction.')
    else:
        print('Model file does not exist.')


def random_forest(x_train, y_train, x_test, y_test, feature_name):
    filename = 'rf_model' + feature_name + '.pkl'
    if not os.path.exists(filename):
        # Define a Random Forest classifier with 100 trees
        rfc = RandomForestClassifier(n_estimators=100, random_state=1)

        # Train the classifier on the training data

        rfc.fit(x_train, y_train)
        with open(filename, 'wb') as file:
            pickle.dump(rfc, file)
        print('Model saved successfully.')
    else:
        print('Model file already exists.')

    # Load the model if the file exists
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            rf_model = pickle.load(file)
            # Make predictions on the testing data
        y_pred = rf_model.predict(x_test)

        # Evaluate the performance of the classifier
        accuracy = accuracy_score(y_test, y_pred)
        print('Accuracy random forest using ' + feature_name + ": " + str(accuracy * 100))

        print('Model loaded and used for prediction.')
    else:
        print('Model file does not exist.')


# def encode_nn(Y):
#     encoder = LabelEncoder()
#     encoder.fit(Y)
#     y_encoded = encoder.transform(Y)
#
#     # Convert the target variable to one-hot vectors
#     y_onehot = to_categorical(y_encoded)
#     return y_onehot


# def NN_model(X, Y):
#     Y_encoded = encode_nn(Y)
#
#     x_train, x_test, y_train, y_test = train_test_split(X, Y_encoded, test_size=0.20, shuffle=True, random_state=1)
#
#     # Define a neural network model
#     model = Sequential()
#     model.add(Dense(16, input_dim=x_train.shape[1], activation='relu'))
#     model.add(Dense(8, activation='relu'))
#     model.add(Dense(Y.shape[1], activation='softmax'))
#
#     # Compile the model
#     model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#
#     # Train the model on the training data
#     model.fit(x_train, y_train, epochs=50, batch_size=32)
#
#     # Evaluate the model on the testing data
#     loss, accuracy = model.evaluate(x_test, y_test)
#     print('Test loss:', loss)
#     print('Test accuracy:', accuracy)
