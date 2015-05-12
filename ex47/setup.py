try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex47',
    'author': 'Randy Wittorp',
    'url': 'github.com/randy-wittorp/',
    'download url': 'Where to download',
    'author_email': 'randy.wittorp@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
