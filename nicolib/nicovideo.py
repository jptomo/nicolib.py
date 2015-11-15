from __future__ import absolute_import

from .util import xml2dict
from ._compat import urlopen


class NMovie(object):
    def __init__(self, movie_id):
        self.movie_id = movie_id
        self._info = {}

    def refresh_info(self):
        res = get_getthumbinfo(self.movie_id)
        self._info = {}
        for elem in res['children'][0]['children']:
            tag = elem.pop('tag')
            self._info[tag] = elem

    def get_info(self):
        if not self._info:
            self.refresh_info()
        return self._info


class NUser(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def get_uploaded(self):
        pass


# ### low-level api ###


def get_getthumbinfo(movie_id):
    base_url = 'http://ext.nicovideo.jp/api/'
    ext_url = 'getthumbinfo/{movie_id:s}'.format(movie_id=movie_id)
    target_url = base_url + ext_url

    try:
        _response = urlopen(target_url)
        return xml2dict(_response.read())
    finally:
        _response.close()


def get_thumb(movie_id):
    base_url = 'http://ext.nicovideo.jp/api/{movie_id:s}'

    try:
        _response = urlopen(base_url.format(movie_id=movie_id))
        return _response.read()
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
    base_url = 'http://www.nicovideo.jp/mylist/{mylist_id:s}?rss={rss_type:s}'
    try:
        _response = urlopen(
            base_url.format(mylist_id=mylist_id, rss_type=rss_type))
        return xml2dict(_response.read())
    finally:
        _response.close()


def get_uploaded(user_id, rss_type='atom'):
    base_url = 'http://www.nicovideo.jp/user/{user_id:s}/video?rss={rss_type:s}'
    try:
        _response = urlopen(
            base_url.format(user_id=user_id, rss_type=rss_type))
        return xml2dict(_response.read())
    finally:
        _response.close()
