#!/usr/bin/env python3

import sys
import myyaml
TRUNC = 120

with open('_data/main.yml') as f:
    main = myyaml.read_yml_dict(f)
for ident, event in main.items():
    if TRUNC <= len(ident):
        event.setdefault('name',ident)
    myyaml.dump({ident:myyaml.sort_event_keys(event)},sys.stdout)    
