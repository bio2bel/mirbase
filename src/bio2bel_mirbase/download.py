# -*- coding: utf-8 -*-

"""Utilities for downloading miRBase."""

from urllib.request import urlretrieve

from .constants import DATA_URL, DATA_PATH

import os
import logging

# build the logger using this module's name at runtime
log = logging.getLogger(__name__)


def download(force_download=False):
    """Downloads the compounds information

    :param bool force_download: If true, overwrites a previously cached file
    :rtype: str
    """
    if os.path.exists(DATA_PATH) and not force_download:
        log.info('using cached data at %s', DATA_PATH)
    else:
        log.info('downloading %s to %s', DATA_URL, DATA_PATH)
        urlretrieve(DATA_URL, DATA_PATH)

    return DATA_PATH
