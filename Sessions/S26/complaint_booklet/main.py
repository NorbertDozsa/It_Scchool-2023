from lib.interface import CLIMenu
from lib.complaint import Complaint
from pathlib import Path
import pickle

ROOT = Path(__file__).parent

menu = CLIMenu("Complaint booklet", {
    "Adauga plangere": lambda : print("Plangere"),
    "Rezolva plangere": lambda : print("Rezolva plangere"),
    "Vezi plangeri nerezolvate": lambda : print("Vezi plangeri nerezolvate")
})

# menu.show_main()

c1 = Complaint("Am o problem 1", "random text")
c2 = Complaint("Am o problem 2", "random text")
c3 = Complaint("Am o problem 3", "random text")
c4 = Complaint("Am o problem 4", "random text")

l1 = [c1, c2 , c3, c4]

for i in l1:
    print(i.id, i.title)

try:
    with open(ROOT / "complaints.dump", "wb") as fout:
        pickle.dump(l1, fout)
except OSError as err:
    print(err)

dump_file = ROOT / "complaints.dump"

try:
    with open(dump_file, "rb") as fin:
        unknown = pickle.load(fin)
except OSError as err:
    print(err)
else:
    for i in unknown:
        print(i.id, i.title)
