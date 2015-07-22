# PdfMetadataEditor
A script for editing PDF files' title and author metadata. 
Useful for correcting files before putting them on a kindle.
Could be used by a bash script to run through all pdfs in a folder and take out 
underscores in the title, for example.

Requires pdfrw and PyPdf2.

Usage: pdf_info_edit.py [-h] -f FILENAME [-a AUTHOR] [-t TITLE]
