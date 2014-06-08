# -*- coding: cp936 -*-
__author__ = 'alex king'
from textblob import TextBlob
from textblob import Word
import getdata
import string

WORDTYPE_MEANINGFULL = {'JJ': 0, 'JJR': 0, 'JJS': 0, 'NN': 0, 'NNS': 0, 'NNP': 0, 'NNPS': 0}


def getword(word):
    w = Word(word[0])
    result = word[0]
    if word[1] == 'JJR' or word[1] == 'JJS':
        result = w.lemmatize('a')
    elif word[1] == 'NNS' or word[1] == 'NNP' or word[1] == 'NNPS':
        result = w.lemmatize('n')
    return result


def get_onesentense_po(sentence, star):
    words = sentence.tags
    polarity = sentence.sentiment.polarity
    if polarity > 0:
        star = (5 - star) * polarity + star
    else:
        star = -star * polarity
    keyword = {}
    for word in words:
        if WORDTYPE_MEANINGFULL.has_key(word[1]) and len(word[0]) > 1:
            w = getword(word)
            if keyword.has_key(w):
                if star > 3:
                    keyword[w][1] += 1
                elif star < 3:
                    keyword[w][2] += 1
            else:
                if star > 3:
                    keyword[w] = [word[1], 1, 0]
                elif star < 3:
                    keyword[w] = [word[1], 0, 1]
    return keyword


def getstar(star):
    star = star.split(' ')[0]
    result = 3
    try:
        result = string.atof(star)
    except:
        print(star)
    return result


def asin_keywordAnalyse(asin):
    data = getdata.get_asin_data(asin)
    keywords = {}
    for review in data['review']:
        #sentenses=review['content']
        star = getstar(review['star'])
        sentenses = TextBlob(review['content'])
        sentenselist = sentenses.sentences
        for sentense in sentenselist:
            keyword = get_onesentense_po(sentense, star)
            for (k, v) in keyword.items():
                if keywords.has_key(k):
                    keywords[k][1] += v[1]
                    keywords[k][2] += v[2]
                else:
                    keywords[k] = [v[0], v[1], v[2]]
    kws = []
    for (k, v) in keywords.items():
        kws.append((k, v[1], v[2]))
    kws.sort(key=lambda x: x[1] + x[2])
    kws.reverse()
    if len(kws) >= 8 :
        return kws[0:8]
    return kws



if __name__ == '__main__':
    kws = asin_keywordAnalyse('B003FGWY1O')
    for k in kws:
        print k[0], '  ', k[1], '  ', k[2], ' ', (0.0 + k[1]) / (k[2] + k[1])
    pass