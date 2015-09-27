from setuptools import setup

__author__ = 'netanelrevah'

main_namespace = {}
with open('pkg-name/version.py') as version_file:  # TODO: Change to package name
    exec(version_file.read(), main_namespace)
version = main_namespace['__version__']

REQUIREMENTS = []

setup(
    name='pkg-name',  # TODO: Change to package name
    version=version,
    packages=['pkg-name'],  # Don't forget to add subpackages # TODO: Change to package Name

    install_requires=REQUIREMENTS,

    author='netanelrevah',
    author_email='netanelrevah@users.noreply.github.com',
    description='Package Description',  # TODO: Change to package description
    license='GNU General Public License, version 2',
    keywords="pkg-name",  # TODO: Add package keywords
    url='https://github.com/netanelrevah/python-pkg'  # TODO: Change to package site URL
)
