import os

PROJECT_ROOT = os.path.dirname(__file__)
RAW_DATA = os.path.join(PROJECT_ROOT, "raw")
TEMPLATES = os.path.join(PROJECT_ROOT, "latex_templates")
EXPORTED_FILES = os.path.join(PROJECT_ROOT, "exported_files")

EXPORT_FORMATS = {0: "tex (Latex)", 1: "md (Markdown)", 2: "txt (Plain text)"}
