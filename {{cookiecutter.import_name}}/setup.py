import os
import sys
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "{{cookiecutter.import_name}}", "__version__.py")) as version_file:
    exec(version_file.read()) # pylint: disable=W0122

_INSTALL_REQUIERS = []

setup(name="{{cookiecutter.import_name}}",
      classifiers = [
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          ],
      description="Python library for deprecating code",
      license="{{cookiecutter.license}}",
      author="Slash Developers",
      author_email="{{cookiecutter.developer_email}}",
      version=__version__, # pylint: disable=E0602
      packages=find_packages(exclude=["tests"]),

      url="https://github.com/{{cookiecutter.gh_username}}/{{cookiecutter.import_name}}",

      install_requires=_INSTALL_REQUIERS,
      scripts=[],
      namespace_packages=[]
      )
