#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_dir(dirpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))


if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if 'no' == '{{ cookiecutter.need_docs }}':
        remove_dir('docs')
        remove_file('.readthedocs.yml')
        remove_file('.github/workflows/.deploy_docs.yml')
