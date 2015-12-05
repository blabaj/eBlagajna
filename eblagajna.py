# -*- coding: utf-8 -*-
def povejCeno(izdelek):
    izdelek = izdelek.lower()
    izdelki = {"mleko" : 2.99, "banane" : 1, "jogurt" : 0.65, "kivi" : 2.30}

    if izdelek in izdelki.keys():
        return izdelki[izdelek]
    else:
        napaka = "Napaka izdelek ne obstaja ali pa ga ni na zalogi"
        return napaka

def main():
    artikel = raw_input("Naziv artikla: ")
    print povejCeno(artikel)

if __name__ == '__main__':
    main()