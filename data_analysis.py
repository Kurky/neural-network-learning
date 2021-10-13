import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#CREATING BALANCED TRAIN DATASET
def create_balanced_dataset(name):
    df = pd.read_csv('../../../Dataset/2020/' + name + '.csv')
    malignant = df[df.target == 1]
    benign = df[df.target == 0]
    malignant_count = len(malignant)
    # this gets random benign rows
    benign = benign.sample(n=malignant_count)
    # new balanced data
    new_data = pd.concat([benign, malignant])
    new_data.to_csv('../../../Dataset/2020/balanced_' + name + '.csv')


if __name__ == '__main__':
    #creating balanced dataset
    #create_balanced_dataset('train')
    train_df = pd.read_csv('../../../Dataset/2020/balanced_train.csv')
    malignant = train_df[train_df.target == 1]
    benign = train_df[train_df.target == 0]



