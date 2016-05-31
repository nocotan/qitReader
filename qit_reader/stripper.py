#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' qitReader
stripper.py

created by @nocotan
'''
from html.parser import HTMLParser


class Stripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip(html):
    s = Stripper()
    s.feed(html)
    return s.get_data()
