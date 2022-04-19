"""A etuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html>=0.5.0>=0.5.0>=0.5.0
https://github.com/pypa/sampleproject
Autogenerated by poetry-setup:
https://github.com/orsinium/poetry-setup
"""
# IMPORTANT: this file is autogenerated. Do not edit it manually.
# All changes will be lost after `poetry-setup` command execution.
# ----------------------------------------------------------------
# Always prefer setuptools over distutils
import re

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    readme_txt = f.read()
with open(path.join(here, "HISTORY.rst"), encoding="utf-8") as f:
    history_txt = f.read()

long_description = "{}\n{}".format(
    re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub("", readme_txt),
    re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", history_txt),
)
# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
setup(
    # https://packaging.python.org/specifications/core-metadata/#name
    name="scml-agents",  # Required
    # https://www.python.org/dev/peps/pep-0440/
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.1.4",  # Required
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="Agents submitted to the SCML competition or contributed by the community",  # Required
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type="text/x-rst",  # Optional (see note above)
    url="https://github.com/yasserfarouk/scml-agents",  # Optional
    author="Yasser Mohammad",  # Optional
    author_email="yasserfarouk@gmail.com",  # Optional
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],  # Optional
    keywords=" ".join(
        ["negotiation", "mas", "multi-agent", "simulation", "AI"]
    ),  # Optional
    packages=find_packages(
        exclude=[
            "scml2020/**/*.pyc",
            "scml2020/**/__pycache__",
            "scml2019/**/*.pyc",
            "scml2019/**/__pycache__",
            "config",
            "docs",
            "etc",
            "notebooks",
            "tests",
        ]
    ),  # Required
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        "Click (>=6.0)",
        'dataclasses; python_version < "3.7"',
        "scml>=0.5.0",
        "torch",
        "pulp",
        "xgboost",
        "tensorflow; sys_platform != 'darwin' ",
        "tensorflow-macos; sys_platform == 'darwin' ",
    ],  # Optional
    # extras_require={},
    # https://setuptools.readthedocs.io/en/latest/setuptools.html#dependencies-that-aren-t-in-pypi
    dependency_links=[],  # Optional
    # https://stackoverflow.com/a/16576850
    include_package_data=True,
    # entry_points={  # Optional
    #     "console_scripts": ["negmas=negmas.scripts.app:cli", "negui=negmas.gui.app:cli"]
    # },
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    project_urls={"homepage": "https://github.com/yasserfarouk/negmas"},  # Optional
    python_requires=">=3.6",
)
