import random

from text_extract_pdf import getSentTokens
from cbot_response import response

# getting the filepath
# check the data directory for 'sample corpus.pdf'
filename = 'C:/Users/Muzaffar/Desktop/sample_corpus.pdf'

# getSentTokens() from text_extract_pdf.py extracts sentence tokens from the file provided.
# issues with files downloaded from internet.
sentTokens = getSentTokens(filename)

GREETING_INPUTS = ("hello", "hi", "greetings", "hey", "namaste", "whats up", "good morning", "good afternoon")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me", "greetings are boring"]


# greeting user from the given string constants.
def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


flag = True
print("Chandler: Hello! I will answer your queries based on the document given to me.")
print("Chandler: If you want to exit, type Bye")

while flag:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response != 'thanks' and user_response != 'thank you':
            if greet(user_response) is not None:
                print("Chandler: " + greet(user_response))
            else:
                print("Chandler: ", end="")
                print(response(user_response, sentTokens))
                sentTokens.remove(user_response)
        else:
            flag = False
            print("Chandler: You are welcome..")
    else:
        flag = False
        print("Chandler: Bye! take care..")
