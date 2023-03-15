auto = {
    "marca": "Audi",
    "model": "A4",
    "usi": 4
}

sablon = "Detin o masina marca {}, model {} si are {} usi."

print(sablon.format(auto["marca"], auto["model"], auto["usi"]))

ticket = {
    "s_plecare": "Bucuresti Nord",
    "s_sosire": "Iasi",
    "data_plecare": "27.02.2023",
    "data_sosire": "27.02.2023",
    "ora_plecare": "19:30",
    "ora_sosire": "23:30",
    "pret": 98.45,
    "loc": True,
    "vagon": "2",
    "scaun": "34"
}