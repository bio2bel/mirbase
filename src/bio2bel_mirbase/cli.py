# -*- coding: utf-8 -*-

"""The command line interface module for Bio2BEL miRBase."""

import json
import sys

import click

from .download import download_definitions
from .manager import Manager
from .parser import make_bel_namespace, parse_definitions

main = Manager.get_cli()


@main.command()
@click.option('-f', '--file', type=click.File('w'), default=sys.stdout, help='the directory to save file')
def write_json(file):
    """Download and write miRBase to a file."""
    path = download_definitions()
    mirbase_dict = parse_definitions(path)
    json.dump(mirbase_dict, file, indent=2)


@main.command()
@click.option('-f', '--file', type=click.File('w'), default=sys.stdout, help='the directory to save file')
def write_belns(file):
    """Download and write miRBase to a BELNS."""
    path = download_definitions()
    mirbase_dict = parse_definitions(path)
    make_bel_namespace(mirbase_dict, file)


if __name__ == '__main__':
    main()
