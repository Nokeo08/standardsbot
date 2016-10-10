#!/usr/bin/python
# -*- coding: utf-8 -*-

from standards.WLC import getWLC
from standards.WSC import getWSC
from standards.HC import getHC
from standards.BC import getBC
from standards.WCF import getWCF, parseWCFArgs
import re
import datetime

def log(msg):
    print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ": " +msg + "\n", flush=True)

def parseArgs(numGroups):
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

def fetchCitations(citations):
    malformed = False
    footer = "\n\n***\n[^Code](https://github.com/Nokeo08/standardsbot) ^| [^Contact ^Dev](/message/compose/?to=nokeo08) ^| [^Usage](https://github.com/Nokeo08/standardsbot/blob/master/README.md#usage) ^| [^Changelog](https://github.com/Nokeo08/standardsbot/blob/master/CHANGELOG.md) ^| [^Find ^a ^problem? ^Submit ^an ^issue.](https://github.com/Nokeo08/standardsbot/issues)"
    citation = ''
    result = ''
    if citations:
        westminsterLarger = re.findall(r"\[\s*(?:W|Westminster)\s*(?:L|Larger)\s*(?:C|Catechism)\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        westminsterShorter = re.findall(r"\[\s*(?:W|Westminster)\s*(?:S|Shorter)\s*(?:C|Catechism)\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        heidelberg = re.findall(r"\[\s*(?:H|Heidelberg)\s*(?:C|Catechism)?\s*(?:(?:Q|Question)\s*(?:and|&)\s*(?:A|Answer))?\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        belgic = re.findall(r"\[\s*(?:B|Belgic)?\s*(?:C|Confession)\s*(?:of)?\s*(?:F|Faith)\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        westminster = re.findall(r"\[\s*(?:W|Westminster)?\s*(?:C|Confession)\s*(?:of)?\s*(?:F|Faith)\s*([\d\,\-\:\s]+)\]", citations, re.IGNORECASE)

        if westminsterLarger:
            tempResult = ''
            citation += '[WLC '
            args, temp = parseArgs(westminsterLarger)
            malformed |= temp
            for i in args:
                citation += str(i[0]) + '-' + str(i[1])+","
                quote, temp = getWLC(i[0], i[1])
                malformed |= temp
                if tempResult:
                    tempResult += quote
                elif quote:
                    tempResult = "\n**Westmintser Larger Catechism**\n" + quote
            citation = citation[:-1] + "]"
            result += tempResult
        if westminsterShorter:
            tempResult = ''
            citation += '[WSC '
            args, temp = parseArgs(westminsterShorter)
            malformed |= temp
            for i in args:
                citation += str(i[0]) + '-' + str(i[1])+","
                quote, temp = getWSC(i[0], i[1])
                malformed |= temp
                if tempResult:
                    tempResult += quote
                elif quote:
                    tempResult = "\n**Westminster Shorter Catechism**\n" + quote
            citation = citation[:-1] + "]"
            result += tempResult
        if heidelberg:
            tempResult = ''
            citation += '[HC '
            args, temp = parseArgs(heidelberg)
            malformed |= temp
            for i in args:
                citation += str(i[0]) + '-' + str(i[1])+","
                quote, temp = getHC(i[0], i[1])
                malformed |= temp
                if tempResult:
                    tempResult += quote
                elif quote:
                    tempResult += "\n**Heidelberg Catechism**\n" + quote
            citation = citation[:-1] + "]"
            result += tempResult
        if belgic:
            tempResult = ''
            citation += '[BCF '
            args, temp = parseArgs(belgic)
            malformed |= temp
            for i in args:
                citation += str(i[0]) + '-' + str(i[1])+","
                quote, tamp = getBC(i[0], i[1])
                malformed |= temp
                if tempResult:
                    tempResult += quote
                elif quote:
                    tempResult += "\n**Belgic Confession of Faith**\n" + quote
            citation = citation[:-1] + "]"
            result += tempResult
        if westminster:
            tempResult = ''
            citation += '[WCF '
            args, temp = parseWCFArgs(westminster)
            malformed |= temp
            for i in args:
                citation += str(i[0]) + ':' + str(i[1])+ "-" + str(i[2]) + ':' + str(i[3]) + ", "
                quote, temp = getWCF(i[0], i[1], i[2], i[3])
                malformed |= temp
                if tempResult:
                    tempResult += quote
                elif quote:
                    tempResult += "\n**Westminster Confession of Faith**\n" + quote
            citation = citation[:-1] + "]"
            result += tempResult


        if malformed:
            result += "\n\n**Your request contained one or more malformed requests that I could not fulfill.**"

        if len(result) > 0:
            if len(result) > 9500:
                result = "Citation contains more than the maximum number characters allowed in a comment."
                citation += " Comment overflow"
            result += footer
        return (result, citation)
