import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]
outfile = open(outfilename, "w")
flag = False
for line in open(infilename):
    if line.startswith("# _Interruption"):
        flag = True
    elif flag == True and line.startswith("-"):
        pass 
    else:
        flag = False
        outfile.write(line)
outfile.close()