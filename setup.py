import setuptools

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'ccs-cli',
    'install_requires': ['requests'],
    'entry_points' : {
        'console_scripts': ['ccs=cirrascale.cli:main'],
    }
}

setup(**config)
