# -*- coding: utf-8 -*-

"""Wrap all functions together"""

import click
from .writefile import writefile
import sys


@click.command()
@click.option('--file', type=click.File('w'), default=sys.stdout, help='the directory to save file')
def main(file):
    writefile(file)


if __name__ == '__main__':
    main()
