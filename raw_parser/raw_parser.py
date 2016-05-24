import re
import os
from model import book

"""
Parses raw kindle highlights document

Example of the document:

The 5 Elements of Effective Thinking (Burger, Edward B.;Starbird, Michael)
- Your Bookmark on Location 111 | Added on Monday, August 10, 2015 7:26:42 PM


==========
﻿The Intelligent Investor, Rev. Ed (Graham, Benjamin;Jason Zweig;Warren E. Buffett)
- Your Bookmark on Location 6152 | Added on Monday, August 10, 2015 8:06:01 PM


==========
﻿The 5 Elements of Effective Thinking (Burger, Edward B.;Starbird, Michael)
- Your Bookmark on Location 289 | Added on Tuesday, August 11, 2015 4:49:23 PM


==========
﻿The 5 Elements of Effective Thinking (Burger, Edward B.;Starbird, Michael)
- Your Bookmark on Location 607 | Added on Tuesday, August 11, 2015 5:19:06 PM


==========
The 5 Elements of Effective Thinking (Burger, Edward B.;Starbird, Michael)
- Your Highlight on Location 718-718 | Added on Wednesday, August 12, 2015 7:17:46 AM

perspiration, the perspiration was the process of incrementally
==========
The 5 Elements of Effective Thinking (Burger, Edward B.;Starbird, Michael)
- Your Bookmark on Location 897 | Added on Wednesday, August 12, 2015 7:33:04 AM

"""


class RawParser:
    def parse_raw(self, filename):
        """
        Parses raw Kindle highlights file.
        Given file must be in valid format or it could crash the program

        :param filename: Path to the file
        :return: List of Book class files
        """
        raise NotImplementedError


class KindlePapewhite5Parser(RawParser):
    """
    Parser implementation for Kindle Paperwhite 5.th generation
    """

    def parse_raw(self, filename):
        with open(filename, 'r') as file:
            # Load file into one string and replace the newline with dollars
            # so it can be split later
            input = file.read().replace('\n', '\n')

        # This will split data by edits
        lines = input.split("==========")

        books_created = dict()
        for i, edit in enumerate(lines):

            # Split edit by new line
            content = edit.split('\n')

            # Check if this type of books exists
            if content[1] not in books_created:
                book_new = book.Book()
                books_created[content[1]] = book_new
                print(content[1])
            else:
                book_old = books_created[content[1]]


class RawParserContext:
    def __init__(self, parse_strategy):
        self.strategy = parse_strategy

    def parse_raw(self, filename):
        self.strategy.parse_raw(filename)
