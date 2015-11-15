import sys


IS_PY2 = sys.version_info.major == 2
IS_PY3 = sys.version_info.major == 3


if IS_PY2:
    from urllib2 import urlopen
elif IS_PY3:
    from urllib.request import urlopen
