#!/usr/bin/env python3

import sys
import os
import datetime
import yaml
import myyaml

main = myyaml.read_test_dict('_data/main.yml')
for key, event in main.items():
    errors = myyaml.check_event(key,event)
    if errors:
        print(f'Errors in item {key}:\n')
    for error in errors:
        print(error)

if not main:
    print('Watch out: Old file main.yml is empty')

for key, event in main.items():
    if 'excerpt' not in event.keys() or not event['excerpt']:
        print(yaml.dump({key:event}))
