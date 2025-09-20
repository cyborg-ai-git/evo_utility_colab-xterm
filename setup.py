#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages  # type: ignore
import os
VERSION='2025.9.201800'

def _get_version():
    version_file = os.path.normpath(os.path.join(os.path.dirname(__file__), 'cyborgai_colab_xterm', 'VERSION'))
    try:
        with open(version_file) as fh:
            version = fh.read().strip()
            # If version is 'dev', use a proper version format
            if version == 'dev':
                return VERSION + '.dev0'
            return version
    except FileNotFoundError:
       return VERSION

setup(name='cyborgai-colab-xterm',
      version=_get_version(),
      description='Open a terminal in colab, including the free tier.',
      long_description_content_type="text/markdown",
      long_description=open('README.md').read(),
      url='https://github.com/cyborg-ai-git',
      project_urls={
          "Bug Tracker": "https://github.com/cyborg-ai-git/evo_utility_colab-xterm.git",
      },
      python_requires=">=3.6",
      packages=["cyborgai_colab_xterm"],
      package_data={
          'cyborgai_colab_xterm': ['client/dist/*', 'VERSION']
      },
      include_package_data=True,
      install_requires=['ptyprocess~=0.7.0', 'tornado>5.1'],
      extras_require={
          'dev': [
              'jupyter',
              'twine'
          ],
      }
      )
