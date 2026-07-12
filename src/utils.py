import pandas as pd


def load_dataset(file_path):
    return pd.read_csv(file_path)


def display_dataset_info(df):
    print("Dataset Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print(df.head())


def preprocess_data(df):
    return df
