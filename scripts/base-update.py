#!/usr/bin/env python3
#
# Part of: https://github.com/bjbraams/calendars.
#
# Description: Process a YAML calendar file and its update files.
# Report errors; optionally proceed to apply the updates.
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
from titlecase import titlecase
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
with open('_data/main.yml') as f:
    main = myyaml.read_yml_dict(f)
for ident, event in main.items():
    errors = myyaml.check_event(ident,event)
    if errors:
        print(f'Errors in item {ident}:\n')
    for error in errors:
        print(error)

print('Checking _data/latest.yml...')
with open('_data/latest.yml') as f:
    latest = myyaml.read_yml_dict(f)
for ident, event in latest.items():
    errors = myyaml.check_event(ident,event)
    if errors:
        print(f'Errors in item {ident}:\n')
    for error in errors:
        print(error)

print('Checking _data/deletes.yml...')
with open('_data/deletes.yml') as f:
    deletes = myyaml.read_yml_dict(f)
for ident in deletes.keys():
    if ident not in main.keys():
        print(f'key {ident} is not found')
        del deletes[ident]

print('Checking _data/updates.yml...')
with open('_data/updates.yml') as f:
    updates = myyaml.read_yml_dict(f)
for ident, update in updates.items():
    for error in myyaml.check_update(ident,update):
        print(error)

if not main:
    print('Fatal error: Old file main.yml is empty')
    sys.exit(1)

# Apply the updates to the local files
for ident in deletes.keys():
    del main[ident]

for ident, event in updates.items():
    t0 = main.get(ident,{})|event
    main[ident] = myyaml.sort_event_keys(t0)

for ident, event in latest.items():
    main[titlecase(ident)] = myyaml.sort_event_keys(event)

main1 = sorted(main.items(),
               key=lambda item: myyaml.sort_key(item))
main = dict(main1)

# Check to proceed
input(f'Return to proceed, Ctrl-c to cancel')

os.rename('_data/main.yml', '_data/main-'+TODAY+'.yml')
with open('_data/main.yml', 'w') as f0:
    myyaml.dump(main,f0)
with open('_data/new-'+TODAY+'.yml', 'a') as f0:
    if latest:
        myyaml.dump(latest,f0)
with open('_data/latest.yml', 'w') as f0:
    f0.write('# <name>:{dd,link,loc,more}\n')
with open('_data/deletes.yml', 'w') as f0:
    f0.write('# <name>:\n')
with open('_data/updates.yml', 'w') as f0:
    f0.write('# <name>:{dd,link,loc,more}\n')

print('Now do YAML to MD and git update')
