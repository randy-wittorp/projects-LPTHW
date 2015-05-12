try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Randy Wittorp',
    'url': 'github.com/randy-wittorp/',
    'download url': 'Where to download',
    'author_email': 'randy.wittorp@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
