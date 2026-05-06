from datasets import load_dataset
import pandas as pd

print("Starting download...")

# Load Hausa dataset
hausa = load_dataset("SemRel/SemRel2024", "hau")

# Load English dataset
english = load_dataset("SemRel/SemRel2024", "eng")

print("Datasets loaded!")

# Convert to pandas
hausa_train = hausa["train"].to_pandas()
hausa_test = hausa["test"].to_pandas()

english_train = english["train"].to_pandas()

# Save locally
hausa_train.to_csv("data/hausa_train.csv", index=False)
hausa_test.to_csv("data/hausa_test.csv", index=False)

english_train.to_csv("data/english_train.csv", index=False)

print("Data saved successfully!")