import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'todocore'
AUTHOR = 'Neel-Bimal'
AUTHOR_EMAIL = 'firebird@firebird.in'
URL = ''

DESCRIPTION = 'Request package for Todo list app'
#LONG_DESCRIPTION = (HERE / "README.md").read_text()
#LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    #   'numpy',
    #   'pandas',
    #   'tqdm',
    #   'neurokit2',
    #   'heartpy'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
#      long_description=LONG_DESCRIPTION,
#      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )