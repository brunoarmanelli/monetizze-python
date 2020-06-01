#!/usr/bin/env python
from setuptools import setup
from io import open

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

setup(name='monetizze-python',
      version='0.1',
      description='Monetizze requests made easy',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      author='Bruno Armanelli',
      author_email='brunoarmanelli@me.com',
      url='https://github.com/brunoarmanelli/monetizze-python',
      packages=['monetizze'],
      keywords='monetizze',
      install_requires=['requests', 'six']
     )