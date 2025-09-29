# Aplikacija za računanje harmonijskog kromatskog broja grafa

Aplikacija omogućava vizualno interaktivno definiranje grafa, izradu veza i bojanje vrhova s minimalnim brojem boja. Korisnici mogu postavljati čvorove, povezivati vrhove, alternativno unijeti graf putem tekstualne datoteke (lista susjedstva) te izravno prikazati harmonijski kromatski broj u novom prozoru.

Ova aplikacija je idealna za edukaciju o teoriji grafova, jer nudi praktičan način za eksperimentiranje i vizualizaciju svojstava grafa. Također je korisna u istraživanju i razvoju algoritama za optimizaciju grafova.

---

## Korištenje

1. Unesite graf **ručno** (postavljanjem čvorova i povezivanjem vrhova) **ili** učitajte **listu susjedstva** iz tekstualne datoteke.  
2. Pritiskom na gumb **„Compute harmonic index and draw colors“**:
   - prikaže se **novi prozor** s harmonijskim kromatskim brojem unesenog grafa (npr. `5`),
   - čvorovi se **obojaju** prema dobivenom bojanju.

---

## Tehnologije

- **Python**
- **Tkinter** (grafičko i korisničko sučelje)

---

## Struktura programa

Glavni dio aplikacije je klasa **`DotConnectorApp`**, koja sadrži sve metode za interakciju s korisnikom, crtanje grafa i izračun harmonijskog kromatskog broja.

### Ključne metode

- `__init__` – inicijalizacija korisničkog sučelja, postavljanje canvas-a i dodavanje gumbova (izračun, uvoz grafa, brisanje platna).
- `show_info_window` – prikaz prozora s uputama za korištenje.
- `place_dot` – dodavanje točke (čvora) na mjesto klika.
- `connect_dot` – povezivanje dviju točaka (vrhova) linijom.
- `get_nearest_dot` – pronalazak najbliže točke u odnosu na poziciju miša.
- `import_graph` – uvoz grafa iz tekstualne datoteke koja sadrži listu susjedstva.
- `create_dots_from_graph` – stvaranje čvorova i veza na platnu na temelju uvezenog grafa.
- `compute_and_draw` – izračun harmonijskog kromatskog broja i bojanje čvorova.
- `display_harmonic_index` – prikaz prozora s izračunatim harmonijskim kromatskim brojem.
- `execute_coloring` – bojanje čvorova na platnu prema izračunatom bojanju.
- `generate_graph` – generiranje internog modela grafa iz veza između čvorova.
- `clear_canvas` – brisanje svih elemenata s platna i reset stanja aplikacije.

---

## Algoritamska funkcija

**`dodaj_vrh`** – rekurzivno dodaje čvorove u graf i provjerava mogućnosti bojanja čvorova tako da se zadovolje uvjeti harmonijskog kromatskog broja.

**Parametri:**
- `L` – lista boja dodijeljenih čvorovima
- `boje` – trenutni broj boja korištenih za bojanje
- `Susjedi` – lista susjedstva za svaki čvor
- `n` – ukupan broj čvorova u grafu
- `susjedi_boje` – lista susjedstva za svaku boju
