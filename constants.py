import os

PROJECT_ROOT = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(PROJECT_ROOT, "templates")

EXPORT_FORMATS = {0: "tex (Latex)", 1: "md (Markdown)",
                  2: "txt (Plain txt file)"}

EXPORT_EXTENSIONS = {"tex": "tex", "markdown": "md", "plain": "txt"}

EXPORT_NAME_REGEX = ['[^a-zA-Z0-9 \n\.]']
