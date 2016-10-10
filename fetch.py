#!/usr/bin/python
# -*- coding: utf-8 -*-

from parsers import oneToOneParser
from standards.WLC import WLC
from standards.WSC import WSC
from standards.HC import HC
from standards.BC import BC
from standards.WCF import getWCF, parseWCFArgs
import re
import datetime

def log(msg):
    print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ": " +msg + "\n", flush=True)

def fetchCitations(citations):
    footer = "\n\n***\n[^Code](https://github.com/Nokeo08/standardsbot) ^| [^Contact ^Dev](/message/compose/?to=nokeo08) ^| [^Usage](https://github.com/Nokeo08/standardsbot/blob/master/README.md#usage) ^| [^Changelog](https://github.com/Nokeo08/standardsbot/blob/master/CHANGELOG.md) ^| [^Find ^a ^problem? ^Submit ^an ^issue.](https://github.com/Nokeo08/standardsbot/issues)"
    result = ''
    citation = ''
    malformed = False

    if citations:
        westminsterLarger = re.findall(r"\[\s*(?:W|Westminster)\s*(?:L|Larger)\s*(?:C|Catechism)\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        westminsterShorter = re.findall(r"\[\s*(?:W|Westminster)\s*(?:S|Shorter)\s*(?:C|Catechism)\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        heidelberg = re.findall(r"\[\s*(?:H|Heidelberg)\s*(?:C|Catechism)?\s*(?:(?:Q|Question)\s*(?:and|&)\s*(?:A|Answer))?\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        belgic = re.findall(r"\[\s*(?:B|Belgic)?\s*(?:C|Confession)\s*(?:of)?\s*(?:F|Faith)\s*([\d\-,\s]+)\s*\]", citations, re.IGNORECASE)
        westminster = re.findall(r"\[\s*(?:W|Westminster)?\s*(?:C|Confession)\s*(?:of)?\s*(?:F|Faith)\s*([\d\,\-\:\s]+)\]", citations, re.IGNORECASE)
        
        if westminsterLarger:
            tempResult, tempCitation, tempMalformed = WLC(oneToOneParser).fetch(westminsterLarger)
            result += tempResult
            citation += tempCitation
            malformed |= tempMalformed
        if westminsterShorter:
            tempResult, tempCitation, tempMalformed = WSC(oneToOneParser).fetch(westminsterShorter)
            result += tempResult
            citation += tempCitation
            malformed |= tempMalformed
        if heidelberg:
            tempResult, tempCitation, tempMalformed = HC(oneToOneParser).fetch(heidelberg)
            result += tempResult
            citation += tempCitation
            malformed |= tempMalformed
        if belgic:
            tempResult, tempCitation, tempMalformed = BC(oneToOneParser).fetch(belgic)
            result += tempResult
            citation += tempCitation
            malformed |= tempMalformed 
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
                citation = "Comment overflow"
            result += footer
        return (result, citation)
