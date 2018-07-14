with open('liwc7clean.csv','w') as tmp:
    with open('liwc7.csv','r',encoding="utf-8") as infile:
        firstRow=True
        for linenumber, line in enumerate(infile):
            line = line[:-1]
            lineSplit = line.split(",")
            splitLine = lineSplit[::-1]
            authorName = lineSplit[0]
            if (authorName.startswith('"')):
                authorName = authorName[1:]
                indexOfSecond = authorName.index('"')
                authorName = authorName[:indexOfSecond]
            splitLine.insert(0,authorName)

            if (firstRow):
                for i in range(0,len(splitLine)):
                    splitLine[i]="LIWC_"+splitLine[i]
                firstRow = False
            tmp.write(", ".join(splitLine[0:93]))
            tmp.write("\n")


            #
            # if (line.startswith('"')):
            #     line = line[1:]
            #     if not '"' in line:
            #         print(linenumber/36383782)
            #         continue
            #     indexOfSecond = line.index('"')+2
            #     line = line[indexOfSecond:]
            #     quote=True
            # if '"' in line:
            #     print(linenumber/36383782)
            #     continue
            # columns = line.split(",")
            # if len(columns)==20:
            #     tmp.write(line)
            # elif len(columns)==19:
            #     if (quote):
            #         tmp.write(line)
            # else:
            #     print(linenumber/36383782)