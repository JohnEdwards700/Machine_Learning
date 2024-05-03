# Author: Robert Guthrie

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd

def prepare_sequence(seq, to_ix):
    idxs = [to_ix[w] for w in seq]
    return torch.tensor(idxs, dtype=torch.long)

#  pre-process csv file
training_data_unclean = pd.read_csv('LSTM/text.csv')
texts = [t.split() for t in training_data_unclean["text"].tolist()]
tags = [t.split() for t in training_data_unclean["tag"].tolist()]
training_data = list(zip(texts, tags))
#print(training_data)
#Output: [( [text] , [tags] ), ...]

#   map token to index
#Output: [( [text:int] , [tags:int] ), ...]
def seqs_to_dictionary(training_data: list):
     word_to_ix = {}
     tag_to_ix = {}
     word_count = tag_count = 0

     for sent, tags in training_data:
        for word in sent:
           if word not in word_to_ix:
              word_to_ix[word] = word_count
              word_count += 1
        for tag in tags:
           if tag not in tag_to_ix:
              tag_to_ix[tag] = tag_count
              tag_count += 1

     return word_to_ix, tag_to_ix

word_to_ix, tag_to_ix = seqs_to_dictionary(training_data)
# print(word_to_ix) 
# print(tag_to_ix) 

EMBEDDING_DIM = 6
HIDDEN_DIM = 6


class LSTMTagger(nn.Module):

    def __init__(self, embedding_dim, hidden_dim, vocab_size, tagset_size):
        super(LSTMTagger, self).__init__()
        self.hidden_dim = hidden_dim

        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)

        # The LSTM takes word embeddings as inputs, and outputs hidden states
        # with dimensionality hidden_dim.
        self.lstm = nn.LSTM(embedding_dim, hidden_dim)

        # The linear layer that maps from hidden state space to tag space
        self.hidden2tag = nn.Linear(hidden_dim, tagset_size)

    def forward(self, sentence):
        embeds = self.word_embeddings(sentence)
        lstm_out, _ = self.lstm(embeds.view(len(sentence), 1, -1))
        tag_space = self.hidden2tag(lstm_out.view(len(sentence), -1))
        #tag_scores = F.log_softmax(tag_space, dim=1)
        predicted_tags = torch.max(tag_space, dim=1)
        # return tag_scores
        return predicted_tags
    
model = LSTMTagger(EMBEDDING_DIM, HIDDEN_DIM, len(word_to_ix), len(tag_to_ix))
loss_function = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

with torch.no_grad():
    inputs = prepare_sequence(training_data[0][0], word_to_ix)
    tag_scores = model(inputs)
    print(tag_scores)

for epoch in range(300):  # again, normally you would NOT do 300 epochs, it is toy data
    for sentence, tags in training_data:
        model.zero_grad()
        sentence_in = prepare_sequence(sentence, word_to_ix)
        targets = prepare_sequence(tags, tag_to_ix)
        tag_scores = model(sentence_in)
        loss = loss_function(tag_scores, targets)
        loss.backward()
        optimizer.step()

with torch.no_grad():
    inputs = prepare_sequence(training_data[0][0], word_to_ix)
    tag_scores = model(inputs)
    predicted_tags_list = [tag_to_ix[i.item()] for i in predicted_tags]
    print("Original sentence:", training_data[0][0])
    print("Predicted tags:", predicted_tags_list)
    print(tag_scores)