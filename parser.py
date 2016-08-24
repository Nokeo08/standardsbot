#!/usr/bin/python
# -*- coding: utf-8 -*-

from WLC import getWLC
from WSC import getWSC
from HC import getHC
from BC import getBC
import re

malformed = False

def parseArgs(numGroups):
    global malformed
    result = []
    for numGroup in numGroups:
        args = numGroup.split(",")
        for i in args:
            i = "".join(i.split())
            if len(i) == 1 and i.isdigit():
                result.append([int(i), int(i)])
            elif not i.isdigit():
                malformed = True
            elif '-' in i:
                split = i.split("-")
                if len(split) == 2 and split[0].isdigit() and split[1].isdigit() and int(split[0]) < int(split[1]):
                    result.append([int(split[0]), int(split[1])])
                elif not split[0].isdigit() or not split[1].isdigit():
                    malformed = True


    return result

def fetchCitations(citations):
    global malformed
    result = ''
    wlcResult = None
    wscResult = None
    hcResult = None
    bcResult = None
    if citations:
        westminsterLarger = re.findall(r"\[\s*WLC\s*(.*?)\]", citations, re.IGNORECASE)
        westminsterShorter = re.findall(r"\[\s*WSC\s*(.*?)\]", citations, re.IGNORECASE)
        heidelberg = re.findall(r"\[\s*HC\s*(.*?)\]", citations, re.IGNORECASE)
        belgic = re.findall(r"\[\s*BC\s*(.*?)\]", citations, re.IGNORECASE)

        if westminsterLarger:
            args = parseArgs(westminsterLarger)
            for i in args:
                quote = getWLC(i[0], i[1])
                if wlcResult:
                    wlcResult = result + quote if quote else wlcResult
                elif quote:
                    wlcResult = "\n**Westminser Larger Catechism**\n" + quote
        if westminsterShorter:
            args = parseArgs(westminsterShorter)
            for i in args:
                quote = getWSC(i[0], i[1])
                if wscResult:
                    wscResult = result + quote if quote else wscResult
                elif quote:
                    wscResult = "\n**Westminser Shorter Catechism**\n" + quote
        if heidelberg:
            args = parseArgs(heidelberg)
            for i in args:
                quote = getHC(i[0], i[1])
                if hcResult:
                    hcResult = hcResult + quote if quote else hcResult
                elif quote:
                    hcResult = "\n**Heidelberg Catechism**\n" + quote
        if belgic:
            args = parseArgs(belgic)
            for i in args:
                quote = getBC(i[0], i[1])
                if bcResult:
                    bcResult = bcResult + quote if quote else bcResult
                elif quote:
                    bcResult = "\n**Belgic Confession**\n" + quote

        result = wlcResult if wlcResult else result
        result = result + wscResult if wscResult else result
        result = result + hcResult if hcResult else result
        result = result + bcResult if bcResult else result

        if malformed:
            result = result + "\n\n^**Your request contained one or more malformed requests that I could not fulfill.**"
            malformed = False

        if len(result) > 0:
            print(result)
            return result
