#!/usr/bin/env python

import sys
import argparse
from PyPDF2 import PdfFileReader
from pdfrw import IndirectPdfDict, errors, PdfReader, PdfWriter

if __name__ == "__main__":
    argParser = argparse.ArgumentParser(
        description='PDF Metadata Editor')

    argParser.add_argument("-f", "--filename", help="Filename of PDF", required=True)
    argParser.add_argument("-a", "--author", help="Author of PDF")
    argParser.add_argument("-t", "--title", help="Title of PDF")

    args = argParser.parse_args()

    if args.filename is None:
        print "No filename given"
        sys.exit(-1)

    fileInfo = PdfFileReader(file(args.filename)).getDocumentInfo()
    
    if args.author is None:
        author = str(fileInfo.author) if fileInfo.author is not None else None
    else:
        author = args.author

    if args.title is None:
        title = str(fileInfo.title) if fileInfo.title is not None else None
    else:
        title = args.title

    try:
        metaWriter = PdfWriter()
        metaWriter.addpages(PdfReader(args.filename).pages)
        metaWriter.trailer.Info = IndirectPdfDict(Title=title, Author=author)
        metaWriter.write(args.filename)
    except errors.PdfParseError as e:
        print "Error parsing PDF:", e.msg
        sys.exit(-1)

    sys.exit(0)