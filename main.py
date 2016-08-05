# Main program

import argparse
import collections

from constants import *
from export import exporter
from raw_parser import raw_parser


def choose_export(export_index):
    """
    Choose export object based on the user input
    :param export_index: Index which was input by user
    :return: Export object
    """
    author = input(
        "Enter your name (this will appear on the top of the document): ")

    if export_index == 0:
        # TEX
        template = input("Enter Latex Template name: ")
        while template not in os.listdir(TEMPLATES) or "latex" not in template:
            template = input(
                "Templates does not exist or the wrong template format was given."
                " Please enter the template name again: ")

        return exporter.ExportTex(author_name=author,
                                  template_path=os.path.join(TEMPLATES,
                                                             template))

    elif export_index == 1:
        # Markdown
        template = input("Enter Markdown Template name: ")
        while template not in os.listdir(
                TEMPLATES) or "markdown" not in template:
            template = input(
                "Templates does not exist or the wrong template format was given."
                " Please enter the template name again: ")

        return exporter.ExportMarkdown(author_name=author,
                                       template_path=os.path.join(TEMPLATES,
                                                                  template))

    else:
        # Plain Text
        return exporter.ExportPlain(author_name=author)


def extract(book_index, books, export_dir):
    """
    Extracts book info
    :param book_index: Book index (If the index is invalid, it will be skipped)
    :param books: List of Book objects
    :return:
    """
    # Validate index
    try:
        if int(book_index) > len(books) - 1:
            print("WARNING: index '" + book_index + "' is out of range.")
            return
    except ValueError:
        print("WARNING: index '" + book_index + "' is not valid.")
        return

    book_name = next(
        v for i, v in enumerate(books.keys()) if i == int(book_index))
    print("Exporting book: " + book_name)

    # Ask for export format
    print("Choose your export format\n")
    [print('{:5d}) {}'.format(index, ex_format)) for index, ex_format in
     enumerate(EXPORT_FORMATS.values())]
    user_input = input(PROMPT_NUMBER)

    # Check if range is ok
    while int(user_input) < 0 or int(user_input) > len(EXPORT_FORMATS) - 1:
        print("Invalid number given.")
        user_input = input(PROMPT_NUMBER)
    format_exp = next(
        v for i, v in enumerate(EXPORT_FORMATS.keys()) if i == int(user_input))

    choose_export(format_exp).export(books[book_name], export_dir)
    print()


def main():
    parser = raw_parser.KindlePaperwhite5Parser()
    parser_context = raw_parser.RawParserContext(parser)
    parser = argparse.ArgumentParser()
    parser.add_argument("input_log",
                        help="Path of the file where kindle stores all notes,"
                             " highlights and bookmarks")
    parser.add_argument("output_dir", default=EXPORTED_FILES, nargs='?',
                        help="Export directory")
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        print("Output directory is invalid")
        return

    books = collections.OrderedDict(
        sorted(parser_context.parse_raw(args.input_log).items()))

    # List all books
    print("Enter one or more numbers from the list\n")
    [print('{:5d}) {}'.format(index, name)) for index, name in enumerate(books)]
    user_input = input(PROMPT_BOOK_LIST)

    for book_index in user_input.split(" "):
        extract(book_index, books, args.output_dir)


if __name__ == "__main__":
    main()
