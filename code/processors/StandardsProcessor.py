#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class StandardsProcessor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def fetch(self, full_citations):
        pass
