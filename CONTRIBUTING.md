# Contributing

:tada:Thank you so much for taking the time to contribute:tada:

## Wait!

Before trying to help please tell us what's wrong.
Please check if there is an [open issue](https://github.com/AdamGold/pypkgfreeze/issues) with your problem.
If there isn't one, [create one](https://github.com/AdamGold/pypkgfreeze/issues/new/choose).

If you still want to contribute! Then you will need to:

## Create an enviroment

Clone the repository and run inside it:

```sh
python -m venv venv # Create a virtual enviroment
source venv/bin/activate # Activate it
pip install -e .[test] # Install the project in an [e]ditable way
```

## Write the tests (before or after the actual solution? Your call)

Inside the `tests/` folder:

```py
def test_something_you_wanna_test(fixtures_you_need):
    # your code here
```

## Write your solution

You can add your code inside `pypkgfreeze.py` or a new file (make sure you import it in `__init__.py`). The `main` method is where the magic happens - it is the command that is being run when you type `pkgfreeze`.

## Run the tests

Activate your virtual enviroment and run

```sh
pytest
```

To run a specific test run

```sh
pytest -k <test name>
```
