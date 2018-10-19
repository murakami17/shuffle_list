# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='shuffle_list',
    version='0.1.0',
    description='Shuffle and put icons with given distributions.',
    long_description=readme,
    author='Taku MURAKAMI',
    author_email='murakami.taku.17@shizuoka.ac.jp',
    url='https://github.com/murakami17/shuffule_list',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

