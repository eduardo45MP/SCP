import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from tqdm import tqdm  # Importing tqdm for progress bar

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Tokenization
    tokens = nltk.word_tokenize(text)
    
    # Removing stop words
    filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
    
    # Checking for empty text
    if not filtered_tokens:
        return None
    
    # Stemming
    stemmer = SnowballStemmer("english")
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    
    return stemmed_tokens


# Load the CSV file
df = pd.read_csv('./data/combined_data.csv')

# Apply preprocessing to each dataframe row with progress bar
preprocessed_texts = []
for text in tqdm(df['text'], desc="Preprocessing"):
    preprocessed_texts.append(preprocess_text(text))

# Add preprocessed texts to the dataframe
df['preprocessed_text'] = preprocessed_texts

# Save the dataframe to a new CSV file
df.to_csv('./data/preprocessed_combined_data.csv', index=False)