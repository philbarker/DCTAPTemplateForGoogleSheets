#!/usr/bin/env python
import requests 

def downloadSheet(docID, tabID):
    sheetURL = f'https://docs.google.com/spreadsheets/d/{docID}/gviz/tq?tqx=out:csv&sheet={tabID}'
    r = requests.get(sheetURL)
    return r

def saveFile(fname, sheet):
    with open(fname, 'wb') as f:
        f.write(sheet)
        print(f'CSV of sheet saved to {fname}.')
