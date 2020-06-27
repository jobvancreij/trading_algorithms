import setuptools
import os
import sys
with open("README.md", "r") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

if sys.version_info[0] != 3: #raise exception when not using python3
    raise ImportError("This repo needs python3 to be installed, you use python {}".format(sys.version_info[0]))



setuptools.setup(
    name="LJT_database",
    version="0.0.2",
    author="Job van Creij & Lex Fons",
    author_email="jobvancrey@hotmail.com",
    description="Simulate trading",
    long_description=long_description,
    url="https://github.com/jobvancreij/trading_algorithms",
    packages=setuptools.find_packages(),
    install_requires=required,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)