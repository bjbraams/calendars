import sys
import yaml

def process(text):
    return ''.join(char for char in text if char.isdigit() or char.isupper())

data = yaml.safe_load(sys.stdin)
if not data:
    data = []
data_out = []

for x in data:
    x['id'] = process(str(x['id']))
    data_out.append(x)

yaml.safe_dump(data_out, sys.stdout,
               allow_unicode=True, width=999, sort_keys=False)
