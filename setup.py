# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in redtheme_v13b/__init__.py
from redtheme_v13b import __version__ as version

setup(
	name='redtheme_v13b',
	version=version,
	description='Red Theme for Frappe v13b',
	author='Hashir',
	author_email='hashirabdulla@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
