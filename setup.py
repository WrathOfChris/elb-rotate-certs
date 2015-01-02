import os
import re
from elb_rotate_certs import __version__
from setuptools import setup, find_packages

setup(
    name='elb-rotate-certs',
    version=__version__,
    author="Chris Maxwell",
    author_email="chris@wrathofchris.com",
    description="ELB Certificate Rotation Tool",
    url = "https://github.com/WrathOfChris/elb-rotate-certs",
    download_url = 'https://github.com/WrathOfChris/elb-rotate-certs/tarball/%s' % __version__,
    license="Apache",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'boto'
    ],
    entry_points={
        "console_scripts": [
            "elb-rotate-certs = elb_rotate_certs.cli:elb_rotate_certs"
        ]
    }
)
