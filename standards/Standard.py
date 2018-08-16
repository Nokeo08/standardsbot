#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.Util import load_json


class Standard(object):

    def __init__(self, name, processor):
        self.p = processor(load_json(name))

    def fetch(self, c):
        return self.p.fetch(c)
