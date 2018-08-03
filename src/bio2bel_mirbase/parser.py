# coding: utf-8
import gzip

def miRNA_to_dict(path):
    """This function parse file of miRNA data from filepath and convert it to dictionary.The structure of dictionary is {ID:[AC,DE,[[miRNA],[miRNA]]]} """
    with gzip.open(path, 'r') as f:
        groups = []
        for line in f:
            if line.startswith(b'ID'):
                listnew = []
                groups.append(listnew)
                groups[-1].append(line)
            else:
                groups[-1].append(line)
        # print(groups[0][0][5:18])
        mirna_dict = {}
        for group in groups:
            IDname = group[0][5:23].strip()
            mirna_dict[IDname] = []

            AC = group[2][3:-2].strip()
            # print(AC)
            mirna_dict[IDname].append(AC)

            DE = group[4][3:-1].strip()
            # print(DE)
            mirna_dict[IDname].append(DE)
            list_mirna = []

            for i in range(0, len(group)):
                if 'FT   miRNA    ' in str(group[i]):
                    # print(i)
                    list_mirna.append(i)
            mirna_dict[IDname].append([])

            for index in list_mirna:
                mirna_dict[IDname][-1].append([])
                location = group[index][10:-1].strip()
                # print(location)
                mirna_dict[IDname][-1][-1].append(location)

                accession = group[index + 1][33:-2]
                # print(accession)
                mirna_dict[IDname][-1][-1].append(accession)

                product = group[index + 2][31:-2]
                # print(product)
                mirna_dict[IDname][-1][-1].append(product)

    return mirna_dict
