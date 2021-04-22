from file_read_txt import data

from preprocess import convert_number_to_word, punctuation_removal, get_tokenized_words, get_tokenized_sentences, get_lemmatized_words

corpus = data.lower()
corpus_sent = data.lower()

punct_removed_text = punctuation_removal(corpus)
number_converted_text = convert_number_to_word(punct_removed_text)
whitespace_removed_text = " ".join(number_converted_text.split())
lem = get_lemmatized_words(whitespace_removed_text)

# print("Text : " + whitespace_removed_text)
# print(lem)
# print(pos_tag(whitespace_removed_text))

word_tokens = get_tokenized_words(lem)
sent_tokens = get_tokenized_sentences(corpus)  # without preprocess

print(sent_tokens)
print(word_tokens)

# sentences = []
# for entry in sent_tokens:
#     punct_remove = punctuation_removal(entry)
#     number_converted = convert_number_to_word(punct_remove)
#     whitespace_removed = " ".join(number_converted_text.split())
#     lemmatized = get_lemmatized_words(whitespace_removed)
#     sentences.append(lemmatized)






