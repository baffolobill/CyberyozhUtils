import os
import sys
import platform
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent.resolve()

# The text of the README file
README = (HERE / 'README.md').read_text(encoding='utf-8')

DEPENDENCIES = []

setup(
    name="cyberyozh_utils",
    version="1.0.0",
    author="Yurii Cherkasov",
    author_email="yurii.cherkasov@antidetect.online",
    description="Python utilities and helpers",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/CyberYozh/CyberyozhTools",
    project_urls={
        "Bug Tracker": "https://antidetect.atlassian.net/jira/software/projects/IPAUD/boards/8",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Commercial",
        "Operating System :: OS Independent",
    ],
    packages=["cyberyozh_utils"],
    package_dir={"": "src"},
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=DEPENDENCIES,
)
