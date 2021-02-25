import pytest
from data.preprocessing_helpers import row_to_list, convert_to_int, preprocess
from unittest.mock import call


@pytest.fixture
def raw_and_clean_data_file(tmpdir):
    raw_data_file_path = 'raw.txt'
    clean_data_file_path = 'clean.txt'
    with open(raw_data_file_path, 'w') as f:
        f.write('1,801\t201,411\n'
                '1,767565,112\n'
                '2,002\t333,209\n'
                '1990\t782,911\n'
                '1,285\t389129\n')
    yield raw_data_file_path, clean_data_file_path


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


class TestRowToList(object):
    def test_for_clean_row(self):
        assert row_to_list('2,081\t314,567\n') == ['2,081', '314,567']

    def test_for_missing_area(self):
        assert row_to_list('\t314,567\n') is None

    def test_for_missing_tab(self):
        assert row_to_list('1,46665,755\n') is None

    def test_on_no_tab_no_missing_value(self):  # (0, 0) boundary value
        # Assign actual to the return value for the argument "123\n"
        actual = row_to_list("123\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_two_tabs_no_missing_value(self):  # (2, 0) boundary value
        actual = row_to_list("123\t4,567\t89\n")
        # Complete the assert statement
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_one_tab_with_missing_value(self):  # (1, 1) boundary value
        actual = row_to_list("\t4,567\n")
        # Format the failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_no_tab_with_missing_value(self):  # (0, 1) case
        # Assign to the actual return value for the argument "\n"
        actual = row_to_list('\n')
        # Write the assert statement with a failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_two_tabs_with_missing_value(self):  # (2, 1) case
        # Assign to the actual return value for the argument "123\t\t89\n"
        actual = row_to_list("123\t\t89\n")
        # Write the assert statement with a failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)


class TestConvertToInt(object):
    def test_with_no_comma(self):
        actual = convert_to_int("756")
        # Complete the assert statement
        assert actual == 756, "Expected: 756, Actual: {0}".format(actual)

    def test_with_one_comma(self):
        actual = convert_to_int("2,081")
        # Complete the assert statement
        assert actual == 2081, "Expected: 2081, Actual: {0}".format(actual)

    def test_with_two_commas(self):
        actual = convert_to_int("1,034,891")
        # Complete the assert statement
        assert actual == 1034891, "Expected: 1034891, Actual: {0}".format(actual)

    # Give a name to the test for an argument with missing comma
    def test_on_string_with_missing_comma(self):
        actual = convert_to_int("178100,301")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_string_with_incorrectly_placed_comma(self):
        # Assign to the actual return value for the argument "12,72,891"
        actual = convert_to_int("12,72,891")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_float_valued_string(self):
        actual = convert_to_int("23,816.92")
        # Complete the assert statement
        assert actual is None, "Expected: None, Actual: {0}".format(actual)


class TestPreprocess(object):
    def test_on_raw_data(self, raw_and_clean_data_file):
        # setup: create the raw data file
        raw_path, clean_path = raw_and_clean_data_file
        preprocess(raw_path, clean_path)
        with open(clean_path) as f:
            lines = f.readlines()
        first_line = lines[0]
        assert first_line == '1801\t201411\n'
        second_line = lines[1]
        assert second_line == '2002\t333209\n'

    def test_on_raw_data_mock2(self, raw_and_clean_data_file, mocker):
        raw_path, clean_path = raw_and_clean_data_file
        row_to_list_mock = mocker.patch('data.preprocessing_helpers.row_to_list',
                                        side_efffect=row_to_list_bug_free)
        preprocess(raw_path, clean_path)
        assert row_to_list_mock.call_args_list == [
            call('1,801\t201,411\n'),
            call('1,767565,112\n'),
            call('2,002\t333,209\n'),
            call('1990\t782,911\n'),
            call('1,285\t389129\n')
        ]

    # Add the correct argument to use the mocking fixture in this test
    def test_on_raw_data_mock(self, raw_and_clean_data_file, mocker):
        raw_path, clean_path = raw_and_clean_data_file
        # Replace the dependency with the bug-free mock
        convert_to_int_mock = mocker.patch("data.preprocessing_helpers.convert_to_int",
                                           side_effect=convert_to_int_bug_free)
        preprocess(raw_path, clean_path)
        # Check if preprocess() called the dependency correctly
        assert convert_to_int_mock.call_args_list == [call("1,801"), call("201,411"), call("2,002"), call("333,209"),
                                                      call("1990"), call("782,911"), call("1,285"), call("389129")]
        with open(clean_path, "r") as f:
            lines = f.readlines()
        first_line = lines[0]
        assert first_line == "1801\t201411\n"
        second_line = lines[1]
        assert second_line == "2002\t333209\n"

