# -*- coding: utf-8 -*-

"""Utilities for downloading miRBase."""

import logging
import os
from urllib.request import urlretrieve

from .constants import DATA_PATH, DATA_URL

log = logging.getLogger(__name__)


def download(force_download=False):
    """Download miRBase.

    :param bool force_download: If true, overwrites a previously cached file
    :rtype: str
    """
    if os.path.exists(DATA_PATH) and not force_download:
        log.info('using cached data at %s', DATA_PATH)
    else:
        log.info('downloading %s to %s', DATA_URL, DATA_PATH)
        urlretrieve(DATA_URL, DATA_PATH)

    return DATA_PATH
