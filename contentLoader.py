import json
from pathlib import Path


def load_content_file(filename):
    file_path = Path(__file__).with_name("content") / filename
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)
