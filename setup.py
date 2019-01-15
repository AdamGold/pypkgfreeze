from setuptools import setup

test_req = ['pytest==4.0.2', ]

setup(
    name='pypkgfreeze',
    version='0.1',
    packages=['src'],
    author="Adam Goldschmidt",
    author_email="adamgold7@gmail.com",
    description="Automatically inserts your currently used package versions to setup.py.",
    install_requires=[
        "Click==7.0",
    ],
    tests_require=test_req,
    setup_requires=['pytest-runner==4.2'],
    extras_require={
        'test': test_req
    },
    entry_points={'console_scripts': "pkgfreeze=src.pypkgfreeze:main"}
)
