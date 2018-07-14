import os

with open('finalNewNew.csv','w') as tmp:

    with open('finalNew.csv','r') as infile:
        for linenumber, line in enumerate(infile):           # if (linenumber==4668986):
            # if ("Has your friend read the book of Job?" in line):
            #     print(line)
            #     print(linenumber)
            #     print(linenumber)
            #     print(line)
            if (linenumber>3537400 and linenumber<3537420):
                print(line)
                print(linenumber)

