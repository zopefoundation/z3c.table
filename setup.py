##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup
"""
import os

from setuptools import setup


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


setup(
    name="z3c.table",
    version='4.1.dev0',
    author="Stephan Richter, Roger Ineichen and the Zope Community",
    author_email="zope-dev@zope.dev",
    description="Modular table rendering implementation for Zope3",
    long_description=(
        read("README.rst")
        + "\n\n"
        + read("src", "z3c", "table", "README.rst")
        + "\n\n"
        + read("src", "z3c", "table", "sort.rst")
        + "\n\n"
        + read("src", "z3c", "table", "batch.rst")
        + "\n\n"
        + read("src", "z3c", "table", "sequence.rst")
        + "\n\n"
        + read("src", "z3c", "table", "column.rst")
        + "\n\n"
        + read("src", "z3c", "table", "miscellaneous.rst")
        + "\n\n"
        + read("CHANGES.rst")
    ),
    license="ZPL-2.1",
    keywords="zope3 z3c table content provider",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Framework :: Zope :: 3",
    ],
    url="https://github.com/zopefoundation/z3c.table",
    include_package_data=True,
    python_requires='>=3.9',
    extras_require=dict(
        test=[
            "zope.container",
            "zope.publisher",
            "zope.site",
            "zope.testing",
            "zope.testrunner",
        ]
    ),
    install_requires=[
        "setuptools",
        "future>=0.14.0",
        "z3c.batching>=1.1.0",
        "zope.component",
        "zope.contentprovider",
        "zope.dublincore",
        "zope.i18nmessageid",
        "zope.i18n",
        "zope.interface",
        "zope.location",
        "zope.schema",
        "zope.security",
        "zope.traversing",
    ],
    zip_safe=False,
)
