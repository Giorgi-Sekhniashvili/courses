import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

import xgboost
from sklearn.utils import shuffle
from sklearn.metrics import accuracy_score

positive_train = pd.read_excel('C:/Users/gsekhniashvili/Desktop/ისი_MA/MA_1/ხელოვნური ნეირონული ქსელები/data/anti_peptids.xlsx',
                               sheet_name='Positive_Training_set')
negative_train = pd.read_excel('C:/Users/gsekhniashvili/Desktop/ისი_MA/MA_1/ხელოვნური ნეირონული ქსელები/data/anti_peptids.xlsx',
                               sheet_name='Negative_Training_set')

positive_test = pd.read_excel('C:/Users/gsekhniashvili/Desktop/ისი_MA/MA_1/ხელოვნური ნეირონული ქსელები/data/anti_peptids.xlsx',
                              sheet_name='Positive_Test_set')
negative_test = pd.read_excel('C:/Users/gsekhniashvili/Desktop/ისი_MA/MA_1/ხელოვნური ნეირონული ქსელები/data/anti_peptids.xlsx',
                              sheet_name='Negative_Test_set')


positive_train['label'] = np.ones((positive_train.shape[0]))
positive_test['label'] = np.ones((positive_test.shape[0]))

negative_train['label'] = np.zeros((negative_train.shape[0]))
negative_test['label'] = np.zeros((negative_test.shape[0]))

train_dataset = pd.concat([positive_train, negative_train])
train_dataset = train_dataset.astype(np.float32)
train_dataset = shuffle(train_dataset, random_state=0)
print('refreshed, not good!')


if __name__ == '__main__':
    st.header('Imported Dataset:')
    st.dataframe(data=train_dataset)

    st.write('***')
    st.header('XGBoost Parameters:')
    st.subheader('General Parameters:')

    booster = st.sidebar.selectbox('Choose your booster', options=['gbtree', 'dart', 'gblinear'])

    if booster == 'gbtree':
        eta = st.sidebar.number_input(label='eta (learning_rate)', min_value=0.0, max_value=1.)

        gamma = st.sidebar.slider(label='gamma (min_split_loss):', min_value=0, max_value=101)
        max_depth = st.sidebar.slider(label='max_depth', min_value=1, max_value=15)
        lambda_ = st.sidebar.s

    elif booster == 'gblinear':
        pass
    else:
        pass





