# Kindle Highlights extractor

## What is this???
It's a small script written in Python which exports highlights, bookmarks 
and notes from the given book file to the desired output format.

Every note, highlight and bookmark are saved locally to your Kindle device in a 
file named *My Clippings.txt*, or something similar. That file has a specific
format which enables easy parsing of desired data. Script will take this file, 
parse it, and output data the one of the supported output formats.

## Which export formats does it support?
1. Tex (Latex)
Given template .tex file, it will export data in the latex file which can be
easily converted to a PDF file. 

2. Markdown
Given template it will fill the template with given data from the book.

3. Plain Text
Exports in plain .txt format.

## How to use
After you clone the repo, you will see *main.py* script in the root of the
project. Run it with: *python main.py [path_to_the_kindle_file]*
After you run it, it will scan the document and interactively ask you what data
you would like to export, and in what format.

After the program has finished, exported files will be located in the
*exporte_files* directory.
