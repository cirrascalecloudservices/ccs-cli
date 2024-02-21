from setuptools import setup

config = {
    'name': 'ccs-cli',
    'py_modules': ['ccs'],
    'install_requires': ['requests', 'tabulate'],
    'entry_points': {
        'console_scripts': ['ccs=ccs:main'],
    }
}

setup(**config)
