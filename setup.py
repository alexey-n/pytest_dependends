__author__ = 'alexey-n'

from setuptools import setup

setup(
    name='pytest-dependency',
    description='pytest plugin to make dependend tests',
    version='1.0',
    author=__author__,
    author_email=__author__ + '.test@yandex.ru',
    url='https://github.com/alexey-n/pytest_dependends',
    packages=['pytest_dependency'],
    entry_points = {
        'pytest11': [
            'pytest_dependency = pytest_dependency',
        ]
    },
    install_requires=['pytest'],
)