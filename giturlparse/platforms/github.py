# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .base import BasePlatform


class GitHubPlatform(BasePlatform):
    PATTERNS = {
        'https': r'https://(?P<domain>[^/]+?)/(?P<owner>[^/]+?)/(?P<repo>[^/]+?)(?:\.git)?'
                 r'(?P<pathname>/blob/.+)?$',
        'ssh': r'git@(?P<domain>.+?):(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)'
               r'(?P<pathname>/blob/.+)?$',
        'git': r'git://(?P<domain>.+?)/(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?'
               r'(?P<pathname>/blob/.+)?$',
    }
    FORMATS = {
        'https': r'https://%(domain)s/%(owner)s/%(repo)s.git%(pathname)s',
        'ssh': r'git@%(domain)s:%(owner)s/%(repo)s.git%(pathname)s',
        'git': r'git://%(domain)s/%(owner)s/%(repo)s.git%(pathname)s'
    }
    DOMAINS = ('github.com', 'gist.github.com',)
    DEFAULTS = {
        '_user': 'git'
    }
