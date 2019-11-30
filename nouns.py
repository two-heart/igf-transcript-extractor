# Importing necessary library
import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus  # sample text for performing tokenization
from nltk.tokenize import word_tokenize  # Passing the string text into word tokenize for breaking the sentences
from nltk.probability import FreqDist
from textblob import TextBlob
from nltk.corpus import stopwords
import re


if __name__ == '__main__':
    # you can comment those out if you fulfill the requirements
    # nltk.download('stopwords')
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')

    with open('allTranscripts.txt', 'r') as file:
        text = file.read()

    # todo filter out r ^^new transcript...

    token = word_tokenize(text.lower())
    is_noun = lambda pos: pos[:2] == 'NN'
    nouns = [word for (word, pos) in nltk.pos_tag(token) if is_noun(pos)]

    a = set(stopwords.words('english'))
    stopwords = [x for x in nouns if x not in a]
    stopwords = list(filter('.'.__ne__, stopwords))
    stopwords = list(filter(','.__ne__, stopwords))
    stopwords = list(filter("'s".__ne__, stopwords))
    stopwords = list(filter('-'.__ne__, stopwords))
    stopwords = list(filter('--'.__ne__, stopwords))
    stopwords = list(filter('‑‑'.__ne__, stopwords))
    stopwords = list(filter('>'.__ne__, stopwords))
    stopwords = list(filter('('.__ne__, stopwords))
    stopwords = list(filter(')'.__ne__, stopwords))
    stopwords = list(filter('?'.__ne__, stopwords))
    stopwords = list(filter("n't".__ne__, stopwords))
    stopwords = list(filter("[".__ne__, stopwords))
    stopwords = list(filter("]".__ne__, stopwords))
    nouns = stopwords

    fdist = FreqDist(nouns)
    print(fdist.most_common(500))
