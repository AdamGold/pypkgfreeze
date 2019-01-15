# pypkgfreeze

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Automatically inserts your currently used package versions to setup.py.

### Example

#### Old setup.py

```py
from setuptools import setup
test_req = ['pytest', ]
setup(
    name='pypkgfreeze',
    install_requires=[
        "Click",
    ],
    tests_require=test_req,
    extras_require={
        'test': test_req
    }
)
```

#### New setup.py

```py
from setuptools import setup
test_req = ['pytest==4.0.2', ]  # ADDED VERSION HERE
setup(
    name='pypkgfreeze',
    install_requires=[
        "Click==7.0",  # AND HERE
    ],
    tests_require=test_req,
    extras_require={
        'test': test_req
    }
)
```

## Usage

`pkgfreeze`. It's that simple.

## Installation

```py
pip install pypkgfreeze
```

## Contributing

Thanks! Please read the [`CONTRIBUTING.md`](https://github.com/AdamGold/pypkgfreeze/blob/master/CONTRIBUTING.md) file.
