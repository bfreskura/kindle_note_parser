import datetime


class Book:
    def __init__(self):
        self.highlights_list = []
        self.bookmarks_list = []
        self.notes_list = []
        self.book_name = ""
        self.start_reading_date = datetime.datetime.now().date()
        self.end_reading_date = datetime.datetime.now().date()

    def bookmarks_count(self):
        """
        Returns number of all bookmarks in the book
        :return: Number of bookmarks
        """
        return len(self.bookmarks_list)

    def highlights_count(self):
        """
        Returns number of all highlights in the book
        :return: Number of highlights
        """
        return len(self.highlights_list)

    def notes_count(self):
        """
        Returns number of all notes in the book
        :return: Number of notes
        """
        return len(self.notes_list)

    def start_finish_reading_date(self):
        """
        Extracts first and last bookmark date. Dates are sorted in chronological order and then extracted.
        :return: First and last date from the bookmark list
        """
        dates = [item.date for item in self.bookmarks_list]
        dates.sort()

        return dates[0], dates[-1]
