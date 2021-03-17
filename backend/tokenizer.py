from file_reader import data
from nltk import pos_tag

from preprocess import convert_number_to_word, punctuation_removal, get_tokenized_words, \
    get_stemmed_words, get_tokenized_sentences, get_lemmatized_words

# Conversions: lower case, punctuation, number to word, extra whitespace removal, lemmatize, tokenization

corpus = data.lower()
corpus_sent = data.lower()


punct_removed_text = punctuation_removal(corpus)


number_converted_text = convert_number_to_word(punct_removed_text)
whitespace_removed_text = " ".join(number_converted_text.split())
lem = get_lemmatized_words(whitespace_removed_text)
# print("Text : " + whitespace_removed_text)
# print(lem)

word_tokens = get_tokenized_words(lem)
sent_tokens = get_tokenized_sentences(corpus)

# sentences = []

# for entry in sent_tokens:
#     punct_remove = punctuation_removal(entry)
#     number_converted = convert_number_to_word(punct_remove)
#     whitespace_removed = " ".join(number_converted_text.split())
#     lemmatized = get_lemmatized_words(whitespace_removed)
#     sentences.append(lemmatized)






