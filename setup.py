from setuptools import setup, find_packages

version = '0.1'

setup(name='bhr-source-bhr',
    version=version,
    description="BHR block source that uses another BHR installation as a data source",
    long_description="",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='bhr',
    author='Justin Azoff',
    author_email='JAzoff@illinois.edu',
    url='',
    license='MIT',
    py_modules = ["bhr_source_bhr"],
    install_requires=[
        "bhr_client>=0.16",
    ],
    entry_points = {
        'console_scripts': [
            'bhr-source-bhr = bhr_source_bhr:main',
        ]
    },
)
