__author__ = 'Iacopo Spalletti'
__email__ = 'i.spalletti@nephila.it'
__version__ = '0.9.dev1'

from giturlparse.parser import parse as _parse
from giturlparse.result import GitUrlParsed


def parse(url, check_domain=True):
    return GitUrlParsed(_parse(url, check_domain))

def validate(url, check_domain=True):
    return parse(url, check_domain).valid
