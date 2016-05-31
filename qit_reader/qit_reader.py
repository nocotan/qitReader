#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' qitReader
qit_reader.py

created by @nocotan
'''
import sys

from login import Login
from qit_statement import QitStatement
import stripper


class QitReader():
    ''' main block QitReader
    '''
    def __init__(self):
        pass

    def qit_reader(self):
        ''' qit_reader
        '''
        login = Login()
        client = login.get_client()
        user = client.get_authenticated_user().to_json()

        all_items = client.list_items().to_json()

        sys.stdout.write('Welcome to QitReader!\n')
        sys.stdout.write('You can read items in here.\n')

        statements = QitStatement()
        statements.set_root_list()

        i = 0
        for el in all_items:
            statements.all_items_list.append(
                    '[{}] {}'.format(i, el['title']))
            i += 1

        path = '~'
        while True:
            sys.stdout.write("QitReader[{}] {} $ ".format(user['id'], path))
            statement_line = input().split(' ')
            statement = statement_line[0]

            if statement == 'exit':
                statements.qit_exit()
            if statement == 'ls':
                statements.qit_ls(path)
            if statement == 'cd':
                path = statements.qit_cd(path, statement_line)
            if statement.isdigit():
                itm = int(statement)
                print(all_items[itm]['title'])
                print(stripper.strip(all_items[itm]['rendered_body']))

if __name__ == '__main__':
    qit_reader = QitReader()
    qit_reader.qit_reader()
