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
            if '-' not in i:
                if i.isdigit() and self.validChptrNum(int(i)):
                    result.append([int(i), 1, int(i), self.CHPTRMAX[int(i)]]) # (ex: 1)
                elif ":" in i:
                    split = i.split(":")
                    if len(split) != 2:
                        malformed = True
                    elif split[0].isdigit() and split[1].isdigit():
                        result.append([int(split[0]), int(split[1]), int(split[0]), int(split[1])]) # (ex. 2:3)
                    else:
                        malformed = True
                else:
                    malformed = True
            elif '-' in i:
                split = i.split("-")
                if len(split) != 2:
                    malformed = True
                elif ":" not in split[0] and not split[0].isdigit() or ":" not in split[1] and not split[1].isdigit():
                    malformed = True
                elif ":" not in split[0] and split[0].isdigit():
                    if ":" not in split[1] and split[1].isdigit() and self.validChptrNum(int(split[1])):
                        result.append([int(split[0]), 1, int(split[1]), self.CHPTRMAX[int(split[1])]]) # 4-5
                    elif ":" in split[1]:
                        rightSplit = split[1].split(":")
                        if len(rightSplit) != 2:
                            malformed = True
                        elif rightSplit[0].isdigit() and rightSplit[1].isdigit():
                            result.append([int(split[0]), 1, int(rightSplit[0]), int(rightSplit[1])]) # (ex. 6-7:8)
                        else:
                            malformed = True
                    else:
                        malformed = True
                elif ":" in split[0]:
                    leftSplit = split[0].split(":")
                    if len(leftSplit) != 2:
                        malformed = True
                    elif leftSplit[0].isdigit() and leftSplit[1].isdigit():
                        if ":" not in split[1] and split[1].isdigit() and self.validChptrNum(int(split[1])):
                            result.append([int(leftSplit[0]), int(leftSplit[1]), int(split[1]), self.CHPTRMAX[int(split[1])]]) # (ex. 9:10-11)
                        elif ":" in split[1]:
                            rightSplit = split[1].split(":")
                            if len(rightSplit) != 2:
                                malformed = True
                            elif rightSplit[0].isdigit() and rightSplit[1].isdigit():
                                result.append([int(leftSplit[0]), int(leftSplit[1]), int(rightSplit[0]), int(rightSplit[1])]) # 12:13-14:15
                            else:
                                malformed = True
                        else:
                            malformed = True
                    else:
                        malformed = True
                else:
                    malformed = True
            else:
                malformed = True
    return result, malformed
