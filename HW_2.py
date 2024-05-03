import re
import random
import string
import nltk


# Problem 1.1
s1 = "The city of Rome is the 3rd largest of the European Union by population"
s2 = "The city of Madrid is the 2nd largest of the European Union by population"

#Rome has the 3rd largest population in the EU", "Madrid has the 2nd largest population in the EU
patterncity = r"The city of (\w+) is the (\d+)(st|nd|rd|th) largest of the European Union by population"
#print(re.search(patterncity, s1))

citysentence1 = re.sub(patterncity, r"\1 has the \2\3 largest population in the EU", s1)
citysentence2 = re.sub(patterncity, r"\1 has the \2\3 largest population in the EU", s2)

print("The Phrase becomes: \n" + citysentence1 +"\n The next phrase becomes \n "+ citysentence2)

#Problem 1.2 Freestyler

free1 = "We talkin' bout pizza rat"

patternfreestyle = r"\s(\w..)$"
#print(re.search(patternfreestyle, free1))
lastword = re.search(patternfreestyle, free1).group(1)
randomletter = random.choice(string.ascii_letters)
#rhymeScheme = re.sub(patternfreestyle, freestyle, free1)
word = lastword.split
newword = ''.join(randomletter + lastword[1:])
freestyle = f"we can make it rhyme with {newword}"
#print(rhymeScheme[len(rhymeScheme) - 3])
#correctscheme = rhymeScheme[0:[len(rhymeScheme) - 3]] + randomletter + rhymeScheme[[len(rhymeScheme) - 3]: len(rhymeScheme)-1]
#print(correctscheme)
#print(randomletter)
print("The Phrase: "+ free1 + "  "+ freestyle)

#Problem 1.3 Genes
genephrase = "Muscular LMNA interacting protein (MLIP) is a protein that in humans is encoded by Gene: MLIP, with sequence ACGTTG"
genepattern = r"Gene: (\w+)"
sequencepattern = r"sequence ([ACTG]+)"
gene = re.search(genepattern, genephrase).group(1)
sequence = re.search(sequencepattern, genephrase).group(1)
#print(gene)
#print(sequence)
print(f"The Gene {gene} has sequence {sequence}")

#genesequence = re.sub, 
# print(re.search(sequencepattern, genephrase))
# print(re.search(genepattern, genephrase))

#Problem 2

def elementrycontracted(sentence):
    count = 0
    sentence = nltk.regexp_tokenize(sentence, r'[\']\s*', gaps=False)
    for contractions in sentence:
         if contractions:
                count += 1
         else :
            return count 
    return count

print( "The count for contractions is: ", elementrycontracted("don't think I can't see you"))