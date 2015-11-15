from __future__ import absolute_import

from .util import xml2dict
from ._compat import urlopen


class NMovie(object):
    def __init__(self, movie_id):
        self.movie_id = movie_id
        self._info = {}

    @staticmethod
    def _get_info(movie_id):
        information = {}
        res = get_getthumbinfo(movie_id)
        for elem in res['children'][0]['children']:
            tag = elem.pop('tag')
            information[tag] = elem
        return information

    def get_info(self):
        if not self._info:
            self._info = self._get_info(self.movie_id)
        return self._info


class NUser(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def get_uploaded(self):
        pass


# ### low-level api ###


def get_getthumbinfo(movie_id):
    base_url = ('http://ext.nicovideo.jp/api/'
                'getthumbinfo/{movie_id:s}')

    try:
        _response = urlopen(
            base_url
            .format(movie_id=movie_id))
        return xml2dict(_response.read())
    finally:
        _response.close()


def get_thumb(movie_id):
    base_url = 'http://ext.nicovideo.jp/thumb/{movie_id:s}'

    try:
        _response = urlopen(base_url.format(movie_id=movie_id))
        return _response.read().decode('utf-8')
    finally:
        _response.close()


def get_getflv(movie_id):
    '''
    "closed=1&done=true"
    '''
    base_url = 'http://flapi.nicovideo.jp/api/getflv/{movie_id:s}'

    try:
        _response = urlopen(base_url.format(movie_id=movie_id))
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
    base_url = ('http://www.nicovideo.jp/mylist/'
                '{mylist_id:s}?rss={rss_type:s}')

    try:
        _response = urlopen(
            base_url
            .format(mylist_id=mylist_id, rss_type=rss_type))
        return xml2dict(_response.read())
    finally:
        _response.close()


def get_uploaded(user_id, rss_type='atom'):
    base_url = ('http://www.nicovideo.jp/user/'
                '{user_id:s}/video?rss={rss_type:s}')

    try:
        _response = urlopen(
            base_url
            .format(user_id=user_id, rss_type=rss_type))
        return xml2dict(_response.read())
    finally:
        _response.close()
