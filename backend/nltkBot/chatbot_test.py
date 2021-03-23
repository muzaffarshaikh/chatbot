import warnings

warnings.filterwarnings("ignore")

import random

from text_extract_pdf import getSentTokens
from file_read_txt import sent_tokens
from cbot_response import response

# getting the filepath
# check the data directory for 'sample corpus.pdf'
filename = 'data/sample_corpus.pdf'

# getSentTokens() from text_extract_pdf.py extracts sentence tokens from the file provided.
# issues with files downloaded from internet.
sentTokens = sent_tokens

print(sentTokens)

GREETING_INPUTS = ("hello", "hi", "greetings", "hey", "namaste", "whats up", "good morning", "good afternoon")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me", "greetings are boring"]


# greeting user from the given string constants.
def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


flag = True

while flag:
    user_response = input()
    bot_response = ""
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response != 'thanks' and user_response != 'thank you':
            if user_response != 'okay':
                if greet(user_response) is not None:
                    bot_response = bot_response + ("Chandler: " + greet(user_response))
                    print(bot_response)
                else:
                    print("Chandler: ", end="")
                    bot_response = (response(user_response, sentTokens))
                    print(bot_response)
                    sentTokens.remove(user_response)
            else:
                bot_response = bot_response + "Chandler: I'll Wait."
                print(bot_response)
        else:
            bot_response = bot_response + "Chandler: You are welcome.. Anything else i can help you with?"
            print(bot_response)
    else:
        flag = False
        bot_response = bot_response + "Chandler: Bye! take care.."
        print(bot_response)
