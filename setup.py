#!/usr/bin/env python3.8
"""Phishlabs API Client: Setup
Copyright © 2019 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
import logging
from typing import NoReturn

from setuptools import find_packages, setup
import sys

logger = logging.getLogger(__name__)


def readme() -> str:
    with open('README.md') as f:
        return f.read()


def main() -> NoReturn:
    setup(author_email='jerod@jerodg.dev',
          author='Jerod Gawne',
          classifiers=['Development Status :: 5 - Production/Stable',
                       'Environment :: Console',
                       'Intended Audience :: End Users/Desktop',
                       'Intended Audience :: Developers',
                       'Intended Audience :: System Administrators',
                       'License :: Other/Proprietary License',
                       'Natural Language :: English',
                       'Operating System :: MacOS :: MacOS X',
                       'Operating System :: Microsoft :: Windows',
                       'Operating System :: POSIX',
                       'Programming Language :: Python :: 3.8',
                       'Topic :: Utilities',
                       'Topic :: Internet',
                       'Topic :: Internet :: WWW/HTTP'],
          description='Phishlabs API Client Library',
          entry_points={'console_scripts': []},
          include_package_data=True,
          install_requires=['base-api-client==0.9.0'],
          keywords='Phishlabs API Client rest',
          license='Server Side Public License (SSPL)',
          long_description_content_type='text/markdown',
          long_description=readme(),
          name='phishlabs-api-client',
          package_data={'phishlabs-api-client': []},
          packages=find_packages(),
          project_urls={'Bugs':          'https://github.com/jerodg/phishlabs-api-client/issues',
                        'Documentation': 'https://jerodg.github.io/phishlabs-api-client',
                        'Funding':       'https://www.paypal.me/jerodgawne',
                        'Say Thanks!':   'https://saythanks.io/to/jerodg',
                        'Source':        'https://github.com/jerodg/phishlabs-api-client'},
          python_requires='>=3.8, <3.9',
          setup_requires=[] + ['pytest-runner'] if {'pytest', 'test', 'ptr'}.intersection(sys.argv) else [],
          tests_require=['pytest', 'pytest-asyncio'],
          url='https://pypi.org/project/phishlabs-api-client/',
          version='0!0.1.0',
          zip_safe=True)


if __name__ == '__main__':
    try:
        main()
    except Exception as excp:
        logger.exception(excp)
