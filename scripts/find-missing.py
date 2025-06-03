#!/usr/bin/env python3

import sys
import myyaml

wanted = set([t0.strip() for t0 in sys.argv[1].split(',')])
with open('_data/main.yml') as f:
    main = myyaml.read_yml_dict(f)
for ident, event in main.items():
    if not wanted.issubset(event.keys()):
        myyaml.dump({ident:event},sys.stdout)
