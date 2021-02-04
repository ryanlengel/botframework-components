import sys
import random

if len(sys.argv) != 4:
    print("error argument")
    exit(1)
# print(sys.argv)

infile = sys.argv[1]
trainfile = open(sys.argv[2], "w")
testfile = open(sys.argv[3], "w")

last = False
utterances = []
for line in open(infile):
    # line = line.strip()
    if last == True:
        if line.startswith("-"):
            utterances.append(line)
        else:
            if len(utterances) > 0:
                random.shuffle(utterances)
                pos = len(utterances) * 0.8
                for i in range(0, len(utterances)):
                    if i < pos:
                        trainfile.write(utterances[i])
                    else:
                        testfile.write(utterances[i])
            last = False
            utterances = []
            trainfile.write("\n")
            testfile.write("\n")
    else:
        if line.startswith("#"):
            last = True
        trainfile.write(line)
        testfile.write(line)

trainfile.close()
testfile.close()
