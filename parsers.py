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

