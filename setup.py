# Reference: http://python-packaging.readthedocs.io/en/latest/dependencies.html
from setuptools import setup, find_packages

setup(name='pysurrogates',
      version='0.0.1',
      description='Bayesian Rule Lists',
      packages=find_packages(),
      install_requires=['scikit-learn>=0.18', 'pandas>=0.19', 'pymining'],
      include_package_data=True,
      zip_safe=False,)
