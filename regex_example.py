# from https://vegibit.com/how-to-use-python-regular-expressions-for-pattern-matching/
import re

text = "Dante the Groundhog"
pattern = r"[Gg]roundhog"
#will return the first instance in the bracket if found else it will continue on to check other letters in bracket
#you can do [2-5] it will check all num in range of that starting with the first num
#[^2-5] means look for not those nums
# a* means zero or more of a
# r"groundhogs?" the ? means the last thing is either there or not

match = re.search(pattern, text)

if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")
