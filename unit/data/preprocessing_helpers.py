import re
import pytest


def row_to_list(row):
    # clean string
    row.rstrip()
    x = re.split("\t", row.strip())

    # List should contain 2 objects
    return (lambda a: a if len(a) == 2 and "" not in a else None)(x)


def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        # Write an if statement for checking missing commas
        if len(comma_separated_parts[i]) > 3:
            return None
        # Write the if statement for incorrectly placed commas
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    # Fill in with a ValueError
    except ValueError:
        return None


def preprocess(raw_data_file_path, clean_data_file_path):
    with open(raw_data_file_path) as raw, open(clean_data_file_path, 'w') as clean:
        r = raw.readlines()
        f = [row_to_list(row) for row in r]
        f = [x for x in f if x is not None]
        k = [[convert_to_int(row[0]), convert_to_int(row[1])] for row in f]
        k = [x for x in k if x[0] and x[1] is not None]
        for row in k:
            clean.write(str(row[0]) + '\t' + str(row[1]) + '\n')
