# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .base import BasePlatform


class GitHubPlatform(BasePlatform):
    PATTERNS = {
        'https': r'https://(?P<domain>.+)/(?P<owner>.+)/(?P<repo>.+?)(?:\.git)?$',
        'ssh': r'git@(?P<domain>.+):(?P<owner>.+)/(?P<repo>.+?)(?:\.git)?$',
        'git': r'git://(?P<domain>.+)/(?P<owner>.+)/(?P<repo>.+?)(?:\.git)?$',
    }
    FORMATS = {
        'https': r'https://%(domain)s/%(owner)s/%(repo)s.git',
        'ssh': r'git@%(domain)s:%(owner)s/%(repo)s.git',
        'git': r'git://%(domain)s/%(owner)s/%(repo)s.git'
    }
    DOMAINS = ('github.com', 'gist.github.com',)
    DEFAULTS = {
        '_user': 'git'
    }
