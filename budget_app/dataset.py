from transformers import AutoTokenizer
import pandas as pd
from datasets import Dataset,load_dataset
GAIN_LOST = "budget_app\gain-lost, tag-label.csv"
ITEM_TAG = "budget_app\Item Description,TagLabel.csv"
#    Pre-Process Data
#    Use correct File Path Relative
#    The CSV file read is in format: item-description, tag-label
def tokenization(dataset):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    tokenized = tokenizer(dataset["item-description"])
    # print(tokenized)
    return tokenized    

def pre_process_csv(csvfile):
    raw_data = pd.read_csv(f"{csvfile}")
    raw_data = pd.DataFrame(raw_data)
    raw_data_test = raw_data
    raw_data_test['tag-label'] = None
    dataset = Dataset.from_pandas(raw_data, split="train")
    datasetTest = Dataset.from_pandas(raw_data_test, split="test")
    # print(dataset) 
    # print(datasetTest)

    dataset = dataset.map(tokenization, batched=True)
    # print(dataset)
    dataset = dataset.set_format(type="torch", columns=['item-description', 'tag-label', 'input_ids', 'token_type_ids', 'attention_mask'])
    print(dataset)

# def alt_pre_process_csv(csvfile):
#     raw_data = pd.read_csv(f"{csvfile}")
#     data_dictonary = raw_data.to_dict(orient="records")
#     dataset = Dataset.from_dict(data_dictonary)
#     print(dataset)    
    
# alt_pre_process_csv(GAIN_LOST)


# pre_process_csv("budget_app\gain-lost, tag-label.csv")
pre_process_csv("budget_app\Item Description,TagLabel.csv")
# load_dataset("csv", data_dir=GAIN_LOST, sep="\t")