from nltk.util import ngrams
from nltk.probability import FreqDist

s = '<s> I am Sam </s> <s> Sam I am </s> <s> I do not like green eggs and ham </s>'


def unigramcalc(sentence):
    formatedSentence = sentence.split()
    unigrams = ngrams(formatedSentence, 1)
    unifdist = FreqDist(unigrams)
    
    for unigram in unifdist:
        prob = unifdist[unigram] / len(formatedSentence)
        print(f"P({unigram[0]}) = {prob}")
        
        
print(unigramcalc(s))

def bigramcalc(sentence):
    formatedSentence2 = sentence.split()
    formatedSentence = sentence.split()
    bigrams = ngrams(formatedSentence, 2)
    bifdist = FreqDist(bigrams)
    unigrams = ngrams(formatedSentence2, 1)
    unifdist = FreqDist(unigrams)
    
    for grams in bifdist:
        word = grams[0]
        prob = bifdist[grams] / unifdist[(word,)]
        print(f"{grams[1]}|{word} = {prob}")

print(bigramcalc(s))

def trigramcalc(sentence):
    formatedSentence1 = sentence.split()
    formatedSentence2 = sentence.split()
    trigrams = ngrams(formatedSentence1, 3)
    trifdist = FreqDist(trigrams)
    bigrams = ngrams(formatedSentence2, 2)
    bifdist = FreqDist(bigrams)
    for grams in trifdist:
        word = grams[:2]
        prob = trifdist[grams] / bifdist[word]
        print(f"P({grams[2]}|{word[0]},{word[1]}) = {prob}")
        
print(trigramcalc(s))