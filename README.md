# Healthify

# Slot Finder for the given week configuration

### Requirements
Python 2.7+

### Usage

1.  Move to ```<project-dir>```, create virtual environment and then activate it as


```sh
$ cd <project-dir>
$ virtualenv -p python .env
$ source .env/bin/activate
```

2. Add project to ```PYTHONPATH``` as

```sh
$ export PYTHONPATH="$PYTHONPATH:." # . corresponds to current directory(project-dir)
```

3. Then run test cases as

```sh
$ python -m unittest discover -s 'tests' -p '*.py'
```

Note: Input parameters can be changed under `tests/test_sf.py` file.
