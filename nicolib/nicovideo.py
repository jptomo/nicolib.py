from __future__ import absolute_import

from .util import xml2dict
from ._compat import urlopen


class Niconico():
    def login(self):
        '''TODO:
        '''

    def logout(self):
        '''TODO:
        '''

    def search(self):
        '''TODO: implement: http://search.nicovideo.jp/docs/api/snapshot.html
        '''


class Movie(object):
    '''TODO: implement: http://res.nimg.jp/js/nicoapi.js
    '''

    def __init__(self, movie_id):
        self.movie_id = movie_id
        self._info = {}

    def get_owner(self):
        '''TODO:
        '''

    def _get_info(self):
        if not self._info:
            res = get_getthumbinfo(self.movie_id)
            for elem in res['children'][0]['children']:
                tag = elem.pop('tag')
                self._info[tag] = elem
        return self._info


class User(object):
    '''TODO: implement: http://res.nimg.jp/js/nicoapi.js
    '''

    def __init__(self, user_id):
        self.user_id = user_id

    def get_uploaded(self):
        '''TODO:
        '''

    def get_mylists(self):
        pass


# ### low-level api ###


def get_getthumbinfo(movie_id):
    try:
        _response = urlopen(
            ('http://ext.nicovideo.jp/api/'
             'getthumbinfo/{movie_id:s}')
            .format(movie_id=movie_id))
        return xml2dict(_response.read())
    finally:
        _response.close()


def get_thumb(movie_id):
    try:
        _response = urlopen(
            'http://ext.nicovideo.jp/thumb/{movie_id:s}'
            .format(movie_id=movie_id))
        return _response.read().decode('utf-8')
    finally:
        _response.close()


def get_getflv(movie_id):
    '''
    "closed=1&done=true"
    '''
    try:
        _response = urlopen(
            'http://flapi.nicovideo.jp/api/getflv/{movie_id:s}'
            .format(movie_id=movie_id))
        return _response.read()
    finally:
        _response.close()


def get_getmarquee(movie_id):
    pass


def get_getrelation():
    pass


def get_msg(movie_id):
    pass


def get_mylist(mylist_id, rss_type='atom'):
    try:
        _response = urlopen(
            ('http://www.nicovideo.jp/mylist/'
             '{mylist_id:s}?rss={rss_type:s}')
            .format(mylist_id=mylist_id, rss_type=rss_type))
        return xml2dict(_response.read())
    finally:
        _response.close()


def get_uploaded(user_id, rss_type='atom'):
    try:
        _response = urlopen(
            ('http://www.nicovideo.jp/user/'
             '{user_id:s}/video?rss={rss_type:s}')
            .format(user_id=user_id, rss_type=rss_type))
        return xml2dict(_response.read())
    finally:
        _response.close()
