#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.utils.misc import load_json


class Standard:

    def __init__(self, name, processor):
        self._p = processor(load_json("standards/" + name))

    def fetch(self, text):
        return self._p.fetch(text)
