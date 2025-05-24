#!/usr/bin/env python3

import myyaml

main = myyaml.read_yml_dict('_data/main.yml')
for key, event in main.items():
    if not event.get('excerpt',''):
        print(myyaml.dump({key:event}))
