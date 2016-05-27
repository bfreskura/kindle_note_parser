from model import book, edit_type

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



Notice that you have to add a blank line to the start of document
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

    def create_edit(self, book, meta, content):
        """
        Depending on the string, it will create appropriate
        EditType object and append to the list in the Book class object

        content param will be an empty string for bookmarks

        :param book: Book object
        :param meta Meta part of the string (string where location and date are located)
        :param content Actual content of the string (Note and highlight content)
        """
        raise NotImplementedError


class KindlePaperwhite5Parser(RawParser):
    """
    Parser implementation for Kindle Paperwhite 5.th generation
    """

    def parse_raw(self, filename):

        with open(filename, 'r') as file:
            # Read content into one string
            data_raw = file.read()

        # This will split the string by edits (Look at the raw format of the file)
        lines = data_raw.split("==========")

        books_created = {}
        for edit in lines:
            # Split edit by new line
            header, book_name, meta, blank, content, footer1 = edit.split('\n')
            # Check if this type of books exists
            if book_name not in books_created:
                books_created[book_name] = book.Book()
                books_created[book_name].book_name = book_name

            self.create_edit(meta=meta, content=content, book=books_created[book_name])
        return books_created

    def create_edit(self, meta, content, book):
        type_of_edit = meta.split(" ")[2]

        if type_of_edit.lower() == "bookmark":
            edit = edit_type.BookmarkType(bookmark_string=meta)
            book.bookmarks_list.append(edit)

        elif type_of_edit.lower() == "highlight":
            edit = edit_type.HighlightType(highlight_string=meta, content=content)
            book.highlights_list.append(edit)

        else:
            # It's a note type
            edit = edit_type.NoteType(edit_string=meta, content=content)
            book.notes_list.append(edit)


class RawParserContext:
    def __init__(self, parse_strategy):
        self.strategy = parse_strategy

    def parse_raw(self, filename):
        return self.strategy.parse_raw(filename=filename)
