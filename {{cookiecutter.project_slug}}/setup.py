#!/usr/bin/env python

"""The setup script."""

import re
from setuptools import setup, find_packages


def get_long_description():
    return "See https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}"

def get_version():
    with open("{{ cookiecutter.project_slug }}/__init__.py") as f:
        for line in f.readlines():
            m = re.match("__version__ = '([^']+)'", line)
            if m:
                return m.group(1)
        raise IOError("Version information can not found.")


def get_install_requirements():
    requirements = [
    ]
    return requirements


requires_test = ['pytest', 'pytest-cov', 'flake8', 'mypy']
requires_doc = []
with open("docs/requirements.txt") as f:
    for line in f:
        p = line.strip()
        if p:
            requires_doc.append(p)



{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="{{ cookiecutter.project_short_description }}",
    install_requires=get_install_requirements(),
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=get_long_description(),
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version=get_version(),
    zip_safe=False,
    extra_requires={
        'test': requires_test,
        'doc': requires_doc,
        'dev': ["pip", "setuptools", "wheel", "twine", "ipdb"] + requires_test + requires_doc,
    }
)
