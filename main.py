import pandas as pd
from datetime import datetime
import tensorflow as tf
from keras import models, layers
import nltk

def build_dense_network():
    network = models.Sequential()
    network.add(layers.Dense())
    network.add(layers.Dense())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    raw_df = pd.read_csv('training.1600000.processed.noemoticon.csv', encoding='latin-1', header=None,
                         names=['polarity', 'id', 'date', 'query', 'user', 'tweet'])
    y = raw_df['polarity']
    raw_df.drop(columns=['id', 'query', 'polarity'], inplace=True)

    processed_date_series = raw_df['date'].apply(pd.to_datetime)


    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
