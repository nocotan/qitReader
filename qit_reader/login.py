#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' qitReader
login.py

created by @nocotan
'''
import os
import sys

from qiita_v2.client import QiitaClient


class Login():
    ''' login Qiita
    '''
    def __init__(self):
        ''' initialize instanse with access_token
        '''
        config_file = '.config'
        if not os.path.exists('./'+config_file):
            sys.stdout.write('YOUR ACCESS TOKEN: ')
            access_token = str(input())
            with open(config_file, 'w') as f:
                f.write('ACCESS_TOKEN: {}'.format(access_token))
        else:
            with open(config_file, 'r') as f:
                access_token = f.read().split(' ')[1].strip()

        self.access_token = access_token
        self.client = QiitaClient(access_token=access_token)

    def get_client(self):
        return self.client

    def get_access_token(self):
        return self.access_token
