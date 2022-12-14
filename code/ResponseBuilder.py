#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Standard import Standard
from code.processors.ChapterParagraphProcessor import ChapterParagraphProcessor
from code.processors.OneToOneProcessor import OneToOneProcessor
from code.utils.misc import load_json


class ResponseBuilder:
    def __init__(self):
        self.__standards = {
            Standard("WLC", OneToOneProcessor),
            Standard("WSC", OneToOneProcessor),
            Standard("HC", OneToOneProcessor),
            Standard("BCF", OneToOneProcessor),
            Standard("39A", OneToOneProcessor),
            Standard("95T", OneToOneProcessor),
            Standard("SCOTS", OneToOneProcessor),
            Standard("LBCF46", OneToOneProcessor),
            Standard("SPC", OneToOneProcessor),
            Standard("CSBI", OneToOneProcessor),
            Standard("CCC", OneToOneProcessor),
            Standard("ARM", OneToOneProcessor),
            Standard("WCF", ChapterParagraphProcessor),
            Standard("LBCF89", ChapterParagraphProcessor),
            Standard("CDA", ChapterParagraphProcessor),
            Standard("CDR", ChapterParagraphProcessor),
            Standard("AC", ChapterParagraphProcessor),
            Standard("SHC", ChapterParagraphProcessor)
        }
        self.__text = ''
        self.__citation = ''
        self.__malformed = False
        self.__footer = ('\n\n***\n'
                         ' [^(Code: v' + load_json("conf")["VERSION"] + ')](https://github.com/Nokeo08/standardsbot) ^|'
                         ' [^(Contact Dev)](/message/compose/?to=nokeo08) ^|'
                         ' [^(Usage)](https://github.com/Nokeo08/standardsbot/blob/master/README.md) ^|'
                         ' [^(Changelog)](https://github.com/Nokeo08/standardsbot/blob/master/docs/CHANGELOG.md) ^|'
                         ' [^(Find a problem? Submit an issue.)](https://github.com/Nokeo08/standardsbot/issues)')

    def __reset(self):
        self.__append('', '', False, True)

    def __append(self, text, citation='', malformed=False, overwrite=False):
        if overwrite:
            self.__text = text
            self.__citation = citation
            self.__malformed = malformed
        else:
            self.__text += text
            self.__citation += citation
            self.__malformed |= malformed

    def __append_response(self, response):
        if len(response) != 3:
            raise NotImplementedError
        self.__append(response[0], response[1], response[2])

    def fetch(self, citations):
        self.__reset()
        if citations:
            for standard in self.__standards:
                self.__append_response(standard.fetch(citations))

            if self.__malformed:
                self.__append("\n\n**Your request contained one or more malformed requests that I could not fulfill.**")

            if len(self.__text) > 0:
                if len(self.__text) > 9500:
                    self.__append(
                        "Citation contains more than the maximum number characters allowed in a comment.",
                        "Comment overflow",
                        False,
                        True
                    )
                self.__append(self.__footer)
            return self.__text, self.__citation, self.__malformed
