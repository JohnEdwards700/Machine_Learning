import nltk
s1 = "In New york you can buy a car for free"
s2 = "past the brook, over the ocean side. Lies 2 great $"
x = nltk.regexp_tokenize(s1, pattern=r"\w+")#gaps = True#) allows seperation based on punctiation
print(x)