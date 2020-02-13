try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup
import setuptools


long_description = open('README.md').read()


config = {
  'name': 'ok-anime',
  'description': 'this is a python wrapper for https://www.okanime.com',
  'author': 'Etherl',
  'keywords': ['ok anime', 'anime', 'ok','Arabic'],
  'python_requires': '>=3.4, <4',
  'license': '''Copyright (c) 2019 The Python Packaging Authority
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
.''',
  'long_description': long_description,
  'long_description_content_type': 'text/markdown',
  'url': 'https://github.com/Etherll/OKanime',
  'version': '1.0',
  'install_requires': ['requests', 'bs4'],
  'packages': setuptools.find_packages()
}
