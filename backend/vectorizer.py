from sklearn.feature_extraction.text import TfidfVectorizer
from tokenizer import sent_tokens

# print(sent_tokens.__len__())

vectorizer = TfidfVectorizer();
tfidf = vectorizer.fit_transform(sent_tokens)

# print(vectorizer.get_feature_names())
# print(vectorizer.get_feature_names().__len__())

# print(tfidf.toarray())

arr = tfidf.toarray()

# for entry in arr:
#     print(entry)
#
print("\nThe shape of the TF-IDF matrix is: ", tfidf.shape)
print(tfidf)
print(arr)


