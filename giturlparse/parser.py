# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from collections import defaultdict

from .platforms import PLATFORMS

SUPPORTED_ATTRIBUTES = (
    'domain',
    'repo',
    'owner',
    '_user',
    'port',

    'url',
    'platform',
    'protocol',
)


def parse(url, check_domain=True):
    # Values are None by default
    parsed_info = defaultdict(lambda: None)
    parsed_info['port'] = ''

    # Defaults to all attributes
    map(parsed_info.setdefault, SUPPORTED_ATTRIBUTES)

    for name, platform in PLATFORMS:
        for protocol, regex in platform.COMPILED_PATTERNS.items():
            # Match current regex against URL
            match = regex.match(url)

            # Skip if not matched
            if not match:
                # print("[%s] URL: %s dit not match %s" % (name, url, regex.pattern))
                continue

            # Skip if domain is bad
            domain = match.group('domain')
            # print('[%s] DOMAIN = %s' % (url, domain,))
            if check_domain:
                if platform.DOMAINS and not (domain in platform.DOMAINS):
                    # print("domain: %s not in %s" % (domain, platform.DOMAINS))
                    continue

            # add in platform defaults
            parsed_info.update(platform.DEFAULTS)

            # Get matches as dictionary
            matches = match.groupdict(default='')

            # Update info with matches
            parsed_info.update(matches)

            # Update info with platform info
            parsed_info.update({
                'url': url,
                'platform': name,
                'protocol': protocol,
            })
            return parsed_info

    # Empty if none matched
    return parsed_info
