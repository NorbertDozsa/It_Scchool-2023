from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent

FILE_PATH = ROOT / "code1.txt"

ctime = (FILE_PATH.stat().st_ctime)

c_date_time = datetime.fromtimestamp(ctime)

print(c_date_time)