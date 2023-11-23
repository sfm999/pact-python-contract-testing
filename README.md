# Ways to run this
**NOTE** that all commands will be run in verbose mode because I like knowing what tests ran, not just what failed. The verbose mode is triggered by adding the `-v` flag into your run command.

# Running Pytest
```bash
python -m pytest
```

## Our project structure

```
project/
|-- __init__.py  
|-- main.py  
|-- reqs.py  
|-- tests/
|   |-- test_user.py
|-- log/
|-- pacts/


|-- code/  
|   |-- __init__.py  
|   |-- calculations.py  
|-- tests/  
|   |-- __init__.py  
|   |-- test_user.py  
|   |-- test_str.py  
|-- log/
|-- pacts/
```

We will use `test_user.py` throughout our tests for consistency. Feel free to try some of them out on `test_str.py`, just don't forget to change the relevant values :grinning:

## Run all tests with discovery
```bash
python3 -m unittest discover -v
```

## Run tests by file
```bash
python3 -m unittest tests/test_user.py -v
```

## Run a specific test file by pattern
```bash
python3 -m unittest discover -p test_user.py -v
```

## Run a specific TestCase
```bash
python3 -m unittest tests.test_user.GetUserInfoContract -v
```

## Run a specific test from a specific TestCase
```bash
python3 -m unittest tests.test_user.GetUserInfoContract.test_get_user -v
```