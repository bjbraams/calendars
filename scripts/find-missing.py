#!/usr/bin/env python3

import sys
import myyaml

item = sys.argv[1]
with open('_data/main.yml') as f:
    main = myyaml.read_yml_dict(f)
for key, event in main.items():
    if not event.get(item,''):
        myyaml.dump({key:event},sys.stdout)
