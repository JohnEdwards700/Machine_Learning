from dataset import *
from LSTM.ltsmmodel import *

model = LSTMTagger(EMBEDDING_DIM, HIDDEN_DIM, len(word_to_ix), len(tag_to_ix))
loss_function = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

def train(model, loss_fn, training_data, word_to_ix, tag_to_ix, optimizer, epoch=10):
     for epoch in range(epoch):  # again, normally you would NOT do 300 epochs, it is toy data
       for sentence, tags in training_data:
           model.zero_grad()

           # Step 2. Get our inputs ready for the network, that is, turn them into
           # Tensors of word indices.
           sentence_in = seq_to_embedding(sentence, word_to_ix)
           targets = seq_to_embedding(tags, tag_to_ix)

           # Step 3. Run our forward pass.
           tag_scores = model(sentence_in)
           # Step 4. Compute the loss, gradients, and update the parameters by
           #  calling optimizer.step()
           loss = loss_fn(tag_scores, targets)
           print("loss for epoch ", epoch, ":", loss)
           loss.backward()
           optimizer.step()