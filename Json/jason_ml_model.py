import json
import numpy as np

path = r'C:\Users\behna\OneDrive\Documents\Data Science - Projects\20220615 JasonRead\2. Prepared Data\snli_1.0_train.jsonl'

data = []
with open(path, 'r') as j_file:
    while j_file:

        data.append(line)

json.loads(data).keys()