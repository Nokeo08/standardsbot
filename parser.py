#!/usr/bin/python
# -*- coding: utf-8 -*-

from standards.WLC import getWLC
from standards.WSC import getWSC
from standards.HC import getHC
from standards.BC import getBC
from standards.WCF import getWCF, parseWCFArgs
import re
import datetime

malformed = False

def log(msg):
    print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ": " +msg + "\n", flush=True)
    # with open('log.out', "a") as f:
    #     f.write(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ": " +msg + "\n")

def parseArgs(numGroups):
    global malformed
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
    return result

def fetchCitations(citations):
    global malformed
    footer = "\n\n***\n[^Code](https://github.com/Nokeo08/standardsbot) ^| [^Contact ^Dev](/message/compose/?to=nokeo08) ^| [^Usage](https://github.com/Nokeo08/standardsbot/blob/master/README.md#usage) ^| [^Changelog](https://github.com/Nokeo08/standardsbot/blob/master/CHANGELOG.md) ^| [^Find ^a ^problem? ^Submit ^an ^issue.](https://github.com/Nokeo08/standardsbot/issues)"
    resultCitation = ''
    result = ''
    wlcCitation = wlcResult = wscCitation = wscResult = hcCitation = hcResult = bcCitation = bcResult = wcfCitation = wcfResult = None
    if citations:
        westminsterLarger = re.findall(r"\[\s*(?:W|Westminster)\s*(?:L|Larger)\s*(?:C|Catechism)\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        westminsterShorter = re.findall(r"\[\s*(?:W|Westminster)\s*(?:S|Shorter)\s*(?:C|Catechism)\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        heidelberg = re.findall(r"\[\s*(?:H|Heidelberg)\s*(?:C|Catechism)?\s*(?:(?:Q|Question)\s*(?:and|&)\s*(?:A|Answer))?\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        belgic = re.findall(r"\[\s*(?:B|Belgic)?\s*(?:C|Confession)\s*(?:of)?\s*(?:F|Faith)\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        westminster = re.findall(r"\[\s*(?:W|Westminster)?\s*(?:C|Confession)\s*(?:of)?\s*(?:F|Faith)\s*([\d\,\-\:\s]+)\]", citations, re.IGNORECASE)

        if westminsterLarger:
            wlcCitation = '[WLC '
            args = parseArgs(westminsterLarger)
            for i in args:
                wlcCitation = wlcCitation + str(i[0]) + '-' + str(i[1])+","
                quote = getWLC(i[0], i[1])
                if wlcResult:
                    wlcResult = wlcResult + quote if quote else wlcResult
                elif quote:
                    wlcResult = "\n**Westmintser Larger Catechism**\n" + quote
            wlcCitation = wlcCitation + "]"
        if westminsterShorter:
            wscCitation = '[WSC '
            args = parseArgs(westminsterShorter)
            for i in args:
                wscCitation = wscCitation + str(i[0]) + '-' + str(i[1])+","
                quote = getWSC(i[0], i[1])
                if wscResult:
                    wscResult = wscResult + quote if quote else wscResult
                elif quote:
                    wscResult = "\n**Westminster Shorter Catechism**\n" + quote
            wscCitation = wscCitation + "]"
        if heidelberg:
            hcCitation = '[HC '
            args = parseArgs(heidelberg)
            for i in args:
                hcCitation = hcCitation + str(i[0]) + '-' + str(i[1])+","
                quote = getHC(i[0], i[1])
                if hcResult:
                    hcResult = hcResult + quote if quote else hcResult
                elif quote:
                    hcResult = "\n**Heidelberg Catechism**\n" + quote
            hcCitation = hcCitation + "]"
        if belgic:
            bcCitation = '[BCF '
            args = parseArgs(belgic)
            for i in args:
                bcCitation = bcCitation + str(i[0]) + '-' + str(i[1])+","
                quote = getBC(i[0], i[1])
                if bcResult:
                    bcResult = bcResult + quote if quote else bcResult
                elif quote:
                    bcResult = "\n**Belgic Confession of Faith**\n" + quote
            bcCitation = bcCitation + "]"
        if westminster:
            wcfCitation = '[WCF '
            args = parseWCFArgs(westminster)
            for i in args:
                wcfCitation = wcfCitation + str(i[0]) + ':' + str(i[1])+ "-" + str(i[2]) + ':' + str(i[3]) + ", "
                quote = getWCF(i[0], i[1], i[2], i[3])
                if wcfResult:
                    wcfResult = wcfResult + quote if quote else wcfResult
                elif quote:
                    wcfResult = "\n**Westminster Confession of Faith**\n" + quote
            wcfCitation = wcfCitation + "]"

        result = wlcResult if wlcResult else result
        result = result + wscResult if wscResult else result
        result = result + hcResult if hcResult else result
        result = result + bcResult if bcResult else result
        result = result + wcfResult if wcfResult else result

        resultCitation = wlcCitation if wlcCitation else resultCitation
        resultCitation = resultCitation + wscCitation if wscCitation else resultCitation
        resultCitation = resultCitation + hcCitation if hcCitation else resultCitation
        resultCitation = resultCitation + bcCitation if bcCitation else resultCitation
        resultCitation = resultCitation + wcfCitation if wcfCitation else resultCitation

        if malformed:
            result = result + "\n\n**Your request contained one or more malformed requests that I could not fulfill.**"
            malformed = False

        if len(result) > 0:
            if len(result) > 9500:
                result = "Citation contains more than the maximum number characters allowed in a comment."
                resultCitation = "Ccomment overflow"
            result = result + footer
        return (result, resultCitation)
