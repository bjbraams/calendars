import sys
import os
import datetime
import yaml
import myyaml

def new_dest_yml(y): # Has side effects!
    # Prepare new destination for YAML files
    try:
        with open(f'{y}/_data/main.yml','r') as fmain:
            try:
                y_prev = yaml.safe_load(fmain)
            except yaml.YAMLError as e:
                sys.exit(
                    f'YAML parsing error in {y}/_data/main.yml: {str(e)}')
            except:
                sys.exit(f'Unidentified error in {y}/_data/main.yml')
        if not y_prev:
            y_prev = {}
        with open(f'{y}/_data/prev.yml','w') as fprev:
            myyaml.dump(y_prev,fprev)
        dest =\
            {'prev':y_prev,
             'main':open(f'{y}/_data/main.yml','w'),
             'hl':open(f'{y}/_data/highlights.yml','w'),
             'new':open(f'{y}/_data/new-{TODAY}.yml','a')}
    except: 
        print (f'Not accessible: {y}/_data/')
        dest = None
    return dest

def new_dest_md(y): # Has side effects!
    # Prepare new destination for Markdown files
    try:
        dest =\
            {'past':open(f'{y}/_includes/past.md','w'),
             'future':open(f'{y}/_includes/future.md','w'),
             'hl':open(f'{y}/_includes/highlights.md','w'),
             'new':open(f'{y}/_includes/new.md','w')}
    except: 
        print (f'Not accessible: {y}/_includes/')
        dest = None
    return dest

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
    data = myyaml.read_yml_dict(f)
for key, event in data.items():
    errors = myyaml.check_event(key,event)
    if errors:
        print(f'Errors in item {key}:\n')
    for error in errors:
        print(error)

# Compute page contents
pages = myyaml.base_to_pages(data)

# Check to proceed
input(f'Return to proceed with */_data/*.yml, Ctrl-c to cancel')

# Write the results
for y, p in pages.items():
    dest = new_dest_yml(y)
    if dest:
        for x in p['main']:
            myyaml.dump({x:None},dest['main'])
            if x not in dest['prev'].keys():
                myyaml.dump({x:None},dest['new'])
        for x in p['hl']:
            myyaml.dump({x:None},dest['hl'])
        dest['main'].close()
        dest['hl'].close()
        dest['new'].close()

# Check to proceed
input(f'Return to proceed with */_includes/*.md, Ctrl-c to cancel')

# Proceed with conversion to Markdown
# (Files new.md to follow)
for y, p in pages.items():
    dest = new_dest_md(y)
    if dest:
        page0 = {}
        for x in p['main']:
            page0[x] = data[x]
        page1 = sorted(page0.items(),
                       key=lambda item: myyaml.sort_key(item[1]))
        page = {}
        for x, event in page1:
            page[x] = event
        past_md, future_md, hl_md =\
            myyaml.page_yaml_to_md(page,p['hl'],TODAY)
        for line in past_md:
            dest['past'].write(line+'\n\n')
        for line in future_md:
            dest['future'].write(line+'\n\n')
        for line in hl_md:
            dest['hl'].write(line+'\n\n')
