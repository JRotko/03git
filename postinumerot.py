import http_pyynto


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        nimi = nimi.replace(" ", "")
        nimi = nimi.replace("-", "")

        if nimi not in paikat:
            paikat[nimi] = []

        paikat[nimi].append(numero)

    return paikat


postinumerot = http_pyynto.hae_postinumerot()

def etsi_postinumerot(toimipaikka):
    toimipaikat = ryhmittele_toimipaikoittain(postinumerot)
    toimipaikka = toimipaikka.replace(" ", "")
    toimipaikka = toimipaikka.replace("-", "")
    
    if toimipaikka in toimipaikat:
        toimipaikat[toimipaikka].sort()

        loydetyt_str = ', '.join(toimipaikat[toimipaikka])
        print('Postinumerot: ' + loydetyt_str)
    else:
        print('Toimipaikkaa ei löytynyt')

def main():

    toimipaikka = input('Kirjoita postitoimipaikka: ').strip().upper()
    etsi_postinumerot(toimipaikka)

if __name__ == '__main__':
    main()