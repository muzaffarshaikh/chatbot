from preprocess import preprocess, get_tokenized_sentences
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer();

user_input = input()
temp_str = get_tokenized_sentences(user_input)

print(temp_str)

tfidf = vectorizer.fit_transform(temp_str)

print(tfidf)
print(tfidf.shape)


