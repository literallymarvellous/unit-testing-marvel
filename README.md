This repository holds the code for the DataCamp course Unit Testing for Data Science in Python.
s repo using pip before running pytest. Otherwise, you may get ImportErrors.

To install it, first clone the repo.

git clone https://github.com/literallymarvellous/unit_testing_marvel.git
Then install the package locally using pip, making sure that you are using Python version >=3.6.

pip install -e unit_testing_marvel
Once the installation finishes, you can run all the tests by doing

cd unit_testing_marvel
pytest --mpl