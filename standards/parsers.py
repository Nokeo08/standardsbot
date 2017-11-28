def one_to_one_parser(num_groups):
    malformed = False
    result = []
    for numGroup in num_groups:
        args = numGroup.split(",")
        for i in args:
            i = "".join(i.split())
            if '-' not in i:
                if i.isdigit():
                    result.append([int(i), int(i)])  # 1
                else:
                    malformed = True  # a
            else:
                split = i.split("-")
                if len(split) == 2:
                    if split[0].isdigit() and split[1].isdigit():
                        if int(split[0]) < int(split[1]):
                            result.append([int(split[0]), int(split[1])])  # 1-2
                        else:
                            malformed = True  # 2-1
                    else:
                        malformed = True  # a-2, 1-b,
                else:
                    malformed = True  # -, 1-, -2, 1-2-3
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
                if len(split) == 2:
                    if ':' in split[0] or '.' in split[0]:
                        left_split = split[0].split(':') if ':' in split[0] else split[0].split('.')
                        if len(left_split) == 2:
                            if left_split[0].isdigit() and left_split[1].isdigit():
                                if ':' in split[1] or '.' in split[1]:
                                    right_split = split[1].split(':') if ':' in split[1] else split[1].split('.')
                                    if len(right_split) == 2:
                                        if right_split[0].isdigit() and right_split[1].isdigit():
                                            result.append([int(left_split[0]),
                                                           int(left_split[1]),
                                                           int(right_split[0]),
                                                           int(right_split[1])])  # 1:2-2:1, 1.2-2.1
                                        else:
                                            malformed = True  # 1:2-a:1, 1:2-2:b, 1.2-a.1, 1.2-2.b
                                    else:
                                        malformed = True  # 1:2-2:, 1:2-2:1:, 1:2-2:1:2, 1.2-2., 1.2-2.1., 1.2-2.1.2
                                elif split[1].isdigit():
                                    result.append([int(left_split[0]),
                                                   int(left_split[1]),
                                                   int(left_split[0]),
                                                   int(split[1])])  # 1:2-3, 1.2-3
                                else:
                                    malformed = True  # 1:2-a, 1.2-a
                            else:
                                malformed = True  # a:2-2:1, 1:b-2:1, a.2-2.1, 1.b-2.1
                        else:
                            malformed = True  # 1:-2:1, 1:2:-2:1, 1:2:3-2:1, 1.-2.1, 1.2.-2.1, 1.2.3-2.1
                    else:
                        malformed = True  # 1-2:1
                else:
                    malformed = True  # -, 1:1-, -2:1, 1:1-2:1-3:1
            else:
                if ':' in i or '.' in i:
                    split = i.split(":") if ':' in i else i.split('.')
                    if len(split) == 2:
                        if split[0].isdigit() and split[1].isdigit():
                            result.append([int(split[0]),
                                           int(split[1]),
                                           int(split[0]),
                                           int(split[1])])  # 1:2, 1.2
                        else:
                            malformed = True  # a:1, 1:b, a.1, 1.b
                    else:
                        malformed = True  # 1:2:3, 1:, :, 1.2.3, 1., .
                else:
                    malformed = True  # 1
    return result, malformed
