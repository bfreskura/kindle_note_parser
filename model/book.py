import datetime


class Book:
    def __init__(self):
        self.highlights_list = []
        self.bookmarks_list = []
        self.notes_list = []
        self.book_name = ""
        self.start_reading_date = datetime.time()
        self.end_reading_date = datetime.time()

    def get_number_of_bookmarks(self):
        """
        Returns number of all bookmarks in the book
        :return: Number of bookmarks
        """
        return len(self.bookmarks_list)

    def get_number_of_highlights(self):
        """
        Returns number of all highlights in the book
        :return: Number of highlights
        """
        return len(self.highlights_list)

    def get_number_of_notes(self):
        """
        Returns number of all notes in the book
        :return: Number of notes
        """
        return len(self.notes_list)

    def get_start_and_end_reading_dates(self):
        dates = []
        [dates.append(item.date) for item in self.bookmarks_list]
        dates.sort()

        return dates[0], dates[-1]
