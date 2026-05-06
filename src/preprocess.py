import re
import pandas as pd

def clean_text(text):
    if not isinstance(text, str):
        return ""

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text

# Load Hausa train dataset
df = pd.read_csv("data/hausa_train.csv")

# Clean sentences
df["sentence1"] = df["sentence1"].apply(clean_text)
df["sentence2"] = df["sentence2"].apply(clean_text)

# Save cleaned version
df.to_csv("data/hausa_train_clean.csv", index=False)

print("Preprocessing complete!")