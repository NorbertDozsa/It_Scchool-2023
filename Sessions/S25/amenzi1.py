from pathlib import Path
import sys
from datetime import datetime

AMENDA_TEMPLATE = """
Stimate proprietar,

In data de {data} autovehiculul cu numarul de inmatriculare {numar} a fost
identificat circuland pe drumurile publice fara Rovigneta valabila.

Amenda: {amenda} RON
"""

ROOT = Path(__file__).parent
amenzi_dir_path = ROOT / "Amenzi"

file_path = ROOT / "amenzi.txt"



def get_plate_numbers(file_path):
    with open(file_path, "r") as fin:
        numbers = fin.readlines()
        for i, v in enumerate(numbers):
            numbers[i] = v.strip("\n\r\t ")
    return numbers


def get_text(numar, amenda):
    now_str = datetime.now().strftime("%d.%m.%Y")
    return AMENDA_TEMPLATE.format(data=now_str, numar=numar, amenda=amenda)


def convert_number(numar):
    return numar.lower().replace("-","_")

# def get_path():
#     for i in numbers:
#         folder_name = i.split("-")[0]
#         folder_path = amenzi_dir_path / folder_name
#         folder_path.mkdir(exist_ok=True)

try:
    amenzi_dir_path.mkdir(exist_ok=True)
except OSError as err:
    print(err)
    sys.exit(1)

try:
    numbers = get_plate_numbers(file_path)
except OSError as err:
    print(err)
else:
    for i in numbers:
        folder_name = i.split("-")[0]
        folder_path = amenzi_dir_path / folder_name
        folder_path.mkdir(exist_ok=True)
        file_name = f"Amenda_{convert_number(i)}.txt"
        # print(file_name)
        file_path = folder_path / file_name
        with open(file_path, "w") as fout:
            try:
                suma = sys.argv[1]
                fout.write(get_text(i, suma))
            except IndexError:
                print("Introduceti valoarea totala a amenzii!")
                sys.exit(1)
            