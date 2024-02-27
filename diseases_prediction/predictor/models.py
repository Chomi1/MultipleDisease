
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
import numpy as np

class SVM_classifier():


  # initiating the hyperparameters
  def __init__(self, learning_rate, no_of_iterations, lambda_parameter):

    self.learning_rate = learning_rate
    self.no_of_iterations = no_of_iterations
    self.lambda_parameter = lambda_parameter



  # fitting the dataset to SVM Classifier
  def fit(self, X, Y):

    # m  --> number of Data points --> number of rows
    # n  --> number of input features --> number of columns
    self.m, self.n = X.shape

    # initiating the weight value and bias value

    self.w = np.zeros(self.n)

    self.b = 0

    self.X = X

    self.Y = Y

    # implementing Gradient Descent algorithm for Optimization

    for i in range(self.no_of_iterations):
      self.update_weights()



  # function for updating the weight and bias value
  def update_weights(self):

    # label encoding
    y_label = np.where(self.Y <= 0, -1, 1)



    # gradients ( dw, db)
    for index, x_i in enumerate(self.X):

      condition = y_label[index] * (np.dot(x_i, self.w) - self.b) >= 1

      if (condition == True):

        dw = 2 * self.lambda_parameter * self.w
        db = 0

      else:

        dw = 2 * self.lambda_parameter * self.w - np.dot(x_i, y_label[index])
        db = y_label[index]


      self.w = self.w - self.learning_rate * dw

      self.b = self.b - self.learning_rate * db



  # predict the label for a given input value
  def predict(self, X):

    output = np.dot(X, self.w) - self.b

    predicted_labels = np.sign(output)

    y_hat = np.where(predicted_labels <= -1, 0, 1)

    return y_hat



class Logistic_Regression():
    # declaring learning rate & number of iterations (Hyperparameters)
    def __init__(self, learning_rate, no_of_iterations):
        self.learning_rate = learning_rate
        self.no_of_iterations = no_of_iterations
    
    # fit function to train the model with dataset
    def fit(self, X, Y):
        # number of data points in the dataset (number of rows) --> m
        # number of input features in the dataset (number of columns) --> n
        self.m, self.n = X.shape

        # initiating weight & bias value
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        # implementing Gradient Descent for Optimization
        for i in range(self.no_of_iterations):
            self.update_weights()

    def update_weights(self):
        # Y_hat formula (sigmoid function)
        Y_hat = 1 / (1 + np.exp( - (self.X.dot(self.w) + self.b ) ))

        # derivatives
        dw = (1/self.m)*np.dot(self.X.T, (Y_hat - self.Y))
        db = (1/self.m)*np.sum(Y_hat - self.Y)

        # updating the weights & bias using gradient descent
        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db

    # Sigmoid Equation & Decision Boundary
    def predict(self, X):
        if not isinstance(X, np.ndarray):
            X = np.array(X)  # Convert list to numpy array if it's a list
        Y_pred = 1 / (1 + np.exp( - (X.dot(self.w) + self.b ) ))
        Y_pred = np.where( Y_pred > 0.5, 1, 0)
        return Y_pred
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for user profile if needed
    age = models.IntegerField(default=0)  

    def __str__(self):
        return self.user.username
    


class HeartDiseasePredictionData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    age = models.IntegerField(default=0) 
    sex = models.IntegerField(default=0)
    cp = models.IntegerField(default=0)
    trestbps = models.FloatField(default=0)
    chol = models.FloatField(default=0)
    fbs = models.IntegerField(default=0)
    restecg = models.IntegerField(default=0)
    thalach = models.FloatField(default=0)
    exang = models.IntegerField(default=0)
    oldpeak = models.FloatField(default=0)
    slope = models.IntegerField(default=0)
    ca = models.IntegerField(default=0)
    thal = models.IntegerField(default=0)
    prediction = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"

class DiabetesPredictionData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pregnancies = models.IntegerField(default=0)
    glucose = models.IntegerField(default=0)
    blood_pressure = models.IntegerField(default=0)
    skin_thickness = models.IntegerField(default=0)
    insulin = models.IntegerField(default=0)
    bmi = models.FloatField(default=0)
    diabetes_pedigree_function = models.FloatField(default=0)
    age = models.IntegerField(default=0)
    prediction = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"
    
    # contact section
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    