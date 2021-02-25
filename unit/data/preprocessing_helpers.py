import re, os
import pytest


def row_to_list(str):
    # clean string
    str.rstrip()
    x = re.split('\t', str.strip())

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


@pytest.fixture
def raw_and_clean_data_file():
    raw_data_file_path = 'raw.txt'
    clean_data_file_path = 'clean.txt'
    with open(raw_data_file_path, 'w') as f:
        f.write('1,801\t201,411\n'
                '1,767565,112\n'
                '2,002\t333,209\n'
                '1990\t782,911\n'
                '1,285\t389129\n')
    yield raw_data_file_path, clean_data_file_path
    os.remove(raw_data_file_path)
    os.remove(clean_data_file_path)


def row_to_list_bug_free(row):
    return_values = {
                '1,801\t201,411\n': ['1,801', '201,411'],
                '1,767565,112\n': None,
                '2,002\t333,209\n' : ['2,002', '333,209'],
                '1990\t782,911\n' : ['1990', '782,911'],
                '1,285\t3899129\n' : ['1,285', '389129']
                    }
    return return_values[row]


# Define a function convert_to_int_bug_free
def convert_to_int_bug_free(comma_separated_integer_string):
    # Assign to the dictionary holding the correct return values
    return_values = {"1,801": 1801, "201,411": 201411, "2,002": 2002, "333,209": 333209, "1990": None, "782,911": 782911, "1,285": 1285, "389129": None}
    # Return the correct result using the dictionary return_values
    return return_values[comma_separated_integer_string]


def preprocess(raw_data_file_path, clean_data_file_path):
    with open(raw_data_file_path) as raw, open(clean_data_file_path, 'w') as clean:
        r = raw.readlines()
        f = [row_to_list(row) for row in r]
        f = [x for x in f if x is not None]
        k = [[convert_to_int(row[0]), convert_to_int(row[1])] for row in f]
        k = [x for x in k if x[0] and x[1] is not None]
        for row in k:
            clean.write(str(row[0]) + '\t' + str(row[1]) + '\n')
