# setup.py

from setuptools import setup, find_packages

setup(
    # Metadata
    name='production_lines_lib',
    version='6.1.8', 
    author='Dimitrios Koromilas',
    author_email='dimkoromilas@gmail.com',
    description='Compute Production Line KPIs.',
    url='https://github.com/dataanalytics986/production_lines_project',

    # Package modules path
    packages=find_packages(),

    # Check for the dependencies 
    install_requires=[
        'pandas>=1.0.0',
    ],

    python_requires='>=3.10', # Minimum Python version required
)