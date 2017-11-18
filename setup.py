#!/usr/bin/env python
import versioneer
from setuptools import setup, find_packages
cmdclass = versioneer.get_cmdclass()


setup(
    name='PyRequirements',
    version = versioneer.get_version(),
    install_requires=[
        "pip",
    ],
    packages=find_packages('src'),
    package_dir={
        "": "src"
    },
    package_data={
        'pyrequirements': ['*.txt']
    },
    include_package_data=True,
    description="python requirements dynamic generation",
    author = "xuxingci",
    author_email="x007007007@hotmail.com",
    license='MIT',
    url='https://github.com/x007007007/pyrequirements/',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Programming Language :: Python',
    ],
    platforms=[
        "RaspberryPi", "Linux", "Unix", "Window", "MacOS"
    ],
    entry_points = {
        'console_scripts': [
            'pyrequirements=pyrequirements.main:main',
        ],
    }
)
