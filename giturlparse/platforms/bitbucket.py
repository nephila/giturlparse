# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .base import BasePlatform


class BitbucketPlatform(BasePlatform):
    PATTERNS = {
        'https': r'(?P<protocols>(git\+)?(?P<protocol>https))://(?P<_user>.+)@(?P<domain>.+?)(?P<pathname>/(?P<owner>.+)/(?P<repo>.+?)(?:\.git)?)$',
        'ssh': r'(?P<protocols>(git\+)?(?P<protocol>ssh))?(://)?git@(?P<domain>.+?):(?P<pathname>(?P<owner>.+)/(?P<repo>.+?)(?:\.git)?)$'
    }
    FORMATS = {
        'https': r'https://%(owner)s@%(domain)s/%(owner)s/%(repo)s.git',
        'ssh': r'git@%(domain)s:%(owner)s/%(repo)s.git'
    }
    DOMAINS = ('bitbucket.org',)
    DEFAULTS = {
        '_user': 'git'
    }
