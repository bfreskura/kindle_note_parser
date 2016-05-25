# Main program

import argparse
import os
from raw_parser import raw_parser
from constants import EXPORT_FORMATS, TEMPLATES, EXPORTED_FILES
from export import exporter


def choose_export(export_index):
    """
    Chooes export object based on the user input
    :param export_index: Index which was input by user
    :return: Export object
    """
    author = input("Enter your name (this will appear on the top of the document): ")

    if export_index == 0:
        # TEX
        template = input("Enter Template name: ")
        if not template:
            template = "template1.txt"

        return exporter.ExportTex(author_name=author,
                                  template_path=os.path.join(TEMPLATES, template))

    elif export_index == 1:
        # Markdown
        pass
    else:
        # Plain Text
        pass


# raw_data_file = os.path.join(RAW_DATA, "my_clippings.txt")

parser = raw_parser.KindlePaperwhite5Parser()
parser_context = raw_parser.RawParserContext(parser)

parser = argparse.ArgumentParser()
parser.add_argument("input_log", help="Path of the file where kindle stores all notes, highlights and bookmarks")
args = parser.parse_args()

books = parser_context.parse_raw(args.input_log)

# List all books
print("Enter one number from the list:\n")
[print('{:5d}) {}'.format(index, name)) for index, name in enumerate(books)]
user_input = input("\nEnter number: ")

# Check if range is ok
while int(user_input) < 0 or int(user_input) > len(books) - 1:
    print("Invalid number given.")
    user_input = input("Enter number: ")
book = next(v for i, v in enumerate(books.keys()) if i == int(user_input))

# Ask for export format
print("Choose your export format\n")
[print('{:5d}) {}'.format(index, format)) for index, format in enumerate(EXPORT_FORMATS.values())]
user_input = input("\nEnter number: ")

# Check if range is ok
while int(user_input) < 0 or int(user_input) > len(EXPORT_FORMATS) - 1:
    print("Invalid number given.")
    user_input = input("Enter number: ")
format_exp = next(v for i, v in enumerate(EXPORT_FORMATS.keys()) if i == int(user_input))

choose_export(format_exp).export(books[book], EXPORTED_FILES)
