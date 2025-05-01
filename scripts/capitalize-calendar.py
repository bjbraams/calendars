import sys
import yaml
from titlecase import titlecase

def capitalize(event):
    event['name'] = titlecase(event['name'])

data = yaml.safe_load(sys.stdin)
for event in data:
    capitalize(event)

yaml.safe_dump(data, sys.stdout,
               allow_unicode=True, width=999, sort_keys=False)
