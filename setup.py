# vim:fileencoding=utf-8:noet

import io
from os import path

from setuptools import setup

version = "0.7.3"

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="powerline-taskwarrior",
    description="Powerline segments for showing information from the Taskwarrior task manager",
    version=version,
    keywords="powerline taskwarrior context prompt",
    license="MIT",
    author="German Lashevich",
    author_email="german.lashevich@gmail.com",
    url="https://github.com/zebradil/powerline-taskwarrior",
    download_url="https://github.com/zebradil/powerline-taskwarrior/tarball/{version}".format(version=version),
    packages=["powerline_taskwarrior"],
    install_requires=["powerline-status"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Terminals",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
