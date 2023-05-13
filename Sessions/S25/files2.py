from pathlib import Path
import os

ROOT = Path(__file__).parent

input_file_path = ROOT / "git.txt"

try:
    with open(input_file_path, 'r') as fin:
        print(fin.tell())
        print(fin.read())
        print(fin.tell())
        print(fin.read())        
        fin.seek(0, os.SEEK_SET)
except OSError as err:
    print(err)