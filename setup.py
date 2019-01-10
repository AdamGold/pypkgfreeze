from setuptools import setup

setup(
    name='pypkgfreezer',
    version='0.1',
    packages=['src'],
    install_requires=[
        "Click==7.0",
    ],
    entry_points={'console_scripts': "pkgfreeze=src.command:cli"}
)
