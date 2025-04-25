#!/usr/bin/env python3
#
# Part of: https://github.com/bjbraams/calendars.
#
# Description: Processes a YAML calendar file from stdin and reports
# errors.
#
# Expected syntax: The file contains a list of items, each item is
# a dictionary, the keys in the dictionary come from a defined set
# of mandatory and optional keys, and each value is a string.
#
# Common errors:
# - A 'dates' entry is seen as a date and not as a string. In the YAML
# file, a date range is fine, that is recognized as a string. But a
# single date is interpreted as a date, so there quotes must be used.
# - An intended string contains a ": " and YAML sees it as a key-value
# pair. Such a string must be quoted.
# - An intended string starts with an opening square bracket and YAML
# sees it as a list. Such an initial square bracket must be escaped.
# - An intended string starts with "*" or with "!" and this is seen
# as a YAML syntax item. Such a special character must be escaped.
# - Also "- " at the start of an intended string must be escaped.

import sys
import yaml

MANDATORY_KEYS = {'dates','name','loc','pages'}
OPTIONAL_KEYS = {'link','more'}
RECOGNIZED_KEYS = MANDATORY_KEYS|OPTIONAL_KEYS

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

try:
    data = yaml.safe_load(sys.stdin)
    if data is None:
        errors = [f"No valid YAML data provided"]
    else:
        errors = check_calendar(data)
except yaml.YAMLError as e:
    errors = [f"YAML parsing error: {str(e)}"]

for error in errors:
    print(error)
