import sys
import random

if len(sys.argv) != 2:
    print("error argument")
    exit(1)
# print(sys.argv)

infile = sys.argv[1]

last = False
intent = ""
utterances = []
for line in open(infile):
    if last == True:
        if line.startswith("-"):
            utterances.append(line)
        else:
            print(intent, len(utterances))
            last = False
            utterances = []
    else:
        if line.startswith("#"):
            last = True
            intent = line.strip()