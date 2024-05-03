import nltk
nltk.download('punkt')
nltk.download('stopwords')
import nltk.corpus as corp
import numpy as numpy
import heapq 


with open("VectorHWtxt.txt", "r") as sentencefile:
    text = sentencefile.read()
    text = text.lower()

#text = "hey man what. I saw sunday two dogs at the park. lent where are you. more than one cat can fly. "
    
sentences = nltk.sent_tokenize(text)    
#print(sentences)
stopword = corp.stopwords.words('english')

token = [[word for word in nltk.word_tokenize(sentence) if word not in stopword]
         for sentence in sentences]
#print(token)

#
context = set(word for sentence in token for word in sentence)
#print(context)

#bag of words vector
bagofwordvects = []
bagofwordvects = numpy.array(bagofwordvects)
for sentence in token:
    bagofwordvects = numpy.zeros(len(context))
    # print (bagofwordvects)
    for word in sentence:
        if word in context:
            bagofwordvects[list(context).index(word)] += 1
        else:
            numpy.append(bagofwordvects, bagofwordvects)
    

#make lent vector
lentvect = numpy.zeros(len(context))
lentvect[list(context).index("lent")] = 1
#print(lentvect)

#using dot products find the relatedness
related = [numpy.dot(bagofwordvects, lentvect) for bagofwordvect in bagofwordvects]

#print(related)

toprelated = heapq.nlargest(3, bagofwordvects)
print(toprelated)
#print(bagofwordvects)

# sortedlist = numpy.argsort(related)[::-1]
# top3 = [list(context)[i] for i in sortedlist[0:4]]
# print(sortedlist)
# print(top3)

