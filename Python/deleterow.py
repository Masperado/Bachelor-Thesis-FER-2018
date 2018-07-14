import os

with open('debateNew.csv','w') as tmp:

    with open('debatereligion.csv','r') as infile:
        for linenumber, line in enumerate(infile):
            quote=False
            if (line.startswith('"')):
                line = line[1:]
                if not '"' in line:
                    print(linenumber/36383782)
                    continue
                indexOfSecond = line.index('"')+2
                line = line[indexOfSecond:]
                quote=True
            if '"' in line:
                print(linenumber/36383782)
                continue
            columns = line.split(",")
            if len(columns)==20:
                tmp.write(line)
            elif len(columns)==19:
                if (quote):
                    tmp.write(line)
            else:
                print(linenumber/36383782)
