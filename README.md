# Investigating Cross-Lingual Relatedness and Data Augmentation for Hausa
This project invesigated the Cross-Lingual relatedness and Data Augementation for the low-level language Hausa. 
It trains a variety of models using the SemRel database and shows the Spearman correlation, which is a metric used to measure relatedness

## Setup and Installation
Run the pip install -r requirements.txt to install specific versions needed

## Repository Structure
```
SemRel-Hausa-Project/
├── src/
│   ├── load_data.py
│   ├── preprocess.py
│   ├── stats.py
│   ├── NLP_Project_Week2_3.ipynb
│   ├── CrossLingual.ipynb
│   └── Week5.ipynb
├── data/
│   ├── english_train.csv
│   ├── hausa_test.csv
│   ├── hausa_train_clean.csv
│   └── hausa_train.csv
├── requirements.txt
└── README.md
```

## Order to run Notebooks

1. Load the data by running  load_data.py
2. Preprocess the data using preprocess.py 
3. Get statistics to verify data is correctly preporccessed by running stats.py
4. NLP_Project_Week2_3.ipynb
5. CrossLingual.ipynb
6. Week5.ipynb

## Data and Model Files
The following link is a link to the models that have been trained and saved to Google Drive
