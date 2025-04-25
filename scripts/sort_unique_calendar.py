import sys
import yaml

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

unique_data = remove_duplicates(yaml.safe_load(sys.stdin))
sorted_unique = sorted(unique_data, key=sort_key)

yaml.safe_dump(sorted_unique, sys.stdout,
               allow_unicode=True, width=999, sort_keys=False)
