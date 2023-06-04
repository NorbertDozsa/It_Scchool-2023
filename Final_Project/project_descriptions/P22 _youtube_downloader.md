## YouTube MP3 Downloader API

### Descriere
Acest proiect constă în dezvoltarea unui API pentru convertirea melodiilor de pe YouTube în format MP3. API-ul va permite dezvoltatorilor să integreze funcționalitatea de convertire a melodiilor în aplicațiile lor prin intermediul cererilor HTTP.

### Interfața
REST API

### Endpoints
#### GET /convert
Parametri:
- `url` (string, obligatoriu): URL-ul videoclipului YouTube pe care se dorește conversia în format MP3.

Aceast endpoint permite dezvoltatorilor să trimită un URL al videoclipului YouTube pentru a iniția conversia melodiei în format MP3. Parametrul `url` trebuie să conțină URL-ul videoclipului YouTube.

Răspunsul va conține un ID unic care poate fi folosit ulterior pentru a verifica statusul conversiei și pentru a obține URL-ul de descărcare a fișierului MP3.

#### GET /status/{id}
Parametri:
- `id` (string, obligatoriu): ID-ul unic returnat de cererea GET /convert.

Aceast endpoint permite dezvoltatorilor să verifice statusul conversiei după ID-ul returnat de cererea GET /convert. Răspunsul va conține informații despre stadiul conversiei, cum ar fi "eroare", "în progres" sau "finalizat".

#### GET /download/{id}
Parametri:
- `id` (string, obligatoriu): ID-ul unic returnat de cererea GET /convert.

Aceast endpoint permite dezvoltatorilor să descarce fișierul MP3 după ID-ul returnat de cererea GET /convert. Răspunsul va conține fișierul MP3 convertit.

### Gestionarea erorilor
API-ul trebuie să gestioneze corect erorile care pot apărea în timpul conversiei și să furnizeze răspunsuri adecvate în cazul unor situații neașteptate sau erori de rulare. Mesajele de eroare trebuie să ofere informații relevante pentru depanare.

### Documentație
API-ul trebuie să fie însoțit de documentație detaliată care descrie modul de utilizare, inclusiv exemple de cereri și răspunsuri. Aceasta va ajuta dezvoltatorii să înțeleagă cum să integreze funcționalitatea de conversie a melodiilor în format MP3 în aplicațiile lor. Aceste se poate genera automat de unele framework-uri.

### Cerințe non-funcționale
- Implementați un sistem de înregistrare (logging) pentru a putea urmări acțiunile utilizatorilor și pentru a diagnostica eventualele probleme.
- Verificați URL-urile furnizate pentru a se asigura că sunt valide și corespund formatului specificat pentru videoclipurile YouTube.
- Se va utiliza o baza de date SQLite pentru a memora ce URL-uri s-au convertit, unde a fost salvata melodia, link catre melodie, id-ul operatiei si statusul.

Succes în dezvoltarea proiectului!