from setuptools import setup

test_req = ['pytest==4.0.2', ]

setup(
    name='pypkgfreezer',
    version='0.1',
    packages=['src'],
    install_requires=[
        "Click",
    ],
    tests_require=test_req,
    setup_requires=['pytest-runner==4.2'],
    extras_require={
        'test': test_req
    },
    entry_points={'console_scripts': "pkgfreeze=src.command:cli"}
)
