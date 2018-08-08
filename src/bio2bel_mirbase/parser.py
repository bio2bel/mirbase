# coding: utf-8

"""This module has the parser for miRBase."""

import gzip


def mirbase_to_dict(path):
    """Parse miRNA data from filepath and convert it to dictionary.

    The structure of dictionary is {ID:[AC,DE,[[miRNA],[miRNA]]]}

    :param path: The path to the miRBase file
    :rtype: dict
    """
    with gzip.open(path, 'r') as file:
        groups = []
        for line in file:
            if line.startswith(b'ID'):
                listnew = []
                groups.append(listnew)
            groups[-1].append(line)

        # print(groups[0][0][5:18])
        mirna_dict = {}
        for group in groups:
            identifier = group[0][5:23].strip()
            mirna_dict[identifier] = []

            accession = group[2][3:-2].strip()
            mirna_dict[identifier].append(accession)

            description = group[4][3:-1].strip()
            mirna_dict[identifier].append(description)
            list_mirna = []

            for i in range(0, len(group)):
                if 'FT   miRNA    ' in str(group[i]):
                    list_mirna.append(i)
            mirna_dict[identifier].append([])

            for index in list_mirna:
                mirna_dict[identifier][-1].append([])
                location = group[index][10:-1].strip()
                # print(location)
                mirna_dict[identifier][-1][-1].append(location)

                accession = group[index + 1][33:-2]
                # print(accession)
                mirna_dict[identifier][-1][-1].append(accession)

                product = group[index + 2][31:-2]
                # print(product)
                mirna_dict[identifier][-1][-1].append(product)

    return mirna_dict
