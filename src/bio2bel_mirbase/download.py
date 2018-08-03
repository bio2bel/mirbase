# -*- coding: utf-8 -*-

"""Utilities for downloading miRBase."""

from urllib.request import urlretrieve

from .constants import DATA_URL, DATA_PATH


def download():
    urlretrieve(DATA_URL, DATA_PATH)
