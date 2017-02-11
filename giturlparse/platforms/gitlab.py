# Imports
from .base import BasePlatform


class GitLabPlatform(BasePlatform):
    PATTERNS = {
        'https': r'https://(?P<domain>.+)/(?P<owner>.+)/(?P<repo>.+)(?:\.git)?',
        'ssh': r'git@(?P<domain>.+):(?P<owner>.+)/(?P<repo>.+)(?:\.git)?',
        'git': r'git://(?P<domain>.+)/(?P<owner>.+)/(?P<repo>.+)(?:\.git)?',
    }
    FORMATS = {
        'https': r'https://%(domain)s/%(owner)s/%(repo)s.git',
        'ssh': r'git@%(domain)s:%(owner)s/%(repo)s.git',
        'git': r'git://%(domain)s/%(owner)s/%(repo)s.git'
    }
    DEFAULTS = {
        '_user': 'git'
    }

