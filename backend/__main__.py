from file_reader import data
from number_converter import convert_number
from punct_remover import remove_punctuation
from tokenizer import get_tokenize_text
from stemmer import get_stemmed_words

# plain text in lower case
text = data.lower()
print(text)

# plain text without punctuation
tempTextPunct = remove_punctuation(text)
print(tempTextPunct)

# plain text with number conversion
tempTextNum = convert_number(tempTextPunct)
print(tempTextNum)

# plain text with whitespace removal
tempWhitespaceRemoved = " ".join(tempTextNum.split())
print(tempWhitespaceRemoved)

# word tokens extracted
word_tokens = get_tokenize_text(tempWhitespaceRemoved)
print(word_tokens)

# stemmed words
# not quite sure if stemming will affect the accuracy
# some words might lose meaning.
# did not do lemmatization as of yet
stemmed = get_stemmed_words(word_tokens)
print(stemmed)

#should speech tagging be done?