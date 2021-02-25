import pytest
import numpy as np
import os
from features.as_numpy import get_data_as_numpy_array


class TestGetDataAsNumpyArray(object):

    # Add a decorator to make this function a fixture
    @pytest.fixture
    def clean_data_file(self):
        file_path = "clean_data_file.txt"
        with open(file_path, "w") as f:
            f.write("201\t305671\n7892\t298140\n501\t738293\n")
        yield file_path
        os.remove(file_path)

    # Pass the correct argument so that the test can use the fixture
    def test_on_clean_file2(self, clean_data_file):
        expected = np.array([[201.0, 305671.0], [7892.0, 298140.0], [501.0, 738293.0]])
        # Pass the clean data file path yielded by the fixture as the first argument
        actual = get_data_as_numpy_array(clean_data_file, 2)
        assert actual == pytest.approx(expected), "Expected: {0}, \
        Actual: {1}".format(expected, actual)

    # @pytest.fixture
    # def empty_file():
    #     file_path = "empty.txt"
    #     open(file_path, "w").close()
    #     yield file_path
    #     os.remove(file_path)

    @pytest.fixture
    # Add the correct argument so that this fixture can chain with the tmpdir fixture
    def empty_file(self, tmpdir):
        # Use the appropriate method to create an empty file in the temporary directory
        file_path = tmpdir.join("empty.txt")
        open(file_path, "w").close()
        yield file_path

    def test_on_empty_file(self, empty_file):
        expected = np.empty((0, 2))
        actual = get_data_as_numpy_array(empty_file, 2)
        assert actual == pytest.approx(expected), "Expected: {0}, \
        Actual: {1}".format(expected, actual)