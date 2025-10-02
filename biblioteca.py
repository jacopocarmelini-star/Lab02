def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        with open("biblioteca.csv", "r") as biblioteca:
            lista = []
            for line in biblioteca:
                riga = line.split(",")
                if len(riga) == 5:
                    lista.append({"Titolo": riga[0], "Autore": riga[1],
                                  "Anno": int(riga[2]), "N_pagine": int(riga[3]), "N_sezione": int(riga[4])})
                else:
                    continue
            biblioteca.close()
            print(lista)
            return lista

    except FileNotFoundError:
        return None



def aggiungi_libro(lista, biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    lunghezzaLista = len(lista)
    Num_sezioni = []

    for libro in lista:
        if libro["Titolo"] == titolo: #and libro["Autore"] ==autore and libro["Anno"]==anno and libro["N_pagine"]==pagine and libro["N_sezione"]==sezione:
           return None
        Num_sezioni.append(libro["N_sezione"])

    if sezione not in Num_sezioni:
        return None

    lista.append({"Titolo": titolo, "Autore": autore,
                  "Anno": int(anno), "N_pagine": int(pagine), "N_sezione": int(sezione)})

    if lunghezzaLista < len(lista):  # per verificare il corretto inserimento del libro
        print("Libro inserito con successo")

    try:
        with open(file_path, "a") as biblioteca:
            libroNuovo = f"{titolo},{autore},{anno},{pagine},{sezione}\n"
            biblioteca.write(libroNuovo)


    except FileNotFoundError:
        return None


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

