# -*- coding: utf-8 -*-
"""Installer for the collective.contact.widget package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='collective.contact.widget',
    version='1.9',
    description="Contact widget",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='',
    author='Vincent Fretin',
    author_email='vincentfretin@ecreall.com',
    url='http://pypi.python.org/pypi/collective.contact.widget',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.contact'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'setuptools',
        'plone.api',
        'plone.formwidget.contenttree >= 1.0.11',
        'plone.formwidget.autocomplete',
        'z3c.relationfield',
    ],
    extras_require={
        'test': [
            'ecreall.helpers.testing',
            'plone.app.testing',
        ],
    },
    entry_points="""
    """,
)
