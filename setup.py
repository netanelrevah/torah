from setuptools import setup, find_packages

__author__ = 'netanelrevah'

main_namespace = {}
with open('torah/version.py') as version_file:
    exec(version_file.read(), main_namespace)
version = main_namespace['__version__']

REQUIREMENTS = []

setup(
    name='torah',
    version=version,
    packages=find_packages(),

    install_requires=REQUIREMENTS,

    author='netanelrevah',
    author_email='netanelrevah@users.noreply.github.com',
    description='Package for researching the Torah',
    license='GNU General Public License, version 2',
    keywords="torah research serialization jewish",
    url='https://github.com/netanelrevah/torah'
)
