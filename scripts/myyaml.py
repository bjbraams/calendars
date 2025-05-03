import yaml
from titlecase import titlecase

MANDATORY_KEYS = {'dd','name','loc','kw'}
OPTIONAL_KEYS = {'link','more'}
RECOGNIZED_KEYS = MANDATORY_KEYS|OPTIONAL_KEYS

def capitalize(event):
    event['name'] = titlecase(event['name'])

def sort_key(event):
    # Sort on dd, ties resolved by event name.
    # Replace spaces with a high-value Unicode character for sorting.
    # ("YYYY tbd" will come after any specific date in year YYYY.)
    s = str(event['dd'])+str(event['name'])
    return s.replace(' ', '\uffff')

def remove_duplicates(data):
    seen = set()
    unique = []
    for event in data:
        t0 = tuple(sorted(event.items()))
        if t0 not in seen:
            seen.add(t0)
            unique.append(event)
    return unique

def sorted_unique(data):
    return sorted(remove_duplicates(data), key=sort_key)

def check_pair(key,value,index):
    # Return a list of errors
    errors = []
    if key not in RECOGNIZED_KEYS:
        errors.append(f"Event {index} contains invalid key: {key}")
    if not isinstance(value,str):
        errors.append(f"Event {index} contains invalid value: {value}")
    return errors

def check_event(event,index):
    # Return a list of errors
    if not isinstance(event,dict):
        return [f"Event {index} is not a dictionary"]
    if not MANDATORY_KEYS <= event.keys():
        return [f"Event {index} is missing a mandatory key"]
    errors = []
    for key, value in event.items():
        errors.extend(check_pair(key,value,index))
    return errors

def check_calendar(calendar):
    # Return a list of errors
    if not isinstance(calendar,list):
        return ["Calendar is not a list"]
    errors = []
    for index, event in enumerate(calendar):
        errors.extend(check_event(event,index))
    return errors

def dump(data,fn):
    # My specialized version of yaml.safe_dump
    yaml.safe_dump(data, fn, allow_unicode=True,
                   width=999, sort_keys=False)
