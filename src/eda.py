import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')

def clean_text(text):
  text = text.lower()
  # Remove Punctuation
  text = re.sub(r'[^a-zA-Z\s]', '', text)
  # Remove whitespace
  text = re.sub(r'\s+', ' ', text).strip()
  return text
  

def remove_stopwords(x):
  stop_words = set(stopwords.words('english'))
  words = word_tokenize(x)
  filtered = [ w for w in words if w.lower() not in stop_words]
  return ' '.join(filtered)


def lemmatize_reviews(x):
  lemmatizer = WordNetLemmatizer()
  words = word_tokenize(x)
  lemmatized_review_words = [lemmatizer.lemmatize(word) for word in words]
  return ' '.join(lemmatized_review_words)
  
  
  

if __name__ == '__main__':
  pass