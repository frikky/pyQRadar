from setuptools import setup
import os

setup(
    name="pyqradar",
    version='0.2.2',
    description="QRadar API Library",
    author='@Frikkylikeme',
    author_email="fredrik_9490@hotmail.com",
    url="https://github.com/frikky/pyQRadar",
    packages=["qradar",],
    install_requires=["requests",]
)
