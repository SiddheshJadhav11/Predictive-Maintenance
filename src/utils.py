



import pandas as pd





def load_dataset(file_path):

    """

    Load CSV dataset.



    Parameters

    ----------

    file_path : str

        Path of CSV file.



    Returns

    -------

    pandas.DataFrame

    """

    return pd.read_csv(file_path)





def display_dataset_info(df):

    """

    Display dataset information.

    """

    print("\nDataset Shape:", df.shape)

    print("\nColumns:")

    print(df.columns.tolist())

    print("\nFirst Five Records:")

    print(df.head())





def preprocess_data(df):

    """

    Placeholder for future preprocessing.



    Parameters

    ----------

    df : pandas.DataFrame



    Returns

    -------

    pandas.DataFrame

    """

    return df
