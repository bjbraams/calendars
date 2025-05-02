import sys
import os
from datetime import date
import yaml
import myyaml

TODAY = date.today().strftime('%Y-%m-%d')

cwd = os.getcwd()
if os.path.basename(cwd) != 'calendars':
    print('wrong working directory: '+cwd)
    sys.exit(1)

print('Checking _data/past.yml...\n')
with open('_data/past.yml') as file:
    past = yaml.safe_load(file)
errors = myyaml.check_calendar(past)
for error in errors:
    print(error)

print('Checking _data/future.yml...\n')
with open('_data/future.yml') as file:
    future = yaml.safe_load(file)
errors = myyaml.check_calendar(future)
for error in errors:
    print(error)

print('Checking _data/new.yml...\n')
with open('_data/new.yml') as file:
    new = yaml.safe_load(file)
errors = myyaml.check_calendar(new)
for error in errors:
    print(error)

print('Checking _data/latest.yml...\n')
with open('_data/latest.yml') as file:
    latest = yaml.safe_load(file)
errors = myyaml.check_calendar(latest)
for error in errors:
    print(error)

for event in latest:
    myyaml.capitalize(event)

all = myyaml.sorted_unique(past+future+latest)

with open('_data/all-'+TODAY+'.yml', 'w') as file:
    yaml.safe_dump(all, file,
                   allow_unicode=True, width=999, sort_keys=False)

with open('_data/new-'+TODAY+'.yml', 'w') as file:
    yaml.safe_dump(latest, file,
                   allow_unicode=True, width=999, sort_keys=False)
    file.write('# '+TODAY+'\n')
    yaml.safe_dump(new, file,
                   allow_unicode=True, width=999, sort_keys=False)

with open('_data/latest-'+TODAY+'.yml', 'w') as file:
    file.write('# dd,name,link,loc,more,kw\n')

f0 = open('_data/past-'+TODAY+'.yml', 'w')
f1 = open('_data/future-'+TODAY+'.yml', 'w')

for event in all:
    if str(event['dd']).replace(' ','\uffff') < TODAY:
        yaml.safe_dump([event], f0, allow_unicode=True,
                       width=999, sort_keys=False)
    else:
        yaml.safe_dump([event], f1, allow_unicode=True,
                       width=999, sort_keys=False)

# Check to proceed
response = input(f"Return to proceed, Ctrl-c to cancel")

# Do not rename '_data/all-'+TODAY+'.yml'
os.rename('_data/new-'+TODAY+'.yml', '_data/new.yml')
os.rename('_data/latest-'+TODAY+'.yml', '_data/latest.yml')
os.rename('_data/past-'+TODAY+'.yml', '_data/past.yml')
os.rename('_data/future-'+TODAY+'.yml', '_data/future.yml')
