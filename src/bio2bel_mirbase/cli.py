# -*- coding: utf-8 -*-

"""The command line interface module for Bio2BEL miRBase."""

import json
import sys

import click

from .download import download
from .parser import mirbase_to_dict


@click.command()
@click.option('-f', '--file', type=click.File('w'), default=sys.stdout, help='the directory to save file')
def main(file):
    """Download and write miRBase to a file."""
    path = download()
    mirbase_dict = mirbase_to_dict(path)
    json.dump(mirbase_dict, file, indent=2)


if __name__ == '__main__':
    main()
