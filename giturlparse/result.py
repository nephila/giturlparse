# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .platforms import PLATFORMS

# Possible values to extract from a Git Url
REQUIRED_ATTRIBUTES = (
    'domain',
    'repo',
)


class GitUrlParsed(object):
    platform = None

    def __init__(self, parsed_info):
        self._parsed = parsed_info

        # Set parsed objects as attributes
        for k, v in parsed_info.items():
            setattr(self, k, v)

        for name, platform in PLATFORMS:
            if name == self.platform:
                self._platform_obj = platform

                break

    def _valid_attrs(self):
        return all(
            [getattr(self, attr, None) for attr in REQUIRED_ATTRIBUTES]
        )

    @property
    def valid(self):
        return all([
            self._valid_attrs(),
        ])

    ##
    # Alias properties
    ##
    @property
    def host(self):
        return self.domain

    @property
    def user(self):
        if hasattr(self, '_user'):
            return self._user

        return self.owner

    ##
    # Format URL to protocol
    ##
    def format(self, protocol):
        return self._platform_obj.FORMATS[protocol] % self._parsed

    ##
    # Normalize
    ##
    @property
    def normalized(self):
        return self.format(self.protocol)

    ##
    # Rewriting
    ##
    @property
    def url2ssh(self):
        return self.format('ssh')

    @property
    def url2http(self):
        return self.format('http')

    @property
    def url2https(self):
        return self.format('https')

    @property
    def url2git(self):
        return self.format('git')

    # All supported Urls for a repo
    @property
    def urls(self):
        return dict(
            (protocol, self.format(protocol))
            for protocol in self._platform_obj.PROTOCOLS
        )

    ##
    # Platforms
    ##
    @property
    def github(self):
        return self.platform == 'github'

    @property
    def bitbucket(self):
        return self.platform == 'bitbucket'

    @property
    def friendcode(self):
        return self.platform == 'friendcode'

    @property
    def assembla(self):
        return self.platform == 'assembla'

    @property
    def gitlab(self):
        return self.platform == 'gitlab'

    ##
    # Get data as dict
    ##
    @property
    def data(self):
        return dict(self._parsed)
