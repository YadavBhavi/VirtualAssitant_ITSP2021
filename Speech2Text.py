import speech_recognition as sr
import pyaudio
r = sr.Recognizer()                  # obtain audio from the microphone
with sr.Microphone() as source:
    print("What would you like me to do?")
    audio = r.listen(source)
    command = r.recognize_google(audio , language='english')
    text = print(command)
# Natural Language Processing part
import nltk
from nltk.tokenize import sent_tokenize , word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
text = command
words = nltk.word_tokenize(text)
tagged = nltk.pos_tag(words)

def ProperNounExtractor(text):
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if (tag == 'NNP' or 'VB') and (word != "please"):       # If the word is a proper noun or verb
                print(word)

# Calling the ProperNounExtractor function to extract all the proper nouns and verb from the given text.
ProperNounExtractor(text)





