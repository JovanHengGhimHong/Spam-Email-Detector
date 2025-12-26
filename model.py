#imports
import pandas as pd
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split

# import the dataset
data = pd.read_csv('dataset/email.csv')
X = data['Message'].values
y = data['Category'].values

X_train , X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocess the data (tokenization, padding, etc.)





