import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

print("Loading data...")
df = pd.read_csv('../movies_metadata.csv')
df = df.drop_duplicates().reset_index(drop=True)
df = df[['title', 'overview', 'genres', 'tagline', 'vote_average', 'popularity']]
df = df.dropna(subset=['title'])
df['overview'] = df['overview'].fillna('')

print("Processing genres...")
import ast
# Some rows might have malformed genres or floats (NaN). We should handle it safely.
def parse_genres(x):
    if pd.isna(x):
        return ""
    try:
        return " ".join([i['name'] for i in ast.literal_eval(x)])
    except:
        return ""

df['genres'] = df['genres'].apply(parse_genres)

df['tagline'] = df['tagline'].fillna('')
df['tags'] = df['overview'] + ' ' + df['genres'] + ' ' + df['tagline']

print("Downloading NLTK data...")
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

print("Preprocessing text...")
def preprocess_text(text):
  text = str(text).lower() # convert to lowercase
  text = re.sub(r'[^\w\s]', '', text) # Remove punctuations using regex
  words = text.split() # Split each words
  words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words] # remove stop words and tokenise each word
  return " ".join(words)

df['tags'] = df['tags'].apply(preprocess_text)

df = df.reset_index(drop=True)

print("Vectorizing...")
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features=50000, ngram_range=(1, 2), stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['tags'])

indices = pd.Series(df.index, index=df['title']).drop_duplicates()

print("Saving pickles...")
import pickle
pickle.dump(tfidf_matrix, open('tfidf_matrix.pkl', 'wb'))
pickle.dump(indices, open('indices.pkl', 'wb'))
df[['title', 'genres', 'popularity']].to_pickle('df.pkl')
pickle.dump(tfidf, open('tfidf.pkl', 'wb'))

print("Done!")
