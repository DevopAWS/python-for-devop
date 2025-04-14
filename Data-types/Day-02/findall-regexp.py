import re

text = " the python course is "
pattern = r"python"

search = re.search(pattern,text)
if search:
    print(" pattren is found :", search.group())
else:
    print("pattren not found")