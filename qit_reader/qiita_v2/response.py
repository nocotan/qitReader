''' qiita.QiitaResponse
Handling QiitaClient response

created by @petitviolet
'''
import re


class QiitaResponse():
    ''' Wrap requests.Response
    '''
    def __init__(self, response):
        ''' initialize with requests.Response
        :params response: instance of requests.Response
        '''
        self.response = response
        self.headers = response.headers
        self.table = {}

    def to_json(self):
        ''' Returns jsonified contents of response
        '''
        return self.response.json()

    @property
    def status(self):
        ''' Returns status code
        '''
        return self.response.status_code

    def _get_from_header(self, key):
        ''' extrace value from header if key exists
        '''
        return self.headers[key] if key in self.headers else None

    @property
    def result_count(self):
        ''' Returns count of result
        '''
        return self._get_from_header('Total-Count')

    @property
    def remain_request_count(self):
        ''' Returns how many api counts remaining
        '''
        return self._get_from_header('Rate-Remaining')

    @property
    def links(self):
        ''' split 'Link' header for pagenation
        '''
        if self.table:
            return self.table
        links = self._get_from_header('Link').split(',')
        pattern = re.compile(r'<(.+?)>; rel="(.+?)"')
        for link in links:
            url, rel = pattern.findall(link.strip())[0]
            self.table[rel] = url
        return self.table

    @property
    def link_first(self):
        ''' Returns link to first page
        '''
        return self.links['first']

    @property
    def link_next(self):
        ''' Returns link to next page
        '''
        return self.links['next']

    @property
    def link_last(self):
        ''' Returns link to last page
        '''
        return self.links['last']
