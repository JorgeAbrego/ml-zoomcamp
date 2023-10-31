#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

# Load the data
data = pd.read_csv('./data/train_dataset.csv')

# Fixing columns names
data.columns = (data
                .columns.str.lower()
                .str.replace("(","_")
                .str.replace(")","")
                .str.replace(" ","_")
                )

df_full_train, df_test = train_test_split(data, test_size=0.2, random_state=42)

best_params = {'n_estimators': 100, 
               'min_samples_split': 8, 
               'min_samples_leaf': 8, 
               'max_features': 'sqrt', 
               'max_depth': 20, 
               'bootstrap': False
               }
n_splits = 5

# Train Function 
def train(X_train, y_train, params):
    model = RandomForestClassifier(**params, random_state=42)
    model.fit(X_train, y_train)
    return  model

# Predict Function
def predict(X, model):
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred

# validation
kfold = KFold(n_splits=n_splits, shuffle=True, random_state=42)

scores = []

fold = 0

for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.smoking.values
    y_val = df_val.smoking.values

    del df_train['smoking']
    del df_val['smoking']

    model = train(df_train, y_train, best_params)
    y_pred = predict(df_val, model)

    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)

    print(f'auc on fold {fold} is {auc}')
    fold = fold + 1

print('validation results:')
print('%.3f +- %.3f' % (np.mean(scores), np.std(scores)))

# training the final model

print('training the final model')

model = train(df_full_train.drop(columns=['smoking']), df_full_train.smoking.values, best_params)
y_pred = predict(df_test.drop(columns=['smoking']), model)

y_test = df_test.smoking.values
auc = roc_auc_score(y_test, y_pred)

print(f'auc={auc}')

# Save the model
output_file = f"model_rf.bin"
with open(output_file, 'wb') as f_out:
    pickle.dump((model), f_out)

print(f'the model is saved to {output_file}')