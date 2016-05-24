# Main program
import os

from constants import RAW_DATA, TEMPLATES, EXPORTED_FILES
from raw_parser import raw_parser
from export import exporter

raw_data_file = os.path.join(RAW_DATA, "my_clippings.txt")

# parsing
parser = raw_parser.KindlePaperwhite5Parser()
parser_context = raw_parser.RawParserContext(parser)

books = parser_context.parse_raw(raw_data_file)
latex = exporter.ExportTex(author_name="Bartol Freškura", template_path=os.path.join(TEMPLATES, "template1.txt"))
name = 'How to Win Friends and Influence People (Dale Carnegie)'
latex.export(books[name], EXPORTED_FILES)
