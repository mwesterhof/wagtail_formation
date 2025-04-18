#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


requirements = [
    'cryptography==39.0.0',
    'wagtail-generic-chooser==0.6.1',
]

test_requirements = []

setup(
    author="Marco Westerhof",
    author_email='m.westerhof@lukkien.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    description="Build forms from wagtail blocks",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='wagtail_formation',
    name='wagtail_formation',
    packages=find_packages(include=['formation', 'formation.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mwesterhof/wagtail_formation',
    version='0.2.0',
    zip_safe=False,
)
