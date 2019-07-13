# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .base import BasePlatform


class GitLabPlatform(BasePlatform):
    PATTERNS = {
        'https': r'https://(?P<domain>.+?)(?P<port>:[0-9]+)?/(?P<owner>[^/]+?)/'
                 r'(?P<groups_path>.*?)?(?(groups_path)/)?(?P<repo>[^/]+?)(?:\.git)?'
                 r'(?P<raw_path>/blob/.+)?$',
        'ssh': r'(ssh://)?git@(?P<domain>.+?):(?P<port>[0-9]+)?(?(port)/)?(?P<owner>[^/]+)/'
               r'(?P<groups_path>.*?)?(?(groups_path)/)?(?P<repo>[^/]+?)(?:\.git)?'
               r'(?P<raw_path>/blob/.+)?$',
        'git': r'git://(?P<domain>.+?):(?P<port>[0-9]+)?(?(port)/)?(?P<owner>[^/]+)/'
               r'(?P<groups_path>.*?)?(?(groups_path)/)?(?P<repo>[^/]+?)(?:\.git)?'
               r'(?P<raw_path>/blob/.+)?$',
    }
    FORMATS = {
        'https': r'https://%(domain)s/%(owner)s/%(groups_slash)s%(repo)s.git%(raw_path)s',
        'ssh': r'git@%(domain)s:%(port_slash)s%(owner)s/%(groups_slash)s%(repo)s.git%(raw_path)s',
        'git': r'git://%(domain)s%(port)s/%(owner)s/%(groups_slash)s%(repo)s.git%(raw_path)s'
    }
    SKIP_DOMAINS = ('github.com', 'gist.github.com',)
    DEFAULTS = {
        '_user': 'git',
        'port': ''
    }
