def oneToOneParser(numGroups):
    malformed = False
    result = []
    for numGroup in numGroups:
        args = numGroup.split(",")
        for i in args:
            i = "".join(i.split())
            if '-' not in i and i.isdigit():
                result.append([int(i), int(i)])
            elif '-' not in i and not i.isdigit():
                malformed = True
            elif '-' in i:
                split = i.split("-")
                if len(split) == 2 and split[0].isdigit() and split[1].isdigit() and int(split[0]) < int(split[1]):
                    result.append([int(split[0]), int(split[1])])
                elif not split[0].isdigit() or not split[1].isdigit():
                    malformed = True
                else:
                    malformed = True
            else:
                malformed = True
    return result, malformed

def chapterParagraphParser(numGroups):
    malformed = False
    result = []
    for numGroup in numGroups:
        args = numGroup.split(",")
        for i in args:
            i = "".join(i.split())
            if '-' in i:
                split = i.split('-')
                if len(split) == 2 and ':' in split[0]:
                    leftSplit = split[0].split(':')
                    if len(leftSplit) == 2 and leftSplit[0].isdigit() and leftSplit[1].isdigit():
                        if ':' in split[1]:
                            rightSplit = split[1].split(':')
                            if len(rightSplit) == 2 and rightSplit[0].isdigit() and rightSplit[1].isdigit():
                                result.append([int(leftSplit[0]), int(leftSplit[1]), int(rightSplit[0]), int(rightSplit[1])]) #1:2-3:4
                            else:
                                malformed = True
                        elif split[1].isdigit():
                            result.append([int(leftSplit[0]), int(leftSplit[1]), int(leftSplit[0]), int(split[1])]) #5:6-7
                        else:
                            malformed = True
                    else:
                        malformed = True
                else:
                    malformed = True
            else:
                if ':' in i:
                    split = i.split(":")
                    if len(split) == 2 and split[0].isdigit() and split[1].isdigit():
                        result.append([int(split[0]), int(split[1]), int(split[0]), int(split[1])]) # 8:9
                    else:
                        malformed = True
                else:
                    malformed = True
    return result, malformed
