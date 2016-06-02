#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' qitReader
qit_reader.py

created by @nocotan
'''
import sys

from login import Login
from qit_statement import QitStatement


class QitReader():
    """main block QitReader."""
    def __init__(self):
        """initialize."""
        pass

    def qit_reader(self):
        """qit_reader."""
        login = Login()
        client = login.get_client()
        user = client.get_authenticated_user().to_json()

        sys.stdout.write('Welcome to QitReader!\n')
        sys.stdout.write('You can read items in here.\n')

        statements = QitStatement()
        statements.set_root_list()

        all_items = client.list_items().to_json()
        follow_items = client.list_user_stocks(user['id']).to_json()
        all_tags = client.list_tags().to_json()
        follow_tags = client.list_user_following_tags(user['id']).to_json()

        statements.set_all_items(all_items)
        statements.set_follow_items(follow_items)
        statements.set_all_tags(all_tags)
        statements.set_follow_tags(follow_tags)

        path = '~'
        while True:
            sys.stdout.write("QitReader[{}] {} $ ".format(user['id'], path))
            statement_line = input().split(' ')
            statement = statement_line[0]

            if statement == 'exit':
                statements.qit_exit()
            elif statement == 'ls':
                statements.qit_ls(path)
            elif statement == 'cd':
                path = statements.qit_cd(path, statement_line)
            elif statement.isdigit():
                statements.qit_select(statement)
            else:
                print("unknown command.")

if __name__ == '__main__':
    qit_reader = QitReader()
    qit_reader.qit_reader()
