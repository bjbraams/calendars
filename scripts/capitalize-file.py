import sys
from titlecase import titlecase

while line := sys.stdin.readline():
    print(titlecase(line[:-1]))
