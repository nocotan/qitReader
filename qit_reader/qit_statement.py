#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' qitReader
qit_statement.py

created by @nocotan
'''
import sys


class QitStatement():
    def __init__(self):
        self.qit_list = []
        self.root_list = [
                'all_items',
                'follow_items',
                'all_tags',
                'follow_tags',
                ]
        self.all_items_list = []
        self.follow_items_list = []
        self.all_tags_list = []
        self.follow_tags_list = []

    def set_root_list(self):
        self.qit_list = self.root_list

    def set_all_items_list(self):
        self.qit_list = self.all_items_list

    def set_follow_items_list(self):
        self.qit_list = self.follow_items_list

    def set_all_tags_list(self):
        self.qit_list = self.all_tags_list

    def set_follow_tags_list(self):
        self.qit_list = self.follow_tags_list

    def qit_exit(self):
        ''' exit system
        '''
        sys.stdout.write('Bye.\n')
        sys.exit()

    def qit_ls(self, path):
        ''' ls
        '''
        sys.stdout.write('  '.join(self.qit_list))
        sys.stdout.write('\n')

    def qit_cd_list(self, current):
        cdir = current[-1]
        if cdir == '~':
            QitStatement.set_root_list(self)
        elif cdir == 'all_items':
            QitStatement.set_all_items_list(self)
        elif cdir == 'follow_items':
            QitStatement.set_follow_items_list(self)
        elif cdir == 'all_tags':
            QitStatement.set_all_tags_list(self)
        elif cdir == 'follow_tags':
            QitStatement.set_follow_tags_list(self)

    def qit_cd(self, path, statement_line):
        ''' cd
        '''
        cmd_count = len(statement_line)
        current = path.split('/')
        if cmd_count == 1:
            QitStatement.set_root_list(self)
            return '~'
        elif statement_line[1] == '..':
            if len(current) == 1:
                return '~'
            else:
                current.pop()
                QitStatement.qit_cd_list(self, current)

                return '/'.join(current)
        else:
            if statement_line[1] in self.qit_list:
                current.append(statement_line[1])

            QitStatement.qit_cd_list(self, current)

            return '/'.join(current)
