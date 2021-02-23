from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from chatbot.text_lemmatizer import LemNormalize


def response(user_response, sentTokens):
    bot_response = ''
    sentTokens.append(user_response)

    TfidfVectorObject = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVectorObject.fit_transform(sentTokens)
    values = cosine_similarity(tfidf[-1], tfidf)
    idx = values.argsort()[0][-2]
    flat = values.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        bot_response = bot_response + "Can you rephrase it? I'm having difficulty understanding you."
        return bot_response
    else:
        bot_response = bot_response + sentTokens[idx]
        return bot_response
