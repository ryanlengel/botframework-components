import sys
import random

if len(sys.argv) != 4:
    print("error argument")
    exit(1)

infile = sys.argv[1]
trainfile = open(sys.argv[2], "w")
rate = float(sys.argv[3])

last = False
min_len = 10000
max_len = 0
for line in open(infile):
    if last == True:
        if line.startswith("-"):
            count+=1
        else:
            min_len = min(count, min_len)
            max_len = max(count, max_len)
            count = 0
            last = False
    else:
        if line.startswith("#"):
            last = True
        count = 0
print(max_len)
print(min_len)

last = False
utterances = []
for line in open(infile):
    if last == True:
        if line.startswith("-"):
            utterances.append(line)
        else:
            if len(utterances) > 0:
                pos = min_len * rate
                for i in range(0, len(utterances)):
                    if i < pos:
                        trainfile.write(utterances[i])
            last = False
            utterances = []
            trainfile.write("\n")
    else:
        if line.startswith("#"):
            last = True
        trainfile.write(line)

trainfile.close()