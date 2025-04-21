import sys
import yaml
import re # for later

def process(a,b,y):
    # entry a+b to dir/y/fn, with formatting
    # dir, fn and targets are global variables
    if y.strip().startswith('+'):
        format0 = '**'
        format1 = '**'
        y1 = y.strip(' +')
    else:
        format0 = ''
        format1 = ''
        y1 = y.strip()
    if y1 not in targets.keys():
        try:
            targets[y1] = open(dir+'/'+y1+'/'+fn+'.md', 'w')
        except:
            print ('not found: '+dir+'/'+y1+'/')
            targets[y1] = None
    if targets[y1]:
        targets[y1].write(format0+a+format1+b+'\n\n')

dir = '_includes'
fn = sys.argv[1]
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
        process(a,b,y)
