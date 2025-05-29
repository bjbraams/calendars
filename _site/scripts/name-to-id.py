#!/usr/bin/env python3

import sys
import myyaml

with open('_data/main.yml') as f:
    main = myyaml.read_yml_dict(f)
for key, event in main.items():
    key = str(event['name'])
    event.pop('name')
    myyaml.dump({key:event},sys.stdout)    
