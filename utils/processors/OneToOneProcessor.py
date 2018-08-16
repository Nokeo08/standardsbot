#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from utils import Parsers
from utils.processors.StandardsProcessor import StandardsProcessor


class OneToOneProcessor(StandardsProcessor):

    def __init__(self, data):
        self.__regex = data["regex"]
        self.__text = data["text"]
        self.__max = data["max"]
        self.__abv = data["abv"]
        self.__title = data["title"]

    def __pull_text(self, from_q, to_q):
        if 0 < from_q <= to_q <= self.__max:
            if from_q == to_q:
                return self.__text[str(from_q)][0] + self.__text[str(from_q)][1], False
            if from_q < to_q:
                result = ''
                for q_num in range(from_q, to_q + 1):
                    result += self.__text[str(q_num)][0] + self.__text[str(q_num)][1]
                return result, False
            else:
                return '', True
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
                args, response_is_malformed = Parsers.one_to_one_parser(citations)
                for i in args:
                    response_citation += str(i[0]) + '-' + str(i[1]) + ", "
                    quote, temp = self.__pull_text(i[0], i[1])
                    response_is_malformed |= temp
                    if response_text:
                        response_text += quote
                    elif quote:
                        response_text += "\n**" + self.__title + "**\n" + quote
                response_citation = response_citation[:-2] + "]"
        return response_text, response_citation, response_is_malformed
