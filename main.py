# Main program
import os

from constants import PROJECT_ROOT, RAW_DATA
from raw_parser import raw_parser

raw_data_file = os.path.join(RAW_DATA, "my_clippings.txt")

parser = raw_parser.KindlePaperwhite5Parser()
parser_context = raw_parser.RawParserContext(parser)

parser_context.parse_raw(raw_data_file)


