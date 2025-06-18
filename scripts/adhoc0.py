#!/usr/bin/env python3

import sys
import myyaml
import myvaria

dic0 = myyaml.read_yml_dict(sys.stdin)
for url, name in dic0.items():
    myyaml.dump({name:{'link':url}},sys.stdout)
