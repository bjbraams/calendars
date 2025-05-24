#!/usr/bin/env python3

import sys
import myyaml

main = myyaml.read_yml_dict('_data/main.yml')
for key, event in main.items():
    if not event.get('excerpt',''):
        myyaml.dump({key:event},sys.stdout)
