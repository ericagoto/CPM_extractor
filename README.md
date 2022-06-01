# CPM_extractor
Pyhton package to modify the CPM column in a kml file

**Author**: [Sangwon Lim](https://github.com/sum1lim)

## Getting Started
### Downloading the Repository
Download this repository using the green `Code` button at the top right 
OR
```
$ git clone https://github.com/sum1lim/CPM_extractor.git
```

### Install the Package in a Python Virtual Environment
#### Windows
Double-click on `install` batch script to install.

Double-click on `uninstall` batch script to uninstall.

#### Linux & OSX
Navigate to the parent directory in terminal, `CPM_extractor`, in the command line interface and run the following commands.
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install .
```
Remove `venv` to uninstall
```
$ rm -r venv
```

## Graphical User Interface (GUI)
### Windows
Double-click on `gui` batch script
### Linux & OSX
```
$ gui
```

## Command-line User Interface (CLI*)
#### *CLI is not recommended for Windows

```
$ CPM_extractor --help                                       
usage: CPM_extractor [-h] --input INPUT [INPUT ...] --column COLUMN

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT [INPUT ...]
                        Path to time-series data file (csv)
  --column COLUMN       Name of the column to modify
```
Command Line:
```
$ CPM_extractor --input [Path(s) to input file (kml)] --column [Name of the column to modify]
```
Example(s):
```
# Single Input
$ CPM_extractor --input ./data/13960228.log.kml --column description

# Multiple inputs
$ CPM_extractor --input ./data/13960228.log.kml ./data/13961002.log.kml --column description

# Multiple inputs (Every file in a directory)
$ CPM_extractor --input ./data/* --column description
```
