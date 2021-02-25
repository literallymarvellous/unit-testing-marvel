from setuptools import setup, find_packages

setup(name="unit_testing_marvel",
      version="0.0.1",
      description="Univariate linear regression of housing price against housing area",
      author="Ahiara Ikechukwu",
      packages=find_packages("unit"),
      package_dir={"": "unit"},
      author_email="ahiaraikechukwu@gmail.com",
      install_requires=["jupyter>=1.0.0",
                        "matplotlib>=3.1.1",
                        "numpy>=1.17.3",
                        "pytest>=5.2.2",
                        "pytest-mpl>=0.10",
                        "pytest-mock>=1.11.2",
                        "scipy>=1.3.1",
                        ],
      )