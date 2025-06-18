#!/usr/bin/env python3

import sys
import myyaml
import myvaria

with open('_data/main.yml') as f:
    main = myyaml.read_yml_dict(f)
for ident, event in main.items():
    name = event.get('name',ident)
    url = event.get('url','')
    info = myvaria.get_url_status(url)
    if not info['code'] or 400 <= info['code']:
        myyaml.dump({ident:name},sys.stdout)
