import re

text = " this is java for the devops for the java course"

pattern = r"java"

replacement = "python"


new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)