import re

file_path = "/Users/howardliao/Desktop/Howard/Howard_CISO/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's inspect how setLang renders headings and card titles.
print("File length before:", len(content))
