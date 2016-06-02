#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' qitReader
qit_statement.py

created by @nocotan
'''
import sys

import stripper


class QitStatement():
    """QitReader statement."""

    def __init__(self):
        """initialize."""
        self.qit_list = []
        self.root_list = ['all_items',
                          'follow_items',
                          'all_tags',
                          'follow_tags']
        self.all_items_list = []
        self.follow_items_list = []
        self.all_tags_list = []
        self.follow_tags_list = []

        self.all_items = []
        self.follow_items = []
        self.all_tags = []
        self.follow_tags = []

        """current_dir flags.
        0: root
        1: all_items
        2: follow_items
        3: all_tags
        4: follow_tags
        """
        self.current_dir = 0

    def set_root_list(self):
        """set root_list."""
        self.qit_list = self.root_list

    def set_all_items_list(self):
        """set all_items_list."""
        self.qit_list = self.all_items_list

    def set_follow_items_list(self):
        """set follow_items_list."""
        self.qit_list = self.follow_items_list

    def set_all_tags_list(self):
        """set all_tags_list."""
        self.qit_list = self.all_tags_list

    def set_follow_tags_list(self):
        """set follow_tags_list."""
        self.qit_list = self.follow_tags_list

    def set_all_items(self, all_items):
        """set all_items."""
        self.all_items = all_items

        i = 0
        for el in all_items:
            self.all_items_list.append('[{}] {}'.format(i, el['title']))
            i += 1

    def set_follow_items(self, follow_items):
        """set user stocked items."""
        self.follow_items = follow_items

        i = 0
        for el in follow_items:
            self.follow_items_list.append('[{}] {}'.format(i, el['title']))
            i += 1

    def set_all_tags(self, all_tags):
        """set all tags."""
        self.all_tags = all_tags

        i = 0
        for el in all_tags:
            self.all_tags_list.append('[{}] {}'.format(i, el['id']))
            i += 1

    def set_follow_tags(self, follow_tags):
        """set follow_tags."""
        self.follow_tags = follow_tags

        i = 0
        for el in follow_tags:
            self.follow_tags_list.append('[{}] {}'.format(i, el['id']))
            i += 1

    def qit_exit(self):
        """exit system."""
        sys.stdout.write('Bye.\n')
        sys.exit()

    def qit_ls(self, path):
        """ls."""
        sys.stdout.write('  '.join(self.qit_list))
        sys.stdout.write('\n')

    def qit_cd_list(self, current):
        """cd_list."""
        cdir = current[-1]
        if cdir == '~':
            QitStatement.set_root_list(self)
            self.current_dir = 0
        elif cdir == 'all_items':
            QitStatement.set_all_items_list(self)
            self.current_dir = 1
        elif cdir == 'follow_items':
            QitStatement.set_follow_items_list(self)
            self.current_dir = 2
        elif cdir == 'all_tags':
            QitStatement.set_all_tags_list(self)
            self.current_dir = 3
        elif cdir == 'follow_tags':
            QitStatement.set_follow_tags_list(self)
            self.current_dir = 4

    def qit_cd(self, path, statement_line):
        """cd."""
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
            else:
                print("No such directory.")

            QitStatement.qit_cd_list(self, current)

            return '/'.join(current)

    def qit_select(self, statement):
        """qit_select."""
        num = int(statement)
        flag = self.current_dir

        err_msg = "No such directory or item."
        disp = err_msg

        if flag == 0 and num <= 3:
            disp = self.qit_list[num]
        elif flag == 1 and num < len(self.all_items):
            disp = self.all_items[num]['title'] + "\n" \
                + stripper.strip(self.all_items[num]['rendered_body'])
        elif flag == 2 and num < len(self.follow_items):
            disp = self.follow_items[num]['title'] + "\n" \
                + stripper.strip(self.follow_items[num]['rendered_body'])
        elif flag == 3 and num < len(self.all_tags):
            disp = self.all_tags[num]['id']
        elif flag == 4 and num < len(self.follow_tags):
            disp = self.follow_tags[num]['id']

        print(disp)
