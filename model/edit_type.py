from datetime import datetime


class EditType:
    """
    EditType interface for all types of user generated content on the kindle device
    Some include: Bookmarks, Notes and Highlights. More content could be available but I am not aware of it
    Attributes which it must contain: Date and content
    """

    def pretty_format(self):
        """
        Returns all information packed into a pretty format string
        :return:
        """

    def parse_edit_location(self, raw_data):
        """
        Parse edit Location or location range
        :param raw_data: String containing location
        :return: Location or location string value
        """

    def parse_edit_date(self, raw_data):
        """
        Parse edit date
        :param raw_data: String containing location
        :return: datetime object
        """


class HighlightType(EditType):
    """
    Created for Kindle Paperwhite gen 5.
    Highlight Edit class.
    Contains content of the highlight, location range of the highlight and the date
    """

    def __init__(self, highlight_string, content):
        self.content = content
        self.date = self.parse_edit_date(highlight_string)
        self.location = self.parse_edit_location(highlight_string)

    def pretty_format(self):
        pass

    def parse_edit_date(self, data):
        """
        Example of input:
        - Your Highlight on Location 6778-6779 | Added on Monday, August 17, 2015 7:38:34 AM

        :param data:
        :return:
        """
        date_part = data.split("|")
        return datetime.strptime(date_part[1], " Added on %A, %B %d, %Y %I:%M:%S %p")

    def parse_edit_location(self, data):
        """
        Example of input:
        - Your Highlight on Location 6778-6779 | Added on Monday, August 17, 2015 7:38:34 AM

        :param data:
        :return:
        """
        return data.split("|")[0].split(" ")[5]


class NoteType(EditType):
    """
    Created for Kindle Paperwhite gen 5.
    Highlight Edit class.
    Note Edit class
    Contains content of the Note, location of the note and the date
    """

    def __init__(self, edit_string, content):
        self.content = content
        self.date = self.parse_edit_date(edit_string)
        self.location = self.parse_edit_location(edit_string)

    def pretty_format(self):
        pass

    def parse_edit_date(self, data):
        """
        Example of input:
        - Your Note on Location 4555 | Added on Wednesday, February 24, 2016 8:28:14 AM

        :param data:
        :return:
        """
        date_part = data.split("|")
        return datetime.strptime(date_part[1], " Added on %A, %B %d, %Y %I:%M:%S %p")

    def parse_edit_location(self, data):
        """
        Example of input:
        - Your Note on Location 4555 | Added on Wednesday, February 24, 2016 8:28:14 AM

        :param data:
        :return:
        """
        return data.split("|")[0].split(" ")[5]


class BookmarkType(EditType):
    """
    Created for Kindle Paperwhite gen 5.
    Highlight Edit class.
    Bookmark Edit class
    Contains location of the bookmark and the date
    """

    def __init__(self, bookmark_string):
        self.date = self.parse_edit_date(bookmark_string)
        self.location = self.parse_edit_location(bookmark_string)

    def pretty_format(self):
        pass

    def parse_edit_date(self, data):
        """
        Example of input:
        - Your Bookmark on Location 3021 | Added on Wednesday, February 17, 2016 1:49:13 PM

        :param data:
        :return:
        """
        date_part = data.split("|")
        return datetime.strptime(date_part[1], " Added on %A, %B %d, %Y %I:%M:%S %p")

    def parse_edit_location(self, data):
        """
        Example of input:
        - Your Bookmark on Location 3021 | Added on Wednesday, February 17, 2016 1:49:13 PM

        :param data:
        :return:
        """
        return data.split("|")[0].split(" ")[5]
