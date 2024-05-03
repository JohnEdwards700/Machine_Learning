import constants as c
import collections
import nltk
import numpy as np
import random
import json
import string
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import matplotlib.pyplot as plt

def net_worth_chart():
#style
# previous style = _mpl-gallery-nogrid
    plt.style.use('dark_background')
# make data
    x = [30000,60000]
    labels = ["checkings","savings"]
    colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(x)))
# plot
    fig, ax = plt.subplots()
    ax.pie(x, labels=labels ,colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "black"}, frame=True)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
    
    return fig




# nltk.download("punkt")
# nltk.download("wordnet")

###   Implementation for nltk tokenization, lemmatization, Bag of Words ###
def lemmatize_date():
#Here I am Reading the Intents JSON File
    with open('budget_app\intents.json', encoding='utf-8') as data_file:
        data = json.load(data_file)
    
    # print(json.dumps(data, indent=2))

    #initilizing Data
    words = [] #for BOW vocabulary patterns
    classes = [] #for BOW tags
    data_X = [] #storing patterns
    data_Y = [] #tag corresponding to the pattern

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            tokens = nltk.word_tokenize(pattern) #tokenize each pattern
            words.extend(tokens) #append tokens to words[]
            data_X.append(pattern) #append to data_X
            data_Y.append(intent["tag"]) #for each pattern append associated tag
        #gets all tags in json file
        if intent["tag"] not in classes:
            classes.append(intent["tag"])
            

    #change words to lower and lemmatize them if they aren't punctuation
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in string.punctuation]
    #sort vocab and classes, also removing duplicates by using hash set
    words = sorted(set(words))
    classes = sorted(set(classes))


    print("Words List: ",words, "\nClasses List:" ,classes)

    #for index and doc in data
    training = []
    #each positon is represented with a zero and if it stays zero then no word exist in there
    out_empty = [0 for _ in range(len(classes))] #[0] * len(classes)
    #getting a list of (index, word) with enumerate
    for i, doc in enumerate(data_X):
        bow = []
        text = lemmatizer.lemmatize(doc.lower())
        for word in words:
            if word in text:
                bow.append(1)
            else:
                bow.append(0)
            
            output_row = list(out_empty)
            output_row[classes.index(data_Y[i])] = 1
            training.append([bow, output_row])

    # print(training) --> this outputed zeros and ones for what was found
    #code for training data by shuffle and easier for nueral network integration
    random.shuffle(training)
    training = np.array(training, dtype=object)
    #training data is split up
    train_X = np.array(list(training[:,0]))
    train_Y = np.array(list(training[:,1]))


###   End of Implementation   ###




##    ADD Nueral network Model   ##

## Process Input ##





#def find_keyphrases(text):
    # tokens = tokenize(text)
    # return any(token in c.CURRENT_USER_RESPONSE for token in tokens)
# def account_match(text):
#     accountpattern = r"accountid(\d+)"
#     match = re.match(accountpattern, text)
#     print(match.group(1))  
# print(account_match("accountid1"))


def tokenize(text):
    return text.lower().split()    

def is_goal(text):
    tokens = tokenize(text)
    return any(token in c.BUDGET_TYPES for token in tokens)

def match(question):
    pattern = r"\b(save|spend|invest|accountid)\b"
    #tokens = tokenize(question)
    #print(tokens)
    matches = re.findall(pattern, question.lower(), flags=re.IGNORECASE)
    # if matches:
    #     tokens = ''.join(matches)
    #     tokens = tokenize(tokens)
    #     return tokens
    # print(tokens)
    
    best_match = None
    best_score = 0
    
    for answer, response in c.KNOWLEDGE_BASE.items():
        answer_tokens = tokenize(answer)
        score = sum(token in matches for token in answer_tokens)
        # print(score)
        if score > best_score:
            best_match = answer
            best_score = score
    return best_match

# match("my my accountid is 1234")

def account_info(account_id):
    accounts = c.DEMO_ACCOUNTS
    #print(accounts)
    for info in accounts:
        if account_id == info["accountid"]:
            print(f"This is your account ID: {account_id}")
            name = info["name"]
            account_amount = info["account_amount"]
            savings = info["savings"]
            checking = info["checking"]
            goals = info["goals"]
            spending = info["spending"]
            return f"Your Name: {name}\nNet_Worth: ${account_amount}\nSavings: ${savings}\nCheckings: ${checking}\nSpenditures: {spending}\nGoals:{goals}"
            break
        else:
            return "Account not found"
    
    #any(account in accounts for account_id in accounts):
    
    
#print(account_info(1))

    

def respond(question):
    #if is_goal(question):
    #    return "Gotchu"
   
    best_match = match(question)
    
    
    if best_match:
        if best_match == "accountid":
            accountpattern = r"\b(\d+)\b"
            matchid = re.match(accountpattern, question)
            print(matchid)
            if matchid and type(int(matchid.group(1))) == int:
                numid = matchid.group(1)
                print(numid)
                return f"{c.KNOWLEDGE_BASE[best_match]}{account_info(1)}"
            else:
                return f"{c.KNOWLEDGE_BASE[best_match]}{account_info(1)} no id"
        if best_match == "save":
            save_goal = input(c.KNOWLEDGE_BASE[best_match])
            return f"I've got a few ways to save ${save_goal}"
        if best_match == "invest":
            invest_goal = input(c.KNOWLEDGE_BASE[best_match])
            return f"we should try and invest that ${invest_goal}"
        else:
            return c.KNOWLEDGE_BASE[best_match]
    else:
        return "I don't know that Phrase, try rewording because I don't understand yet."
    