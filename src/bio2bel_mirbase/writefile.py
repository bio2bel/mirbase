# -*- coding: utf-8 -*-

"""Write the dictionary into a file"""

from .parser import miRNA_to_dict
from .download import download

def writefile(file):
    path = download()
    miRdict = miRNA_to_dict(path)

    file.write(str(miRdict))
