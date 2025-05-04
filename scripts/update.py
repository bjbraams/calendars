import sys
import os
import datetime
import yaml
import myyaml

TODAY = datetime.date.today().strftime('%Y-%m-%d')

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

if latest:
    for event in latest:
        myyaml.capitalize(event)

all0 = past+future
if new:
    all0.extend(new)
if latest:
    all0.extend(latest)
all = myyaml.sorted_unique(all0)

past = []
future = []
for event in all:
    if str(event['dd']).replace(' ','\uffff') < TODAY:
        past.append(event)
    else:
        future.append(event)

with open('_data/all-'+TODAY+'.yml', 'w') as file:
    myyaml.dump(all,file)

with open('_data/past-'+TODAY+'.yml', 'w') as file:
    myyaml.dump(past,file)

with open('_data/future-'+TODAY+'.yml', 'w') as file:
    myyaml.dump(future,file)

with open('_data/new-'+TODAY+'.yml', 'w') as file:
    if latest:
        myyaml.dump(latest,file)
    file.write('# '+TODAY+'\n')
    if new:
        myyaml.dump(new,file)

with open('_data/latest-'+TODAY+'.yml', 'w') as file:
    file.write('# dd,name,link,loc,more,kw\n')

# Check to proceed
response = input(f"Return to proceed, Ctrl-c to cancel")

# Do not rename '_data/all-'+TODAY+'.yml'
os.rename('_data/past-'+TODAY+'.yml', '_data/past.yml')
os.rename('_data/future-'+TODAY+'.yml', '_data/future.yml')
os.rename('_data/new-'+TODAY+'.yml', '_data/new.yml')
os.rename('_data/latest-'+TODAY+'.yml', '_data/latest.yml')

print('Now do YAML to MD and git update')
