import re

text = "this is python course"

pattern = r"python"

match = re.match(pattern,text)
if match:
    print ("match found :", match.group())
else:
    print ("match not found")