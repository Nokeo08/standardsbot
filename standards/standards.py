#!/usr/bin/python
# -*- coding: utf-8 -*-

from .parsers import oneToOneParser, chapterParagraphParser
import standards.text as stds
import re


class standards:

    wlcRegex = r"\[\s*(?:W|Westminster)\s*(?:L|Larger)\s*(?:C|Catechism)\s*([\d\-,\s]+)\s*\]"
    wscRegex = r"\[\s*(?:W|Westminster)\s*(?:S|Shorter)\s*(?:C|Catechism)\s*([\d\-,\s]+)\s*\]"
    hcRegex = r"\[\s*(?:H|Heidelberg)\s*(?:C|Catechism)\s*(?:(?:Q|Question)\s*(?:and|&)\s*(?:A|Answer))?\s*([\d\-,\s]+)\s*\]"
    bcfRegex = r"\[\s*(?:B|Belgic)\s*(?:C|Confession)\s*(?:(?:of)?\s*(?:F|Faith)\s*)?([\d\-,\s]+)\s*\]"
    wcfRegex = r"\[\s*(?:W|Westminster)\s*(?:C|Confession)\s*(?:of)?\s*(?:F|Faith)\s*([\d\,\-\:\s]+)\]"
    lbcf89Regex = r"\[\s*(?:(?:L|London)\s*(?:B|Baptist)\s*(?:C|Confession)\s*(?:of)?\s*(?:F|Faith))?\s*1689\s*([\d\,\-\:\s]+)\]"
    articlesRegex = r"\[\s*39\s*(?:A|Articles)\s*(?:of\s*(?:R|Religion))?\s*([\d\-,\s]+)\s*\]"

    def __init__(self):
        self.footer = ('\n\n***\n[^Code](https://github.com/Nokeo08/standardsbot) ^|'
                    ' [^Contact ^Dev](/message/compose/?to=nokeo08) ^|'
                    ' [^Usage](https://github.com/Nokeo08/standardsbot/blob/master/README.md#usage) ^|'
                    ' [^Changelog](https://github.com/Nokeo08/standardsbot/blob/master/CHANGELOG.md) ^|'
                    ' [^Find ^a ^problem? ^Submit ^an ^issue.](https://github.com/Nokeo08/standardsbot/issues)')
        self.setup()

    def setup(self):
        self.append('','',False,True)

    def append(self, text, citation='', malformed=False, overwrite=False):
        if overwrite:
            self.text = text
            self.citation = citation
            self.malformed = malformed
        else:
            self.text += text
            self.citation += citation
            self.malformed |= malformed

    def fetch(self, citations):
        self.setup()
        if citations:
            westminsterLarger = re.findall(self.wlcRegex, citations, re.IGNORECASE)
            westminsterShorter = re.findall(self.wscRegex, citations, re.IGNORECASE)
            heidelberg = re.findall(self.hcRegex, citations, re.IGNORECASE)
            belgic = re.findall(self.bcfRegex, citations, re.IGNORECASE)
            westminster = re.findall(self.wcfRegex, citations, re.IGNORECASE)
            lbcf89 = re.findall(self.lbcf89Regex, citations, re.IGNORECASE)
            articles = re.findall(self.articlesRegex, citations, re.IGNORECASE)


            text, citation, malformed = stds.WLC(oneToOneParser).fetch(westminsterLarger)
            self.append(text, citation, malformed)

            text, citation, malformed = stds.WSC(oneToOneParser).fetch(westminsterShorter)
            self.append(text, citation, malformed)

            text, citation, malformed = stds.HC(oneToOneParser).fetch(heidelberg)
            self.append(text, citation, malformed)

            text, citation, malformed = stds.BCF(oneToOneParser).fetch(belgic)
            self.append(text, citation, malformed)

            text, citation, malformed = stds.WCF(chapterParagraphParser).fetch(westminster)
            self.append(text, citation, malformed)

            text, citation, malformed = stds.LBCF89(chapterParagraphParser).fetch(lbcf89)
            self.append(text, citation, malformed)

            text, citation, malformed = stds.ARTICLES(oneToOneParser).fetch(articles)
            self.append(text, citation, malformed)


            if self.malformed:
                self.append("\n\n**Your request contained one or more malformed requests that I could not fulfill.**")

            if len(self.text) > 0:
                if len(self.text) > 9500:
                    self.append("Citation contains more than the maximum number characters allowed in a comment.","Comment overflow", malformed, True)
                self.append(self.footer)
            return (self.text, self.citation, self.malformed)
