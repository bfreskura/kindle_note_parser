# Kindle Data Exporter

## What is this sorcery?
It's a small script written in Python which exports highlights, bookmarks
and notes from the given book file to the desired output format.

Every note, highlight and bookmark is saved locally to your Kindle device in a
file named *My Clippings.txt*, or something similar. That file has a specific
format which enables easy parsing of desired data. Script will take this file,
parse it, and output data in one of the supported output formats.

*My Clippings.txt* looks something likes this:
```

The 5 Elements of Effective Thinking (Burger, Edward B.;Starbird, Michael)
- Your Bookmark on Location 111 | Added on Monday, August 10, 2015 7:26:42 PM


==========
The Intelligent Investor, Rev. Ed (Graham, Benjamin;Jason Zweig;Warren E. Buffett)
- Your Bookmark on Location 6152 | Added on Monday, August 10, 2015 8:06:01 PM


==========
The 5 Elements of Effective Thinking (Burger, Edward B.;Starbird, Michael)
- Your Bookmark on Location 289 | Added on Tuesday, August 11, 2015 4:49:23 PM


==========
The 5 Elements of Effective Thinking (Burger, Edward B.;Starbird, Michael)
- Your Bookmark on Location 607 | Added on Tuesday, August 11, 2015 5:19:06 PM


==========
The 5 Elements of Effective Thinking (Burger, Edward B.;Starbird, Michael)
- Your Highlight on Location 718-718 | Added on Wednesday, August 12, 2015 7:17:46 AM

perspiration, the perspiration was the process of incrementally
==========
The 5 Elements of Effective Thinking (Burger, Edward B.;Starbird, Michael)
- Your Bookmark on Location 897 | Added on Wednesday, August 12, 2015 7:33:04 AM


==========
```

## Which export formats does it support?
1. TeX (LaTeX)
  * Given *.tex* template file, it will export data in the latex file which can be
easily converted to a PDF file.
 * For converting *tex* to *PDF* take a look at [this](https://en.wikibooks.org/wiki/LaTeX/Export_To_Other_Formats#Convert_to_PDF)

2. Markdown
  * Given *.md* template file, it will fill the template with given data from the book.

3. Plain Text
  * Exports in plain *.txt* format.

## How to use
After you clone the repository, you will see *export.py* script in the root of the
project. Run it with:
```
python3 export.py --input-log [/My/Clippings/path] --output-dir [/export/directory] --templates-dir [templates/]
```
After you run it, it will scan the document and interactively ask you what data
you would like to export and in which format.

You can run ``` python3 export.py -h``` to show the help menu.

### Template files
You have to set the templates folder directory when running the script. You can
take a look at example templates in the *templates* directory if you wish to
create your own templates. You **DO NOT** need a template file when using the **plain
text** format.

#### **Important**
When creating your own templates, add **.tex**/**.md**/**.txt** extensions at the end
of the template file name, or the template won't be recognised.

### Dates
Start and finish day of reading are dates when the first and the last
bookmarks in the book were made.

### Examples
You can see some of the exported examples in the *examples* directory.

## Requirements
The only requirements is Python3 (tested on Python 3.5.2)

## Versions of Kindle devices supported
The script was tested on Kindle Paperwhite generation 5. I don't know how other versions of Kindle 
devices save this sort of data (I assume it's not very different from this one), but feel free to
email me if you find some differences on other Kindle devices.

## Author
[Bartol Freškura](https://hr.linkedin.com/in/bfreskura)
