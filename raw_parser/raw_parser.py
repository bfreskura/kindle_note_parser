from model import book, edit_type


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

        :param book: Book class object
        :param meta Meta part of the string (string where location and date are located)
        :param content Actual content of the string (Note and highlight content)
        """
        raise NotImplementedError


class KindlePaperwhite5Parser(RawParser):
    """
    Parser implementation for Kindle Paperwhite 5.th generation
    """

    def parse_raw(self, filename):

        with open(filename, 'r', encoding='utf-8') as file:
            # Read content into one string
            data_raw = file.read()

        # This will split the string by edits (Look at the raw format of the file)
        # Last string is deleted  because there is no content after the last
        # ====== in the file.
        lines = data_raw.split("==========")[0:-1]
        # Append new line so all lines have \n at the beginning
        lines[0] = "\n" + lines[0]

        books_created = {}
        for edit in lines:
            # Split edit by new line
            header, book_name, meta, blank, content, footer1 = edit.split('\n')
            # Remove Byte Order Mark (BOM) code
            book_name = book_name.replace(u'\ufeff', '')
            # Check if this type of books exists
            if book_name not in books_created:
                books_created[book_name] = book.Book()
                books_created[book_name].book_name = book_name

            self.create_edit(meta=meta, content=content,
                             book=books_created[book_name])
        return books_created

    def create_edit(self, meta, content, book):
        type_of_edit = meta.split(" ")[2]

        if type_of_edit.lower() == "bookmark":
            edit = edit_type.BookmarkType(bookmark_string=meta)
            book.bookmarks_list.append(edit)

        elif type_of_edit.lower() == "highlight":
            edit = edit_type.HighlightType(highlight_string=meta,
                                           content=content)
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
