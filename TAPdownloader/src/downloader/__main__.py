from .downloader import downloadSheet, saveFile
from .parser import parse_arguments

def main():
    args = parse_arguments()
    docID = args.docID
    tabID = args.tabName
    fname = args.fname
    response = downloadSheet(docID, tabID)
    if response.status_code == 200 :
        print(f'Saving sheet {tabID}.')
        saveFile(fname, response.content)
    else:
        print(response.status_code)


if __name__ == "__main__":
    main()