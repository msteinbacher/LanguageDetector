from langdetect import *      # Bibliothek zur Spracherkennung
from iso639 import languages  # Sprachenname auf Basis der iso639 Abkuerzungen

if __name__ == '__main__':
    # Beispieltexte
    texte = (
        "This is my sample text",               # Englisch, 100%
        "Das ist mein Beispieltext",            # Deutsch, 100%
        "Questo è il mio testo di esempio",     # Italienisch, 100%
        "Detta är min provtext",                # Schwedisch, 100%
        "Tämä on minun otos teksti",            # Finnisch, 100%
        "Dette er min eksempeltekst",           # Norwegisch, 100%
        "Dette er min prøvetekst, " +
        "der ser lidt anderledes ud.",          # Dänisch, 100%
        "Toto je můj ukázkový text"             # Tschechisch, 85.71%
    )
    # Alle Texte werden ueberprueft
    for text in texte:
        result = detect_langs(text)         # Ueberpruefung des
        best = result[0]                    # bestes Ergebnis uebernehmen
        prob = best.prob * 100              # Wahrscheinlichkeit in % errechnen
        short = best.lang                   # Iso639-Abkuerzung der Sprache
        is_reliable = best.prob > 0.5       # Ergebnis ist bei >50% vertrauenswuerdig
        long = languages.get(part1=short)   # Sprache auf Basis des ISo639-Codes ermitteln

        print('  Language: %s' % long.name)        # Ausgabe des Sprachennamens
        print('  reliability: %.2f' % prob)        # Vertraueswuerdigkeit in % 2 Dezimalstellen
        print('  reliable: %s' % is_reliable )     # Ist die Erkennung vertrauenswurdig?
        print('  short name: %s' % short)          # Iso639-Abkuerzung der Sprache
