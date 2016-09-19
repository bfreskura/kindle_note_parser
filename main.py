import argparse
import collections
import sys

from constants import *
from export import exporter
from raw_parser import raw_parser


def choose_template(template_dir, extension):
    """
    Chooses template file from the templates directory
    :param template_dir: Templates directory path
    :param extension: Template extension (.tex, .md or .txt)
    :return: Chosen template path
    """
    print("Available templates for the specified format: ")
    available = {id: name for id, name in enumerate(os.listdir(template_dir)) if
                 name.endswith(extension)}
    if not available:
        print("No supported template files in this folder. Try again with"
              "different templates folder :)")
        sys.exit()

    [print("{}) {}".format(id, name)) for id, name in available.items()
     if name.endswith(extension)]

    selection = ""
    while selection not in list(available.keys()):
        try:
            selection = int(input("Choose format index: "))
        except ValueError:
            print("Please enter valid integer format.")
    return os.path.join(template_dir, available[selection])


def choose_export(export_index, template_dir):
    """
    Choose export object based on the user input
    :param template_dir: Templates directory path
    :param export_index: Index which was input by user
    :return: Export object
    """
    author = input(
        "Enter your name (this will appear on the top of the document): ")
    if export_index == 0:
        # TEX
        return exporter.ExportTex(author_name=author,
                                  template_path=choose_template(
                                      template_dir=template_dir,
                                      extension=EXPORT_EXTENSIONS['tex']))
    elif export_index == 1:
        # Markdown
        return exporter.ExportMarkdown(author_name=author,
                                       template_path=choose_template(
                                           template_dir=template_dir,
                                           extension=EXPORT_EXTENSIONS[
                                               'markdown']))
    else:
        # Plain Text
        return exporter.ExportPlain(author_name=author)


def extract(book_index, books, export_dir, templates_dir):
    """
    Extracts book info
    :param templates_dir: Templates directory path
    :param export_dir: Book export directory
    :param book_index: Book index (If the index is invalid, it will be skipped)
    :param books: List of Book objects
    :return:
    """
    # Validate index
    try:
        if book_index > len(books) - 1:
            print("WARNING: index '" + book_index + "' is out of range.")
            return
    except ValueError:
        print("WARNING: index '" + book_index + "' is not valid.")
        return

    selected_book_name, selected_book_iterator = list(books.items())[book_index]
    print("Exporting book: " + selected_book_name)

    # Ask for export format
    print("Choose your export format\n")
    [print('{:5d}) {}'.format(index, ex_format)) for index, ex_format in
     enumerate(EXPORT_FORMATS.values())]
    user_input = int(input(PROMPT_NUMBER))

    # Check if range is ok
    while user_input not in range(len(EXPORT_FORMATS)):
        print("Invalid number given. Try again.")
        user_input = int(input(PROMPT_NUMBER))
    format_exp = list(EXPORT_FORMATS.items())[user_input][0]

    choose_export(format_exp, templates_dir).export(selected_book_iterator,
                                                    export_dir)
    print()


def check_path_exists(dir_list):
    """
    Checks if all directory/file paths are valid
    :param dir_list: List of directories/files to check
    :return: True if all valid, False otherwise
    """
    for dir in dir_list:
        if not os.path.exists(dir):
            print(dir + " directory is invalid")
            return False
    return True


def main():
    parser = raw_parser.KindlePaperwhite5Parser()
    parser_context = raw_parser.RawParserContext(parser)
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-log",
                        help="Path of the file where kindle stores all notes,"
                             " highlights and bookmarks", type=str,
                        required=True)
    parser.add_argument("--templates-dir",
                        help="Export format template file", type=str,
                        required=True)
    parser.add_argument("--output-dir", type=str, help="Export directory",
                        required=True)
    args = parser.parse_args()
    if not check_path_exists(
            [args.templates_dir, args.output_dir, args.input_log]):
        sys.exit()

    books = collections.OrderedDict(
        sorted(parser_context.parse_raw(args.input_log).items()))

    # List all books
    print("Enter one or more numbers from the list\n")
    [print('{:5d}) {}'.format(index, name)) for index, name in enumerate(books)]
    user_input = input(PROMPT_BOOK_LIST)

    for book_index in user_input.split(" "):
        extract(int(book_index), books, args.output_dir, args.templates_dir)


if __name__ == "__main__":
    main()
