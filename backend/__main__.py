from file_reader import data
from text_preprocessing import convert_number_to_word, remove_punctuation, get_tokenized_text, get_stemmed_words

# plain text in lower case
text = data.lower()

# plain text without punctuation
tempTextPunct = remove_punctuation(text)

# plain text with number conversion
tempTextNum = convert_number_to_word(tempTextPunct)

# plain text with whitespace removal
tempWhitespaceRemoved = " ".join(tempTextNum.split())

# word tokens extracted
word_tokens = get_tokenized_text(tempWhitespaceRemoved)

# stemmed words
# not quite sure if stemming will affect the accuracy
# some words might lose meaning.
# did not do lemmatization as of yet
stemmed = get_stemmed_words(word_tokens)
print(stemmed)

# should speech tagging be done?
