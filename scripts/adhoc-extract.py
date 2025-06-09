#!/usr/bin/env python3

import sys
import myyaml

with open('_data/main.yml') as f:
    main = myyaml.read_yml_dict(f)
for ident, event in main.items():
    if 'https://indico.cern.ch/event/' in event.get('link',''):
        event.setdefault('name',ident)
        myyaml.dump({ident:event['name']},sys.stdout)
