import os 
import shutil
from pathlib import Path

ROOT = Path(__file__).parent

os.rename(ROOT / "code.txt", ROOT / "code1.txt")