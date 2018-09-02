#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from code.utils import parsers
from code.processors.StandardsProcessor import StandardsProcessor


class ChapterParagraphProcessor(StandardsProcessor):

    def __init__(self, data):
        self.__regex = data["regex"]
        self.__text = data["text"]
        self.__max = data["max"]
        self.__chptr_max = data["chptr_max"]
        self.__abv = data["abv"]
        self.__title = data["title"]

    def __pull_text(self, from_chptr, from_para, to_chptr, to_para):
        if (0 < from_chptr <= to_chptr <= self.__max) and \
                (0 < from_para <= self.__chptr_max[str(from_chptr)]) and \
                (0 < to_para <= self.__chptr_max[str(to_chptr)]):
            result = ''
            for chptr_num in range(from_chptr, to_chptr + 1):
                result += self.__text[str(chptr_num)]["0"]
                for para_num in range(from_para if chptr_num == from_chptr else 1,
                                      to_para + 1 if chptr_num == to_chptr else self.__chptr_max[str(chptr_num)] + 1):
                    result += self.__text[str(chptr_num)][str(para_num)]
            return result, False
        else:
            return '', True

    def fetch(self, full_citations):
        response_text = ''
        response_citation = ''
        response_is_malformed = False

        if full_citations:
            citations = re.findall(self.__regex, full_citations, re.IGNORECASE)
            if citations:
                response_citation = "[" + self.__abv + " "
                args, response_is_malformed = parsers.chapter_paragraph_parser(citations)
                for i in args:
                    response_citation += str(i[0]) + ':' + str(i[1]) + "-" + str(i[2]) + ':' + str(i[3]) + ", "
                    quote, temp = self.__pull_text(i[0], i[1], i[2], i[3])
                    response_is_malformed |= temp
                    if response_text:
                        response_text += quote
                    elif quote:
                        response_text += "\n**" + self.__title + "**\n" + quote
                response_citation = response_citation[:-2] + "]"
        return response_text, response_citation, response_is_malformed
