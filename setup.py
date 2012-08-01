from setuptools import setup

setup(
    name='gameshake',
    version='1.0',
    packages=[],
    include_package_data=True,
    scripts=['bin/gameshake'],

    requires=['termtool', 'httplib2', 'oauth2', 'progressbar', 'prettytable'],
    install_requires=['termtool', 'httplib2', 'oauth2', 'progressbar', 'prettytable'],
)
