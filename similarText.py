# -*- coding: utf-8 -*-

import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

#nltk.download('punkt') # if necessary...


#stemmer = nltk.stem.snowball.SnowballStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

#def stem_tokens(tokens):
#    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
#def normalize(text):
#    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(stop_words='english')
print(vectorizer)
def cosine_sim(text1, text2):
    if text1.strip():
        tfidf = vectorizer.fit([text1, text2])
        print(tfi)
        tfidf = vectorizer.transform([text1, text2])
#        print(type(tfidf))
        return ((tfidf * tfidf.T).A)[0,1]
    else:
        return 0.0

print (cosine_sim('a little bird', 'a little bird'))
print (cosine_sim('a little bird', 'a little bird chirps'))
print (cosine_sim('a little bird', 'a big dog barks'))
#print (cosine_sim('what to do', ' '))
print (cosine_sim('', 'a little bird chirps'))
print (cosine_sim(' ', ' '))
#print (cosine_sim(' ', 'what to do'))

import string
s = "string. With. Punctuation?" # Sample string 
out = s.translate(remove_punctuation_map)
print(out)