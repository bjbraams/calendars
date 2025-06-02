import yaml

MANDATORY_KEYS = ['dd']
RECOGNIZED_KEYS = MANDATORY_KEYS+[
    'name','link','loc','more',
    'kw','arxiv','msc','inspec','excerpt']
    # Lists sorted as we like it
SetMK = set(MANDATORY_KEYS)
SetRK = set(RECOGNIZED_KEYS)

def sort_event_keys(event):
    t = {}
    for k in RECOGNIZED_KEYS:
        if k in event.keys():
            t[k] = event[k]
    for k in event.keys():
        t.setdefault(k,event[k])
    return t

def sort_key(item):
    # item is [ident,event]. Sort on event['dd'], ties resolved by ident.
    # Replace spaces with a high-value Unicode character for sorting.
    # ('YYYY tbd' will come after any specific date in year YYYY.)
    t0 = str(item[1].get('dd',''))+' '+str(item[0])
    return t0.replace(' ','\uffff')

def check_pair(key,value,ident):
    # Return a list of errors
    errors = []
    if key not in SetRK:
        errors.append(f'Event {ident} contains unrecognized key: {key}')
    if not isinstance(value,str):
        errors.append(f'Event {ident} contains invalid value: {value}')
    return errors

def check_event(ident,event):
    # Return a list of errors
    if not isinstance(event,dict):
        return [f'Event {ident} is not a dictionary']
    if not SetMK <= event.keys():
        return [f'Event {ident} is missing a mandatory key']
    errors = []
    for key, value in event.items():
        errors.extend(check_pair(key,value,ident))
    return errors

def check_update(ident,update):
    # Return a list of errors
    if not isinstance(update,dict):
        return [f'Update {ident} is not a dictionary']
    errors = []
    for key, value in update.items():
        errors.extend(check_pair(key,value,ident))
    return errors

def check_calendar(calendar):
    # Return a list of errors
    if not isinstance(calendar,dict):
        return ['Calendar is not a dict']
    errors = []
    for ident, event in calendar.items():
        errors.extend(check_event(ident,event))
    return errors

def read_yml_dict(f):
    try:
        dic = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f'YAML parsing error: {str(e)}')
        return {}
    if not dic:
        print(f'Warning: Input file content is Null')
        return {}
    elif not isinstance(dic,dict):
        print(f'Warning: Input file is not a dict')
        return {}
    else:
        return dic

def dump(data,f):
    # My specialized version of yaml.safe_dump
    yaml.safe_dump(data, f, allow_unicode=True,
                   width=999, sort_keys=False)

def event_yaml_to_md(name,event,hl):
    # Generate a Markdown entry for calendar item event, highlight if hl.
    dd = event.get('dd','')
    link = event.get('link','')
    exc = event.get('excerpt','')
    if link and exc:
        a0 = '['+name+']('+link+' "'+exc+'")'
    elif link:
        a0 = '['+name+']('+link+')'
    else:
        a0 = name
    if (loc := event.get('loc','')):
        a = dd+': '+a0+', '+loc
    else:
        a = dd+': '+a0
    if (more := event.get('more','')):
        b = '. '+more.rstrip('.')+'.'
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
#     return sorted(main.items(), key = lambda item: sort_key(item))

def page_yaml_to_md(main,highlights,TODAY):
    # Generate Markdown entries for a page.
    # Entries in main and in new are sorted differently.
    past_md = []
    future_md = []
    highlights_md = []
    # new_md = []
    for ident, event in main.items():
        hl = ident in highlights
        name = event.get('name',ident)
        xmd = event_yaml_to_md(name,event,hl)
        if str(event['dd']).replace(' ','\uffff') < TODAY:
            past_md.append(xmd)
        else:
            future_md.append(xmd)
            if hl:
                highlights_md.append(xmd)
#   for ident in new:
#       if ident in main.keys():
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
        if (kw := event.get('kw','')):
            for y1 in kw.split(','):
                pages_extend(key,y1,pages)
    return pages
