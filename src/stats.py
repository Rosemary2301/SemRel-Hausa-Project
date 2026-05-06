import pandas as pd

def dataset_stats(file_path):
    df = pd.read_csv(file_path)

    print(f"\nDataset: {file_path}")
    print("Rows:", len(df))
    print("Columns:", df.columns.tolist())

    print("\nMissing values:")
    print(df.isnull().sum())

# Check datasets
dataset_stats("data/hausa_train.csv")
dataset_stats("data/hausa_test.csv")
dataset_stats("data/english_train.csv")