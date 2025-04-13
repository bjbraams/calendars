import sys
import re # for later
def process(a,b,y):
    # entry a+b to dir/y/fn, with formatting
    # dir and fn are global variables
    if "*" in y:
        format0 = "**"
        format1 = "**"
        y1 = y.replace("*","")
    else:
        format0 = ""
        format1 = ""
        y1 = y
    if y1 not in targets.keys():
        try:
            targets[y1] = open(dir+"/"+y1+"/"+fn+".md", "w")
        except:
            print ("not found: "+dir+"/"+y1+"/")
            targets[y1] = None
    if targets[y1]:
        targets[y1].write(format0+a+format1+b+"\n\n")
fn = sys.argv[1]
dir = "_includes"
f0 = open("_data"+"/"+fn+".csv")
targets = {}
while line := f0.readline()[:-1]:
    x = line.split("|")
    if len(x) != 5:
        print(line)
    else:
        a = x[0]+": "+x[1]
        b = ", "+x[2]+(". "+x[3] if x[3] else "")+"."
        for y in x[-1].split(","):
            process(a,b,y)
