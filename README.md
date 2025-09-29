Aplikacija za računanje harmonijskog kromatskog broja grafa omogućava korisnicima vizualno interaktivno iskustvo za definiranje grafa, izradu veza i bojanje vrhova s minimalnim brojem boja. Korisničko sučelje omogućava postavljanje čvorova, povezivanje vrhova, alternativno unos grafa putem tekstualne datoteke koja sadrži listu susjedstva te izravno prikazivanje harmonijskog kromatskog broja u novom prozoru. Ova aplikacija je idealna za edukaciju o teoriji grafova, jer korisnicima nudi praktičan način za eksperimentiranje s grafovima i vizualizacijom njihovih svojstava. Također je korisna u istraživanju i razvoju algoritama za optimizaciju grafova
 
Slika 3.3 Izgled prozora aplikacije.
Na slici 4.1 su prikazani svi prozori aplikacije: Prozor u kojem se unosi graf ili ručno ili tablicom susjedstva te vidimo kako graf izgleda nakon bojanja i prozor s uputama za korištenje. Nakon pritiska gumba „Compute harmonic index and draw colors“ iskoči novi prozor unutar kojeg je naveden harmonijsko kromatski broj unesenog grafa, u ovom slučaju je taj broj 5. 
Aplikacija je razvijena u programskom jeziku Python uz korištenje biblioteke Tkinter za grafičko i korisničko sučelje. Program se sastoji od nekoliko ključnih komponenti.
Klasa DotConnectorApp predstavlja glavni dio aplikacije i sadrži sve potrebne metode za interakciju s korisnikom, crtanje grafa te izračun harmonijskog kromatskog broja. Metode klase su :
•	__init__: Inicijalizacija korisničkog sučelja, postavljanje canvas-a za crtanje te dodavanje gumba za izračun, uvoz grafa i brisanje platna.
•	show_info_window: Prikazuje prozor s uputama za korištenje aplikacije.
•	place_dot: Dodaje točku (čvor) na platno na mjestu gdje je korisnik kliknuo.
•	connect_dot: Povezuje dvije točke (čvorove) linijom (vezom) na temelju korisničkog klika.
•	get_nearest_dot: Pronalazi najbližu točku (čvor) na platnu u odnosu na poziciju miša.
•	import_graph: Uvoz grafa iz tekstualne datoteke koja sadrži susjedstvo čvorova.
•	create_dots_from_graph: Stvara čvorove i veze na platnu na temelju uvezenog grafa.
•	compute_and_draw: Izračunava harmonijski kromatski broj te boji čvorove na platnu.
•	display_harmonic_index: Prikazuje prozor s izračunatim harmonijskim kromatskim brojem.
•	execute_coloring: Boji čvorove na platnu prema izračunatom harmonijskom kromatskom broju.
•	generate_graph: Generira graf na temelju veza između čvorova.
•	clear_canvas: Briše sve elemente s platna i resetira stanje aplikacije.
•	Funkcija dodaj_vrh: Rekurzivno dodaje čvorove u graf i provjerava mogućnosti bojanja čvorova tako da se zadovolje uvjeti harmonijskog kromatskog broja. Parametri funkcije su:
o	L: Lista boja dodijeljenih čvorovima.
o	boje: Trenutni broj boja korištenih za bojanje.
o	Susjedi: Lista susjedstva za svaki čvor.
o	n: Ukupan broj čvorova u grafu.
o	susjedi_boje: Lista susjedstva za svaku boju.
