import platform
import subprocess as sps
import sys
from typing import List

from eel.types import OptionsDictT

name: str = 'Edge'


def run(_path: str, options: OptionsDictT, start_urls: List[str]) -> None:
    cmd = 'start msedge --app={} '.format(start_urls[0])
    cmd = cmd + (" ".join(options['cmdline_args']))
    sps.Popen(cmd, stdout=sys.stdout, stderr=sys.stderr, stdin=sps.PIPE, shell=True)


def find_path() -> bool:
    if platform.system() == 'Windows':
        return True

    return False
