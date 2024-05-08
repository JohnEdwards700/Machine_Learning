import csv

def replace_tags_in_csv(input_file, output_file):
  """
  Replaces all occurrences of 'old_tag' in the second column of a CSV file
  with 'new_tag'. Writes the modified data to a new CSV file.

  Args:
    input_file: Path to the input CSV file.
    output_file: Path to the output CSV file.
    old_tag: The tag to be replaced.
    new_tag: The tag to replace 'old_tag' with.
  """

  with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header row (if it exists) and write it to the output file
    headers = next(reader)
    writer.writerow(headers)
    
    old_tags1 = ['Personal Care & Clothing']  # Tag to be replaced
    new_tag1 = 'Retail'  # Tag to replace with
    old_tags2 = ['Insurance','Taxes','Utilities','Retirement','Sports & Fitness','Healthcare','Education']  # Tag to be replaced
    new_tag2 = 'Bills'  # Tag to replace with
    old_tags3 = ['Investment']  # Tag to be replaced
    new_tag3 = 'Employment'  # Tag to replace with
    old_tags4 = ['Transportation']  # Tag to be replaced
    new_tag4 = 'Travel'  # Tag to replace with
    
    def replace_tag(old_tags, new_tag):
        for row in reader:
            for tag in old_tags:
                row[1] = row[1].replace(tag, new_tag)
            writer.writerow(row)
        
    replace_tag(old_tags3, new_tag3)
    # for row in reader:
    #   row[1] = row[1].replace(old_tag, new_tag)
    #   writer.writerow(row)
      
   

# Example usage
output_file = 'budget_app\csvdemo1.csv'
input_file= 'budget_app\csvdemo.csv'


replace_tags_in_csv(input_file, output_file)

print(f'Tags replaced in {input_file} and written to {output_file}')
