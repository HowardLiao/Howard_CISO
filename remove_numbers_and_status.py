import re

file_path = "/Users/howardliao/Desktop/Howard/Howard_CISO/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# Let's inspect where hero.status and 01 02 03 are
print("Contains hero.status:", "hero.status" in code)
print("Contains 隨時履新高階主管:", "隨時履新高階主管" in code)
