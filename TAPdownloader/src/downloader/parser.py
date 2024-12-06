from argparse import ArgumentParser

# defaults
fileName = "tap.csv"
tabName = "tap"
docID = None

def parse_arguments():
    ap = ArgumentParser(
        prog = "TAPdownloader",
        description = "Download a DC TAP froma google sheets."
    )
    ap.add_argument("docID", type=str, metavar="<docID>",)
    ap.add_argument(
        "-t",
        "--tabName",
        type=str,
        metavar="<tabName>",
        default=tabName,
    ),
    ap.add_argument(
        "fname",
        nargs='?',
        type=str,
        metavar="<fname>",
        default=fileName,
    )
    return ap.parse_args()