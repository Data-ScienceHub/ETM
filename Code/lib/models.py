import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

from sklearn import decomposition
from sklearn.cluster import KMeans
from sklearn.metrics import (
    RocCurveDisplay, 
    roc_auc_score, 
    roc_curve,
    confusion_matrix,
    ConfusionMatrixDisplay
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import tensorflow as tf

class EtmKMeans:
    '''
    Python class for generating the clustering labels for the Model
    '''

    def __init__(self, data):
        '''
        Purpose: creates a new k-Means clustering model

        INPUT:
        data - pandas dataframe of data to use
        '''
        self.data = data
    
    def generate_labels(self, clusters, max_iter, random_state):
        '''
        Purpose: generates a new K-mean model

        INPUTS:
        clusters - int number of desired clusters
        max_iter - int max iteration used for the k-Means model
        random_state - int random state for replicability

        OUTPUT:
        labels - list of clustering labels
        '''

        # define standard scaler
        scaler = StandardScaler()
        
        # transform data
        data = scaler.fit_transform(self.data)
        self.scaled_data = data

        # perform clustering to get training labels
        k = 2
        KM = KMeans(
            n_clusters = clusters, 
            max_iter = max_iter, 
            random_state = random_state
        )
        KM.fit(data)
        self.model = KM
        self.labels = KM.labels_

        return self.labels
    
    def visualize_features(self):
        '''
        Purpose: visualize the difference in features for each class
        '''
        data = self.scaled_data
        labels = self.labels
        features = self.data.columns

        # loop through each feature
        for i in range(data.shape[1]):
            # plot the class conditional density
            pd.DataFrame(data[labels == 1,i]).plot.kde(title = f'{features[i]} for 1')
            pd.DataFrame(data[labels == 0,i]).plot.kde(title = f'{features[i]} for 0')
            # print the class conditional mean
            print(data[labels == 1,i].mean())
            print(data[labels == 0,i].mean())
            print()
    
    def generate_pca(self, components):
        '''
        Purpose: performs principal component analysis on the data

        INPUT:
        components - int number of desired components

        OUTPUT:
        pca_components - array of the PCA components
        '''

        self.pca = decomposition.PCA(n_components = components)
        self.pca_points = self.pca.fit_transform(self.scaled_data)

        return self.pca.components_

    def visualize_3d_pca(self, colors, alpha):
        '''
        Purpose: plot a graph of the PCA in a 3D space

        INPUT:
        colors - list of string for the desired colors of the graph
        alpha - float value between 0 and 1 to determine opacity of plot
        '''

        points = self.pca_points

        fig = plt.figure(figsize = (12, 12))
        ax = fig.add_subplot(projection = '3d')

        # 3d projection
        ax.scatter(
            points[:, 0], 
            points[:, 1], 
            points[:, 2], 
            c = self.labels, 
            cmap = matplotlib.colors.ListedColormap(colors), 
            alpha = alpha
        )

        plt.show()
    
    def visualize_2d_pca(self, colors, alpha):
        '''
        Purpose: plot a graph of the PCA in a 2D space

        INPUT:
        colors - list of string for the desired colors of the graph
        alpha - float value between 0 and 1 to determine opacity of plot
        '''

        points = self.pca_points

        # 2d projection of the plot
        plt.scatter(
            points[:, 0], 
            points[:, 1], 
            c = self.labels, 
            cmap = matplotlib.colors.ListedColormap(colors), 
            alpha = alpha
        )
        
        plt.show()

class EtmMLP:
    '''
    Python class for creating the MLP classification model
    '''

    def __init__(self, data, labels):
        '''
        Purpose: creates a new MLP classification model

        INPUT:
        data - pandas dataframe of data to use
        labels - numpy array of labels
        '''

        self.data = data
        self.labels = labels

    def generate_model(self, test_size, random_state):
        '''
        Purpose: creates the MLP model

        INPUT:
        test_size - float value between 0 and 1 to determine the size of the test dataset
        random_state - int value for reproducibility

        OUTPUT:
        model - Tensorflow MLP model
        '''

        # define standard scaler
        scaler = StandardScaler()
        
        # transform data
        data = scaler.fit_transform(self.data)
        self.scaled_data = data

        self.X_train, self.X_valid, self.y_train, self.y_valid = train_test_split(
            data, 
            self.labels, 
            test_size = test_size, 
            random_state = random_state
        )

        # define the weight initializer
        init = tf.keras.initializers.GlorotNormal()

        # define the model architecture
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(10, input_dim = data.shape[1], activation = 'relu', kernel_initializer = init),
            tf.keras.layers.Dense(10, activation = 'relu', kernel_initializer = init),
            tf.keras.layers.Dense(1, activation = 'sigmoid', kernel_initializer = init)
        ])

        # compile the model using the appropriate loss function and optimizer
        model.compile(
            loss = 'binary_crossentropy', 
            optimizer = 'adam', 
            metrics = ['accuracy']
        )

        self.model = model

        return self.model
    
    def train_model(self, num_epochs = 25):
        '''
        Purpose: runs the training loop for the MLP model

        INPUT:
        num_epochs - int number of epochs used for training
        '''

        self.history = self.model.fit(
            self.X_train, 
            self.y_train,
            verbose = 0, 
            epochs = num_epochs, 
            batch_size = 32,
            validation_data = (self.X_valid, self.y_valid),
            callbacks = [
                tf.keras.callbacks.EarlyStopping(
                    monitor = 'loss', 
                    patience = 10, 
                    verbose = 0, 
                    restore_best_weights = True
                )
            ]
        )

        _, train_accuracy = self.model.evaluate(self.X_train, self.y_train, verbose = 0)
        _, test_accuracy = self.model.evaluate(self.X_valid, self.y_valid, verbose = 0)
        print('Train: %.2f, Test: %.2f' % (train_accuracy, test_accuracy))
    
    def plot_training_curve(self):
        '''
        Purpose: plot the training curve of the training loop
        '''

        # plot the training performance metrics
        plt.plot(self.history.history['accuracy'], label = 'train_accuracy')
        plt.plot(self.history.history['val_accuracy'], label = 'val_accuracy')
        plt.legend()
    
    def predict_test_set(self):
        '''
        Purpose: gets the predicted values for the test set

        OUTPUT:
        val_predicts - array of predicted values
        '''

        self.val_predicts = self.model.predict(self.X_valid)
        return self.val_predicts

    def get_auroc(self):
        '''
        Purpose: plot the ROC curve and get the ROC AUC score

        OUTPUT:
        auroc - float AUROC score
        '''

        # plot the ROC curve
        RocCurveDisplay.from_predictions(self.y_valid, self.val_predicts)

        # compute AUROC
        auroc = roc_auc_score(self.y_valid, self.val_predicts)

        return auroc
    
    def find_optimal_roc_cutoff(self):
        '''
        Purpose: computes the optimal cutoff threshold for the ROC

        OUTPUT:
        cutoff_threshold - float cutoff threshold
        '''

        fpr, tpr, threshold = roc_curve(self.y_valid, self.val_predicts)
        i = np.arange(len(tpr)) 
        roc = pd.DataFrame(
            {
                'tf' : pd.Series(tpr - (1 - fpr), index = i), 
                'threshold' : pd.Series(threshold, index = i)
            }
        )
        roc_t = roc.iloc[(roc.tf - 0).abs().argsort()[:1]]

        self.cutoff_threshold = list(roc_t['threshold'])[0]

        return self.cutoff_threshold
    
    def produce_confusion_matrix(self):
        '''
        Purpose: creates a confusion matrix from the classification results

        OUTPUT:
        cm - matrix with the confusion matrix values
        '''

        # produce confusion matrix
        y_pred = 1 * (self.val_predicts >= self.cutoff_threshold)
        cm = confusion_matrix(self.y_valid, y_pred)
        disp = ConfusionMatrixDisplay(cm)
        disp.plot()

        print('True Postive Rate:', cm[1][1] / (cm[1][1] + cm[1][0]))
        print('True Negative Rate:', cm[0][0] / (cm[0][0] + cm[0][1]))

        print('False Postive Rate:', cm[0][1] / (cm[0][0] + cm[0][1]))
        print('False Negative Rate:', cm[1][0] / (cm[1][1] + cm[1][0]))

        return cm