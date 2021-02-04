import sys

file = sys.argv[1]

for line in open(file):
    if line.startswith("> Utterance pass"):
        print(line.strip())
    elif line.startswith("#"):
        print(line)