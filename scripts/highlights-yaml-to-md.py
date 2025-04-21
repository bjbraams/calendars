import sys
import yaml
import re # for later

def process(a,b,y):
    # entry a+b to dir/y/fn only for highlights
    # dir, fn and targets are global variables
    format0 = '**'
    format1 = '**'
    if y not in targets.keys():
        try:
            targets[y] = open(dir+'/'+y+'/'+fn+'.md', 'w')
        except:
            print ('not found: '+dir+'/'+y+'/')
            targets[y] = None
    if targets[y]:
        targets[y].write(format0+a+format1+b+'\n\n')

dir = '_includes'
fn = 'highlights'
data = yaml.safe_load(sys.stdin)
targets = {} # Dictionary entries will be <filename>:<file>.

for x in data:
    if 'link' in x.keys() and x['link']:
        a = x['dates']+': ['+x['name']+']('+x['link']+'), '+x['loc']
    else:
        a = x['dates']+': '+x['name']+', '+x['loc']
    if 'more' in x.keys() and x['more']:
        b = '. '+x['more']
    else:
        b = '.' 
    for y in x['pages'].split(","):
        if y.strip().startswith('+'):
            process(a,b,y.strip(' +'))
