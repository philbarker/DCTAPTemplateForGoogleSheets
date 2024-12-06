# Downloader (in devleopment)

This directory holds a python script that can be used to download the sheets form a Google sheet based on the DCTAP template and save then as csv files with the default names used by TAP2SHACL.

## Usage
Install into a venv.

```
$ downloadtap -t about 1FzJOmM57n8m4oEQS10DerW9PFnJLy2-RDtKPDoKstmg about.csv
Saving sheet about.
CSV of sheet saved to about.csv.
```

if the tab name and file name are omitted the tab named "tap" will be saved as a csv in the file "tap.csv":

```
$ downloadtap 1FzJOmM57n8m4oEQS10DerW9PFnJLy2-RDtKPDoKstmg
Saving sheet tap.
CSV of sheet saved to tap.csv.
```

use -h option for help:

```
$ downloadtap -h
usage: TAPdownloader [-h] [-t <tabName>] <docID> [<fname>]

Download a DC TAP froma google sheets.

positional arguments:
  <docID>
  <fname>

options:
  -h, --help            show this help message and exit
  -t <tabName>, --tabName <tabName>

```