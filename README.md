# pypkgfreezer

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
test_req = ['pytest==4.0.2', ]
setup(
    name='pypkgfreeze',
    install_requires=[
        "Click==7.0",
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
