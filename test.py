string = """{
        "hello":"world",
        "name":"zyz"
    }
"""
import re
from typing import Pattern

PATTERN = re.compile(r"[^{]*{\s*([^}]+)\s*}")

list_1 = re.findall(PATTERN, string)
x = []
for i in list_1:
    x.append(re.sub(r"(?<!,)\n", r",", i))

print(x)
