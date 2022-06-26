## GMC-300/GMC-320 python interface

Python interface for a GQ GMC-300, GMC-300E PLUS, GMC-320 geiger counters.

For the most up to date information refer to the original GQ [website](http://www.gqelectronicsllc.com/comersus/store/download.asp)

### Installation
```bash
pipenv install
# or if you prefer `.venv` to be in the same directory:
PIPENV_VENV_IN_PROJECT=1 pipenv install
```


### Run
```bash
pipenv run start
```

### Example output:
```bash
detecting port...
port detected: /dev/cu.usbserial-210
version: GMC-300Re 4.22
serial: F4880B542489
CPM: 17
```