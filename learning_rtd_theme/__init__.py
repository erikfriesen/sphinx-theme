"""Sphinx Boundless Learning theme.

From http://github.com/boundlessgeo/training

"""
import os

VERSION = (2, 0, 0)

__version__ = ".".join(str(v) for v in VERSION)
__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir
