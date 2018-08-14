# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .parser import parse as _parse
from .result import GitUrlParsed

__author__ = 'Iacopo Spalletti'
__email__ = 'i.spalletti@nephila.it'
__version__ = '0.9.2'


def parse(url, check_domain=True):
    return GitUrlParsed(_parse(url, check_domain))


def validate(url, check_domain=True):
    return parse(url, check_domain).valid
