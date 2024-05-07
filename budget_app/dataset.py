import torch
import torch.utils
import torch.utils.data
from transformers import AutoTokenizer
import pandas as pd
from datasets import Dataset,load_dataset
GAIN_LOST = "budget_app\gain-lost, tag-label.csv"
ITEM_TAG = "budget_app\Item Description,TagLabel.csv"
#    Pre-Process Data
#    Use correct File Path Relative
#    The CSV file read is in format: item-description, tag-label
   

# def convert_tensors(batch):
#     item_description = [item['item-description'] for item in batch]
#     label = torch.tensor([label_map[item["tag-label"] for item in batch]])
#     input_ids = torch.tensor([item["input_ids"] for item in batch])
#     token_type_ids = torch.tensor([item["token_type_ids"] for item in batch])
#     attention_mask = torch.tensor([item["attention_mask"] for item in batch])
    
#     print("Sample batch after tokenization:")
#     print(f"Description: {item_description[0]}") 
#     print(f"Input IDs: {input_ids[0]}")  
#     print(f"Token Type IDs: {token_type_ids[0]}")  
#     print(f"Attention Mask: {attention_mask[0]}")
    
#     return item_description, label, input_ids, token_type_ids, attention_mask

def pre_process_csv(csvfile, label_col = "tag-label"):

    label_map = {}
    new_label_id = 0
    raw_data = pd.read_csv(f"{csvfile}")
    raw_data = pd.DataFrame(raw_data)
    raw_data["tag-label"] = raw_data[label_col]
    
    for i in range(len(raw_data)):
        label = raw_data.loc[i, "tag-label"]
        if label not in label_map:
            print(label)
            label_map[label] = new_label_id
            new_label_id += 1
        raw_data.loc[i, "tag-label"] = label_map[label]
        # print(label_map[label])
        
    print("First few rows with labels: ")
    print(raw_data.head())
    raw_data_test = raw_data.copy()
    raw_data_test['tag-label'] = None
    dataset = Dataset.from_pandas(raw_data, split="train")
    datasetTest = Dataset.from_pandas(raw_data_test, split="test")
    # print(dataset) 
    # print(datasetTest)
    def tokenization(dataset):
        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        tokenized = tokenizer(dataset["item-description"], padding="max_length", truncation=True)
        # print(tokenized)
        return tokenized 
    
    dataset = dataset.map(tokenization, batched=True)
    # print(dataset)
    def convert_tensors(batch):
            item_description = [item['item-description'] for item in batch]
            label = torch.tensor([label_map [item["tag-label"]] for item in batch])
            input_ids = torch.tensor([item["input_ids"] for item in batch])
            token_type_ids = torch.tensor([item["token_type_ids"] for item in batch])
            attention_mask = torch.tensor([item["attention_mask"] for item in batch])
            
            print("Sample batch after tokenization:")
            print(f"Description: {item_description[0]}") 
            print(f"Input IDs: {input_ids[0]}")  
            print(f"Token Type IDs: {token_type_ids[0]}")  
            print(f"Attention Mask: {attention_mask[0]}")
            
            return item_description, label, input_ids, token_type_ids, attention_mask
    dataset = dataset.set_format(
        type="torch",
        columns=['item-description',
                 'tag-label',
                 'input_ids',
                 'token_type_ids',
                 'attention_mask']
        )
    
    train_dataset = torch.utils.data.DataLoader(dataset, batch_size=32, collate_fn=convert_tensors)
    test_dataset = torch.utils.data.DataLoader(datasetTest, batch_size=32, collate_fn=convert_tensors)
    print(dataset)
    return train_dataset, test_dataset

# def alt_pre_process_csv(csvfile):
#     raw_data = pd.read_csv(f"{csvfile}")
#     data_dictonary = raw_data.to_dict(orient="records")
#     dataset = Dataset.from_dict(data_dictonary)
#     print(dataset)    
    
# alt_pre_process_csv(GAIN_LOST)


# pre_process_csv("budget_app\gain-lost, tag-label.csv")
pre_process_csv("budget_app\Item Description,TagLabel.csv")
# load_dataset("csv", data_dir=GAIN_LOST, sep="\t")