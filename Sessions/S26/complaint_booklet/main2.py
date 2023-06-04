import pickle
import json
from pathlib import Path

from lib.complaint import Complaint
from lib.interface import CLIMenu

ROOT = Path(__file__).parent

json_dump_path = ROOT / "complaint.json"

d1 = {
    "title": "plangere",
    "text": "random text",
    "resolves": False,
    "id": 1
}

j1 = json.dumps(d1)



print(type(j1))
print(j1)