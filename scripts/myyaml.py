import yaml
from titlecase import titlecase

MANDATORY_KEYS = {'dd','name','loc','kw'}
OPTIONAL_KEYS = {'link','more','excerpt'}
RECOGNIZED_KEYS = {'dd','name','link','loc','more','kw','excerpt'}
    # = MANDATORY_KEYS|OPTIONAL_KEYS, sorted as we like it

def capitalize(event):
    if 'name' in event.keys():
        event['name'] = titlecase(event['name'])

def sort_event_keys(event):
    t = {}
    for k in RECOGNIZED_KEYS:
        if k in event.keys():
            t[k] = event[k]
    event = t

def sort_key(event):
    # Sort on dd, ties resolved by event name.
    # Replace spaces with a high-value Unicode character for sorting.
    # ('YYYY tbd' will come after any specific date in year YYYY.)
    return str(event['dd'])+str(event['name']).replace(' ','\uffff')

def check_pair(key,value,id):
    # Return a list of errors
    errors = []
    if key not in RECOGNIZED_KEYS:
        errors.append(f'Event {id} contains invalid key: {key}')
    if not isinstance(value,str):
        errors.append(f'Event {id} contains invalid value: {value}')
    return errors

def check_event(id,event):
    # Return a list of errors
    if not isinstance(event,dict):
        return [f'Event {id} is not a dictionary']
    if not MANDATORY_KEYS <= event.keys():
        return [f'Event {id} is missing a mandatory key']
    errors = []
    for key, value in event.items():
        errors.extend(check_pair(key,value,id))
    return errors

def check_update(id,update):
    # Return a list of errors
    if not isinstance(update,dict):
        return [f'Update {id} is not a dictionary']
    errors = []
    for key, value in update.items():
        errors.extend(check_pair(key,value,id))
    return errors

def check_calendar(calendar):
    # Return a list of errors
    if not isinstance(calendar,dict):
        return ['Calendar is not a dict']
    errors = []
    for id, event in calendar.items():
        errors.extend(check_event(id,event))
    return errors

def read_test_dict (fn):
    try:
        with open(fn) as f:
            dic = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f'YAML parsing error: {str(e)}')
        return {}
    except FileNotFoundError:
        print(f'Warning: file {fn} not found')
        return {}
    if not dic:
        print(f'Warning: file {fn} content is Null')
        return {}
    elif not isinstance(dic,dict):
        print(f'Warning: file {fn} is not a dict')
        return {}
    else:
        return dic

def dump(data,fn):
    # My specialized version of yaml.safe_dump
    yaml.safe_dump(data, fn, allow_unicode=True,
                   width=999, sort_keys=False)

def event_yaml_to_md(x,hl):
    # Generate a Markdown entry for calendar item x, highlight if hl.
    if 'link' in x.keys() and x['link']:
        if 'excerpt' in x.keys():
            link = x['link']+' "'+x['excerpt']+'"'
        else:
            link = x['link']
        a = x['dd']+': ['+x['name']+']('+link+'), '+x['loc']
    else:
        a = x['dd']+': '+x['name']+', '+x['loc']
    if 'more' in x.keys() and x['more']:
        b = '. '+x['more'].rstrip('.')+'.'
    else:
        b = '.' 
    if hl:
        return '**'+a+'**'+b
    else:
        return a+b

# def page_yaml_select_sort(source,main):
#     # Expand and sort the main file based on source.values()
#     main = {}
#     for x in main.keys():
#         if x in source.keys():
#             main[x] = source[x]
#     return sorted(main.items(), key = lambda item: sort_key(item[1]))

def page_yaml_to_md(main,highlights,TODAY):
    # Generate Markdown entries for a page.
    # Entries in main and in new are sorted differently.
    past_md = []
    future_md = []
    highlights_md = []
    # new_md = []
    for x, event in main.items():
        hl = x in highlights
        xmd = event_yaml_to_md(event,hl)
        if str(event['dd']).replace(' ','\uffff') < TODAY:
            past_md.append(xmd)
        else:
            future_md.append(xmd)
            if hl:
                highlights_md.append(xmd)
#   for x in new:
#       if x in main.keys():
#           event = main[x]
#           hl = x in highlights
#           xmd = event_yaml_to_md(event,hl)
#           if not str(event['dd']).replace(' ','\uffff') < TODAY:
#               new_md.append(xmd)
    return [past_md,future_md,highlights_md]

def pages_extend(key,y1,dests):
    if y1.strip().startswith('+'):
        y, hl = [y1.lstrip(' +').rstrip(),True]
    else:
        y, hl = [y1.strip(),False]
    if y not in dests.keys():
        dests[y] = {'main':set(),'hl':set()}
    dests[y]['main'].add(key)
    if hl:
        dests[y]['hl'].add(key)

def base_to_pages(data):
    # Assume that data has been checked for errors
    pages = {}
    for key, event in data.items():
        if 'kw' in event.keys():
            for y1 in event['kw'].split(','):
                pages_extend(key,y1,pages)
    return pages
