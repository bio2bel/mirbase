# coding: utf-8

"""This module has the parser for miRBase."""

import gzip

from tqdm import tqdm


def mirbase_to_dict(path):
    """Parse miRNA data from filepath and convert it to dictionary.

    The structure of dictionary is {ID:[AC,DE,[[miRNA],[miRNA]]]}

    :param path: The path to the miRBase file
    :rtype: list[dict]
    """
    with gzip.open(path, 'r') as file:
        groups = []

        for line in file:
            line = line.decode('utf-8')

            if line.startswith('ID'):
                listnew = []
                groups.append(listnew)

            groups[-1].append(line)

        # print(groups[0][0][5:18])
        result = []
        for group in tqdm(groups):

            identifier = group[0][5:23].strip()
            accession = group[2][3:-2].strip()
            description = group[4][3:-1].strip()

            d = {
                'identifier': identifier,
                'description': description,
                'accession': accession
            }

            list_mirna = []
            for i in range(0, len(group)):
                if 'FT   miRNA    ' in str(group[i]):
                    list_mirna.append(i)

            d['products'] = [
                {
                    'location': group[index][10:-1].strip(),
                    'accession': group[index + 1][33:-2],
                    'product': group[index + 2][31:-2],
                }
                for index in list_mirna
            ]

            result.append(d)

    return result
