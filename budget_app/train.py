from budget_app.configDataset import *
import torch
from transformers import RobertaModel, TrainingArguments
from transformers import Trainer
import numpy as np
import evaluate

model = RobertaModel.from_pretrained('roberta-base', num_label= 5)
training_args = TrainingArguments(
    'roberta-base',
    ouptut_dir="budget_app\budgetbot_v1.0.pt",
    evaluation_strategy= "epoch",
    per_device_train_batch_size=16,
    per_gpu_eval_batch_size=16,
    num_train_epochs=5,
    learning_rate=2e-5,
    weight_decay=0.01,)

metric = evaluate.load("accuracy")

def compute_metrics(evaluation_prediction):
    logits, labels = evaluation_prediction
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

trainer = Trainer(
    model,
    training_args,
    train_dataset=complete_train,
    eval_dataset=complete_test,
    compute_metrics=compute_metrics,
    )
trainer.train()

