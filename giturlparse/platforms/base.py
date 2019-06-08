# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import itertools
import re


class BasePlatform(object):
    FORMATS = {
        'ssh': r"%(_user)s@%(host)s:%(repo)s.git",
        'http': r"http://%(host)s/%(repo)s.git",
        'https': r"https://%(host)s/%(repo)s.git",
        'git': r"git://%(host)s/%(repo)s.git"
    }

    PATTERNS = {
        'ssh': r"(?P<_user>.+)@(?P<domain>[^/]+?):(?P<repo>.+).git",
        'http': r"http://(?P<domain>[^/]+?)/(?P<repo>.+).git",
        'https': r"https://(?P<domain>[^/]+?)/(?P<repo>.+).git",
        'git': r"git://(?P<domain>[^/]+?)/(?P<repo>.+).git"
    }

    # None means it matches all domains
    DOMAINS = None
    SKIP_DOMAINS = None
    DEFAULTS = {}

    def __init__(self):
        # Precompile PATTERNS
        self.COMPILED_PATTERNS = dict(
            (proto, re.compile(regex))
            for proto, regex in self.PATTERNS.items()
        )

        # Supported protocols
        self.PROTOCOLS = self.PATTERNS.keys()

        if self.__class__ == BasePlatform:
            sub = [
                subclass.SKIP_DOMAINS
                for subclass in self.__class__.__subclasses__()
                if subclass.SKIP_DOMAINS
            ]
            if sub:
                self.SKIP_DOMAINS = list(itertools.chain.from_iterable(sub))
