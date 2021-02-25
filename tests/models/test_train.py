import pytest
import numpy as np
from math import sin, cos, pi
from unit.models.train import split_into_training_and_testing_sets, train_model, \
    model_test


class TestSplitIntoTrainingAndTestingSets(object):
    def test_on_one_dimension(self):
        test_argument = np.array([1382.0, 390167.0])
        # Store information about raised ValueError in exc_info
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
            raise ValueError

    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        # Store information about raised ValueError in exc_info
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
            raise ValueError

    def test_on_two_rows(self):
        test_argument = np.array([[1059.0, 186606.0], [1382.0, 390167.0]])
        # Fill in with training array's expected number of rows
        expected_training_array_num_rows = 1
        # Fill in with testing array's expected number of rows
        expected_testing_array_num_rows = 1
        actual = split_into_training_and_testing_sets(test_argument)
        # Write the assert statement checking training array's number of rows
        assert actual[0].shape[0] == expected_training_array_num_rows, \
            "The actual number of rows in the training array is not {}" \
                .format(expected_training_array_num_rows)
        # Write the assert statement checking testing array's number of rows
        assert actual[1].shape[0] == expected_testing_array_num_rows, \
            "The actual number of rows in the testing array is not {}". \
                format(expected_testing_array_num_rows)

    def test_on_three_rows(self):
        test_argument = np.array([[1059.0, 186606.0], [1382.0, 390167.0],
                                  [3458.0, 432894.0]])
        # Fill in with training array's expected number of rows
        expected_training_array_num_rows = 2
        # Fill in with testing array's expected number of rows
        expected_testing_array_num_rows = 1
        actual = split_into_training_and_testing_sets(test_argument)
        # Write the assert statement checking training array's number of rows
        assert actual[0].shape[0] == expected_training_array_num_rows, \
            "The actual number of rows in the training array is not {}" \
                .format(expected_training_array_num_rows)
        # Write the assert statement checking testing array's number of rows
        assert actual[1].shape[0] == expected_testing_array_num_rows, \
            "The actual number of rows in the testing array is not {}". \
                format(expected_testing_array_num_rows)

    def test_on_four_rows(self):
        test_argument = np.array([[1059.0, 186606.0], [1382.0, 390167.0],
                                  [3458.0, 432894.0], [2345.0, 453678.0]])
        # Fill in with training array's expected number of rows
        expected_training_array_num_rows = 3
        # Fill in with testing array's expected number of rows
        expected_testing_array_num_rows = 1
        actual = split_into_training_and_testing_sets(test_argument)
        # Write the assert statement checking training array's number of rows
        assert actual[0].shape[0] == expected_training_array_num_rows, \
            "The actual number of rows in the training array is not {}" \
                .format(expected_training_array_num_rows)
        # Write the assert statement checking testing array's number of rows
        assert actual[1].shape[0] == expected_testing_array_num_rows, \
            "The actual number of rows in the testing array is not {}". \
                format(expected_testing_array_num_rows)

    def test_on_five_rows(self):
        test_argument = np.array([[1059.0, 186606.0], [1382.0, 390167.0],
                                  [3456.0, 432895.0], [2345.0, 456786.0],
                                  [3576.0, 756383.0]])
        # Fill in with training array's expected number of rows
        expected_training_array_num_rows = 3
        # Fill in with testing array's expected number of rows
        expected_testing_array_num_rows = 2
        actual = split_into_training_and_testing_sets(test_argument)
        # Write the assert statement checking training array's number of rows
        assert actual[0].shape[0] == expected_training_array_num_rows, \
            "The actual number of rows in the training array is not {}" \
                .format(expected_training_array_num_rows)
        # Write the assert statement checking testing array's number of rows
        assert actual[1].shape[0] == expected_testing_array_num_rows, \
            "The actual number of rows in the testing array is not {}". \
                format(expected_testing_array_num_rows)

    def test_on_six_rows(self):
        test_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                  [1148.0, 206186.0], [1506.0, 248419.0],
                                  [1210.0, 214114.0], [1697.0, 277794.0]])
        # Fill in with training array's expected number of rows
        expected_training_array_num_rows = 4
        # Fill in with testing array's expected number of rows
        expected_testing_array_num_rows = 2
        actual = split_into_training_and_testing_sets(test_argument)
        # Write the assert statement checking training array's number of rows
        assert actual[0].shape[0] == expected_training_array_num_rows, \
            "The actual number of rows in the training array is not {}".format(expected_training_array_num_rows)
        # Write the assert statement checking testing array's number of rows
        assert actual[1].shape[0] == expected_testing_array_num_rows, \
            "The actual number of rows in the testing array is not {}".format(expected_testing_array_num_rows)

    def test_on_eight_rows(self):
        test_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                  [1148.0, 206186.0], [1506.0, 248419.0],
                                  [1210.0, 214114.0], [1697.0, 277794.0],
                                  [4356.0, 734657.0], [2345.0, 345679.0]])
        # Fill in with training array's expected number of rows
        expected_training_array_num_rows = 6
        # Fill in with testing array's expected number of rows
        expected_testing_array_num_rows = 2
        actual = split_into_training_and_testing_sets(test_argument)
        # Write the assert statement checking training array's number of rows
        assert actual[0].shape[0] == expected_training_array_num_rows, \
            "The actual number of rows in the training array is not {}".format(expected_training_array_num_rows)
        # Write the assert statement checking testing array's number of rows
        assert actual[1].shape[0] == expected_testing_array_num_rows, \
            "The actual number of rows in the testing array is not {}".format(expected_testing_array_num_rows)


class TestTrainModel(object):
    def test_on_linear_data(self):
        test_argument = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected_slope = 2.0
        expected_intercept = 1.0
        actual_slope, actual_intercept = train_model(test_argument)
        slope_message = ("train_model({0}) should return slope {1}, "
                         "but it actually returned slope {2}".format(test_argument, expected_slope, actual_slope)
                         )
        intercept_message = ("train_model({0}) should return intercept {1}, "
                             "but it actually returned intercept {2}".format(test_argument,
                                                                             expected_intercept,
                                                                             actual_intercept
                                                                             )
                             )
        assert actual_slope == pytest.approx(expected_slope), slope_message
        assert actual_intercept == pytest.approx(expected_intercept), intercept_message

    def test_on_positively_correlated_data(self):
        test_argument = np.array([[1.0, 4.0], [2.0, 4.0],
                                  [3.0, 9.0], [4.0, 10.0],
                                  [5.0, 7.0], [6.0, 13.0],
                                  ]
                                 )
        actual_slope, actual_intercept = train_model(test_argument)
        assert actual_slope > 0, "Expected slope: > 0, Actual slope: {0}".format(actual_slope)


@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):

    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)

    def test_on_perfect_fit(self):
        # Assign to a NumPy array containing a linear testing set
        test_argument = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        # Fill in with the expected value of r^2 in the case of perfect fit
        expected = 1.0
        # Fill in with the slope and intercept of the model
        actual = model_test(test_argument, slope=2, intercept=1)
        # Complete the assert statement
        assert actual == pytest.approx(expected), "Expected: {0}, \
        Actual: {1}".format(expected, actual)

    def test_on_circular_data(self):
        theta = pi / 4.0
        # Assign to a NumPy array holding the circular testing data
        test_argument = np.array([[1.0, 0.0], [cos(theta), sin(theta)],
                                  [0.0, 1.0],
                                  [cos(3 * theta), sin(3 * theta)],
                                  [-1.0, 0.0],
                                  [cos(5 * theta), sin(5 * theta)],
                                  [0.0, -1.0],
                                  [cos(7 * theta), sin(7 * theta)]]
                                 )
        # Fill in with the slope and intercept of the straight line
        actual = model_test(test_argument, slope=0.0, intercept=0.0)
        # Complete the assert statement
        assert actual == pytest.approx(0.0)