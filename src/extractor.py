import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from tqdm import tqdm

# Load the preprocessed CSV file
input_file = './data/preprocessed_combined_data.csv'
output_file = './data/extracted.csv'

# Load the dataframe
df = pd.read_csv(input_file)

# Treat NaN values by replacing them with an empty string
df['preprocessed_text'].fillna('', inplace=True)

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit the vectorizer to the data
tfidf_vectorizer.fit(df['preprocessed_text'])

# Initialize the progress bar
tqdm.pandas()

# Function to extract features and add a progress bar
def extract_features(text):
    return tfidf_vectorizer.transform([text])

# Extract features for all texts
df['extracted_features'] = df['preprocessed_text'].progress_apply(extract_features)

# Save the dataframe with extracted features to a new CSV file
df.to_csv(output_file, index=False)
