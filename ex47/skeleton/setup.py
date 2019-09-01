try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'My Project',
    'author': 'Lauren Timzen',
    'url': 'https://github.com/laurentimzen/python_learning',
    'author_email': 'lauren.timzen@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'projectname'
]

setup(**config)
