import setuptools
import os

pkg_vars = {}
pkg_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(pkg_dir, "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stream_repeater",
    version='0.1.0',
    author="FrozenFOXX",
    author_email="frozenfoxx@churchoffoxx.net",
    description="Example REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frozenfoxx/restapi-python",
    packages=["restapi"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License v2",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'fastapi'
    ],
    entry_points = {
        "console_scripts": ["restapi=restapi.app:main"],
    },
    data_files=[],
)

