from file_reader import data
from text_preprocessing import convert_number_to_word, remove_punctuation, get_tokenized_words, \
     get_stemmed_words, get_tokenized_sentences, get_lemmatized_words

# Conversions: lower case, punctuation, number to word, whitespace removal, tokenization
text = data.lower()
punct_removed_text = remove_punctuation(text)
number_converted_text = convert_number_to_word(punct_removed_text)
whitespace_removed_text = " ".join(number_converted_text.split())

lem = get_lemmatized_words(whitespace_removed_text)
print("Text : " + whitespace_removed_text)
print("Lem Text : " + lem)

word_tokens = get_tokenized_words(whitespace_removed_text)
sent_tokens = get_tokenized_sentences(text)


# stemmed = get_stemmed_words(word_tokens)
# stemmed words
# not quite sure if stemming will affect the accuracy
# some words might lose meaning.
# did not do lemmatization as of yet
# stemmed = get_stemmed_words(word_tokens)
# print(stemmed)

# should speech tagging be done?
