#!/usr/bin/env python3
#
# Part of: https://github.com/bjbraams/calendars.
#
# Description: Process a YAML calendar file and its intended update
# files. Report errors; optionally proceed to apply the updates.
#
# Common issues:
# - A 'dd' entry is seen as a date and not as a string. In the YAML
# file, a date range is fine, that is recognized as a string. But a
# single date is interpreted as a date, so there quotes must be used.
# - An intended string contains a ": " and YAML sees it as a key-value
# pair. Such a string must be quoted.
# - An intended string starts with an opening square bracket and YAML
# sees it as a list. Such an initial square bracket must be escaped.
# - An intended string starts with "*", "!" or "- " and this is seen
# as a YAML syntax item. Such a special character must be escaped.

import sys
import os
import datetime
import yaml
import myyaml

TODAY = datetime.date.today().strftime('%Y-%m-%d')

# Minimal test for core files
if not os.path.isdir('_data'):
    print('Error: directory ./_data/ not found')
    sys.exit(1)
elif not os.path.isfile('_data/main.yml'):
    print('Error: file ./_data/main.yml not found')
    sys.exit(1)

# Further tests
print('Checking _data/main.yml...')
main = myyaml.read_test_dict('_data/main.yml')
for key, event in main.items():
    errors = myyaml.check_event(key,event)
    if errors:
        print(f'Errors in item {key}:\n')
    for error in errors:
        print(error)

print('Checking _data/latest.yml...')
latest = myyaml.read_test_dict('_data/latest.yml')
for key, event in latest.items():
    for error in myyaml.check_event(key,event):
        print(error)

print('Checking _data/deletes.yml...')
deletes = myyaml.read_test_dict('_data/deletes.yml')
for key in deletes.keys():
    if key not in main.keys:
        print(f'key {key} is not found')
        del deletes[key]

print('Checking _data/updates.yml...')
updates = myyaml.read_test_dict('_data/updates.yml')
for key, update in updates.items():
    for error in myyaml.check_update(key,update):
        print(error)

if not main:
    print('Watch out: Old file main.yml is empty')

# Apply the updates to the local files
for key in deletes.keys():
    del main[key]

for key, event in updates.items():
    myyaml.sort_event_keys(event)
    if key in main.keys():
        main[key].update(event)
    else:
        main[key] = event

for key, event in latest.items():
    myyaml.sort_event_keys(event)
    myyaml.capitalize(event)
    main[key] = event

# Check to proceed
input(f'Return to proceed, Ctrl-c to cancel')

os.rename('_data/main.yml', '_data/main-'+TODAY+'.yml')
with open('_data/main.yml', 'w') as file:
    myyaml.dump(main,file)
with open('_data/new-'+TODAY+'.yml', 'a') as file:
    myyaml.dump(latest,file)
with open('_data/latest.yml', 'w') as file:
    file.write('# <id>:{dd,name,link,loc,more,kw}\n')
with open('_data/deletes.yml', 'w') as file:
    file.write('# <id>:\n')
with open('_data/updates.yml', 'w') as file:
    file.write('# <id>:{dd,name,link,loc,more,kw}\n')

print('Now do YAML to MD and git update')
