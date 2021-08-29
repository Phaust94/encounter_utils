"""
Setups the current library
"""

from setuptools import setup
from setuptools import find_packages
import os
import re

VERSION_FILE = "version.py"
VERSION_RE = r"__version__ = [\'\"]([\d*.]*\d+[a-z]{0,3}\d{0,2})[\'\"]"
REQIRE_FILE = 'REQUIRE.txt'


def main() -> None:
    """
    SE
    :return:
    """

    name = 'encounter_utils'

    version_file = open(os.path.join(name, VERSION_FILE))
    version_file = version_file.read()
    ver = re.findall(VERSION_RE, version_file)[0]

    with open(REQIRE_FILE, 'r') as requirements_file:
        requirements = requirements_file.readlines()
        requirements = list(map(str.strip, requirements))

    setup(
        name=name,
        version=ver,
        description="Utility functions for working with Ecnunter games",
        author='Phaust94',
        license='GPL-3.0',
        packages=find_packages(),
        install_requires=requirements,
        python_requires='>=3.7.0',
        zip_safe=False,
        include_package_data=True,
    )

    return None


if __name__ == '__main__':
    main()
