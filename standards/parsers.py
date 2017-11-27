def one_to_one_parser(num_groups):
    malformed = False
    result = []
    for numGroup in num_groups:
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


def chapter_paragraph_parser(num_groups):
    malformed = False
    result = []
    for numGroup in num_groups:
        args = numGroup.split(",")
        for i in args:
            i = "".join(i.split())
            if '-' in i:
                split = i.split('-')
                if len(split) == 2 and ':' in split[0]:
                    left_split = split[0].split(':')
                    if len(left_split) == 2 and left_split[0].isdigit() and left_split[1].isdigit():
                        if ':' in split[1]:
                            right_split = split[1].split(':')
                            if len(right_split) == 2 and right_split[0].isdigit() and right_split[1].isdigit():
                                result.append([int(left_split[0]),
                                               int(left_split[1]),
                                               int(right_split[0]),
                                               int(right_split[1])])  # 1:2-3:4
                            else:
                                malformed = True
                        elif split[1].isdigit():
                            result.append([int(left_split[0]),
                                           int(left_split[1]),
                                           int(left_split[0]),
                                           int(split[1])])  # 5:6-7
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
                        result.append([int(split[0]),
                                       int(split[1]),
                                       int(split[0]),
                                       int(split[1])])  # 8:9
                    else:
                        malformed = True
                else:
                    malformed = True
    return result, malformed
