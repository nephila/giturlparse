# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import unittest

from giturlparse import parse

# Test data
VALID_PARSE_URLS = (
    # Valid SSH, HTTPS, GIT
    ('SSH', ('git@github.com:Org/Repo.git', {
        'host': 'github.com',
        'user': 'git',
        'owner': 'Org',
        'repo': 'Repo',

        'protocol': 'ssh',
        'github': True,
        'bitbucket': False,
        'assembla': False
    })),
    ('HTTPS', ('https://github.com/Org/Repo.git', {
        'host': 'github.com',
        'user': 'git',
        'owner': 'Org',
        'repo': 'Repo',

        'protocol': 'https',
        'github': True,
        'bitbucket': False,
        'assembla': False
    })),
    ('HTTPS', ('https://github.com/foo-bar/xpwn', {
        'host': 'github.com',
        'user': 'git',
        'owner': 'foo-bar',
        'repo': 'xpwn',

        'protocol': 'https',
        'github': True,
    })),
    ('GIT', ('git://github.com/Org/Repo.git', {
        'host': 'github.com',
        'user': 'git',
        'owner': 'Org',
        'repo': 'Repo',

        'protocol': 'git',
        'github': True,
    })),
    ('GIT', ('git://github.com/foo-bar/xpwn', {
        'host': 'github.com',
        'user': 'git',
        'owner': 'foo-bar',
        'repo': 'xpwn',

        'protocol': 'git',
        'github': True,
    })),

    # BitBucket
    ('SSH', ('git@bitbucket.org:Org/Repo.git', {
        'host': 'bitbucket.org',
        'user': 'git',
        'owner': 'Org',
        'repo': 'Repo',

        'protocol': 'ssh',
        'platform': 'bitbucket'
    })),

    # Gitlab
    ('SSH', ('git@host.org:9999/Org/Repo.git', {
        'host': 'host.org',
        'user': 'git',
        'owner': 'Org',
        'repo': 'Repo',

        'protocol': 'ssh',
        'platform': 'gitlab'
    })),
    ('SSH', ('git@host.org:9999/Org-hyphen/Repo.git', {
        'host': 'host.org',
        'user': 'git',
        'owner': 'Org-hyphen',
        'repo': 'Repo',

        'protocol': 'ssh',
        'platform': 'gitlab'
    })),
    ('SSH', ('git@host.org:Org/Repo.git', {
        'host': 'host.org',
        'user': 'git',
        'owner': 'Org',
        'repo': 'Repo',

        'protocol': 'ssh',
        'platform': 'gitlab'
    })),
    ('SSH', ('ssh://git@host.org:9999/Org/Repo.git', {
        'host': 'host.org',
        'user': 'git',
        'owner': 'Org',
        'repo': 'Repo',

        'protocol': 'ssh',
        'platform': 'gitlab'
    })),
    ('HTTPS', ('https://host.org/Org/Repo.git', {
        'host': 'host.org',
        'user': 'git',
        'owner': 'Org',
        'repo': 'Repo',

        'protocol': 'https',
        'platform': 'gitlab'
    })),
)

INVALID_PARSE_URLS = (
    ('SSH No Username', '@github.com:Org/Repo.git'),
    ('SSH No Repo', 'git@github.com:Org'),
    ('HTTPS No Repo', 'https://github.com/Org'),
    ('GIT No Repo', 'git://github.com/Org'),
)


# Here's our "unit tests".
class UrlParseTestCase(unittest.TestCase):
    def _test_valid(self, url, expected):
        p = parse(url)
        self.failUnless(p.valid, "%s is not a valid URL" % url)
        for k, v in expected.items():
            attr_v = getattr(p, k)
            self.assertEqual(
                attr_v, v, "[%s] Property '%s' should be '%s' but is '%s'" % (
                    url, k, v, attr_v
                )
            )

    def testValidUrls(self):
        for test_type, data in VALID_PARSE_URLS:
            self._test_valid(*data)

    def _test_invalid(self, url):
        p = parse(url)
        self.failIf(p.valid)

    def testInvalidUrls(self):
        for problem, url in INVALID_PARSE_URLS:
            self._test_invalid(url)


# Test Suite
suite = unittest.TestLoader().loadTestsFromTestCase(UrlParseTestCase)
