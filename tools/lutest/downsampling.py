import sys
import random

if len(sys.argv) != 4:
    print("error argument")
    exit(1)
# print(sys.argv)

infile = sys.argv[1]
trainfile = open(sys.argv[2], "w")
rate = float(sys.argv[3])

last = False
utterances = []
for line in open(infile):
    if last == True:
        if line.startswith("-"):
            utterances.append(line)
        else:
            if len(utterances) > 0:
                #random.shuffle(utterances)
                pos = len(utterances) * rate
                for i in range(0, len(utterances)):
                    if i < pos:
                        trainfile.write(utterances[i])
            last = False
            utterances = []
            trainfile.write("\n")
    else:
        if line.startswith("# _Interruption"):
            last = True
        trainfile.write(line)

trainfile.close()