#!/usr/bin/env python3

import sys
import myyaml
import myvaria

with open('_data/main.yml') as f:
    main = myyaml.read_yml_dict(f)
for ident, event in main.items():
    url = event.get('url','')
    info = myvaria.get_url_status(url)
    if 301 == info['code']:
        update = {'url':info['dest']}
        myyaml.dump({ident:update},sys.stdout)
