#create setup.py
from setuptools import setup, find_packages
import io

name = 'NuOp'
description = 'NuOp: https://github.com/prakashmurali/NuOp'

# README file as long_description.
long_description = io.open("README.md", encoding="utf-8").read()

# Read in requirements
requirements = open("requirements.txt").readlines()
requirements = [r.strip() for r in requirements]

packages = find_packages()

setup(
    name=name,
    version="0.0.1",
    python_requires=(">=3.7.0"),
    install_requires=requirements,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=packages,
)


