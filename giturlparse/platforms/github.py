# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .base import BasePlatform


class GitHubPlatform(BasePlatform):
    PATTERNS = {
        'https': r'https://(?P<domain>[^/]+?)/(?P<owner>[^/]+?)/(?P<repo>[^/]+?)(?:\.git)?'
                 r'(?P<pathname>(/blob/|/tree/).+)?$',
        'ssh': r'git@(?P<domain>.+?):(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)'
               r'(?P<pathname>(/blob/|/tree/).+)?$',
        'git': r'git://(?P<domain>.+?)/(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?'
               r'(?P<pathname>(/blob/|/tree/).+)?$',
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

    @staticmethod
    def clean_data(data):
        data = BasePlatform.clean_data(data)
        if data["pathname"].startswith("/blob/"):
            data["path"] = data["pathname"].replace("/blob/", "")
        if data["pathname"].startswith("/tree/"):
            data["branch"] = data["pathname"].replace("/tree/", "")
        return data
