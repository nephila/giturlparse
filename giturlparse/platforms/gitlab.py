# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .base import BasePlatform


class GitLabPlatform(BasePlatform):
    PATTERNS = {
        'https': r'https://(?P<domain>.+)(?P<port>:[0-9]+)?/(?P<owner>.+)/'
                 r'(?P<repo>.+?)(?:\.git)?$',
        'ssh': r'(ssh://)?git@(?P<domain>.+):(?P<port>[0-9]+/)?(?P<owner>.+)/'
               r'(?P<repo>.+?)(?:\.git)?$',
        'git': r'git://(?P<domain>.+):(?P<port>[0-9]+)?/(?P<owner>.+)/'
               r'(?P<repo>.+?)(?:\.git)?$',
    }
    FORMATS = {
        'https': r'https://%(domain)s/%(owner)s/%(repo)s.git',
        'ssh': r'git@%(domain)s:%(port)s%(owner)s/%(repo)s.git',
        'git': r'git://%(domain)s%(port)s/%(owner)s/%(repo)s.git'
    }
    DEFAULTS = {
        '_user': 'git',
        'port': ''
    }
